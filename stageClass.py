import pygame, random
from utils import Button, fileDir, list_chunk, baseloop, gradientColorTextRender
from word import englishWord

pygame.init()
        

class Stage(baseloop):
    def __init__(self, gameSetting: dict, stateMachine) -> None:
        super().__init__(gameSetting, stateMachine)
        self.buttonList = [
            [Button('뒤로가기'), 'MainMenu']
        ]
    
    def init(self):
        self.wordList = WordList(self.display, self.HEIGHT, self.stateMachine)
        self.checkWordTyping = CheckWordTyping()

        self.running = 1
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.running = 0

            
            self.display.fill(pygame.Color("black"))

            self.tutorialFont = pygame.font.Font(fileDir("../Galmuri11.ttf"), 40)
            self.tutorialList = [
                self.tutorialFont.render(">주어진 90초 동안 최대한 많은 영어단어를 입력해 없앤다.", False, pygame.Color("white")),
                self.tutorialFont.render(">단어가 빨간 선에 닿거나, 시간이 모두 지나면 게임이 끝난다.", False, pygame.Color("red")),
                self.tutorialFont.render(">아이템은 두 종류가 있다.", False, pygame.Color("white")),
                gradientColorTextRender("단어들을 일정 시간동안 느리게 만드는 능력", self.tutorialFont, (pygame.Color('gold'), pygame.Color("goldenrod4"))),
                gradientColorTextRender("타이머에 2초를 추가하는 능력", self.tutorialFont, (pygame.Color('blue'), pygame.Color("red"))),
                self.tutorialFont.render("『단어를 느리게 하는 능력은 적절한 타이밍에 사용해야 한다.", False, pygame.Color("grey50")),
                self.tutorialFont.render("무작정 쓰다간 점수를 많이 얻지 못할 수 있다.』", False, pygame.Color("grey50"))
                
                ]
            
            for index, value in enumerate(self.tutorialList):
                self.display.blit(value, (self.WIDTH//2 - value.get_size()[0]//2, 200 + index * 50))

            self.display.blit(pygame.font.Font(fileDir("../Galmuri11.ttf"), 50).render("스페이스 바를 눌러 시작", False, pygame.Color("grey50")), (self.WIDTH//2 - 265, self.HEIGHT - 200))
            pygame.display.update()
        
        self.counter = 90
        self.counterFont = pygame.font.Font(fileDir("../Galmuri11.ttf"), 35)
        self.startTime = pygame.time.get_ticks()
                
        self.dt = 0
        
        self.score = 0
        self.scoreFont = pygame.font.Font(fileDir("../Galmuri11.ttf"), 35)
        
        self.speed = 20
        
        
    def run(self):
        super().run()
        

        
        success = self.checkWordTyping.drawAndCheck(self.display, self.WIDTH, self.HEIGHT, self.text, self.key)
        for n in range(15):
            for i, v in enumerate(self.wordList.wordList[n]):
                if v.checking == success:
                    self.wordList.wordList[n][i].changeBlank()
                    self.score += 100
                    if type(v) == SpecialWord:
                        if v.ability['ability'] == "timePlus":
                            self.counter += 2
                        if v.ability['ability'] == "slowWord":
                            self.abilityStartTime = pygame.time.get_ticks()
        try:               
            self.abilityElapsedTime = (pygame.time.get_ticks() - self.abilityStartTime) / 1000
            if self.abilityElapsedTime < 3:
                    self.speed = 5
            else: self.speed = 17
        except:
            pass
                    
                    
        self.wordList.draw(self.dt, self.speed)
            
        self.elapsedTime = (pygame.time.get_ticks() - self.startTime) / 1000
        if round(self.counter - self.elapsedTime) == 0:
            self.stateMachine.set('GameOver')
        
        self.display.blit(self.counterFont.render(f"남은 시간 : {str(round(self.counter - self.elapsedTime))}", False, pygame.Color("red")), (self.WIDTH - 600, self.HEIGHT - 50))
        
        for index, (button, func) in enumerate(self.buttonList):
            button.draw((self.WIDTH//2 - button.getSize()[0]//2-500, self.HEIGHT - (index * button.getSize()[1] + 50)), self.display)
            button.check(self.stateMachine, self.mPos, self.click, func)
            
        pygame.draw.rect(self.display, pygame.Color('red'), (0, self.HEIGHT - 80, 2000, 5))
        
        self.display.blit(self.scoreFont.render(f"점수 : {str(self.score)}", False, pygame.Color("grey50")), (self.WIDTH - 300, self.HEIGHT - 50))
        
        pygame.display.update()
        

class GameOver(baseloop):
    def __init__(self, gameSetting, stateMachine, StageInstance) -> None:
        super().__init__(gameSetting, stateMachine)
        self.StageInstance = StageInstance
        self.font = pygame.font.Font(fileDir("../Galmuri11.ttf"), 90)
        self.buttonList = [
            [Button('뒤로가기'), 'MainMenu']
        ]
        
    def run(self):
        super().run()
        self.fontSurface = self.font.render(f"Game Over", False, pygame.Color('red'))
        self.display.blit(self.fontSurface, (self.WIDTH//2 - self.fontSurface.get_size()[0]//2, self.HEIGHT//2 - self.fontSurface.get_size()[1]//2))

        self.fontSurface = self.font.render(f"점수 : {self.StageInstance.score}", False, pygame.Color('grey50'))
        self.display.blit(self.fontSurface, (self.WIDTH//2 - self.fontSurface.get_size()[0]//2, self.HEIGHT//2 - self.fontSurface.get_size()[1]//2 + 150))
        
        for index, (button, func) in enumerate(self.buttonList):
            button.draw((self.WIDTH//2 - button.getSize()[0]//2, 800 + (index * button.getSize()[1])), self.display)
            button.check(self.stateMachine, self.mPos, self.click, func)
            
        pygame.display.update()
        
        
class WordList:
    def __init__(self, display: pygame.Surface, HEIGHT, stateMachine) -> None:
        self.wordFont = pygame.font.Font(fileDir("../Galmuri11.ttf"), 23)
        self.tempEnglishWordList = list(englishWord.items())
        random.shuffle(self.tempEnglishWordList)
        self.tempWordList = [Word(i, self.wordFont) for i in self.tempEnglishWordList]
        self.tempWordIndexes = list(random.sample(range(len(self.tempWordList)), 240))
        self.tempWordIndexes = [self.tempWordIndexes[:150], self.tempWordIndexes[150:]]
        for index in self.tempWordIndexes[0]:
            self.tempWordList[index].changeBlank()
            
        for index in self.tempWordIndexes[1]:
            self.tempWord = self.tempWordList[index].word
            self.tempWordList[index] = SpecialWord(self.tempWord, self.wordFont)
        
        self.wordList = list_chunk(self.tempWordList, 4)
        self.x, self.y = 0, 0
        self.display = display
        self.HEIGHT = HEIGHT
        self.stateMachine = stateMachine
        
    def draw(self, dt, speed):
        self.rX, self.rY = 0,0
        for i in self.wordList:
            for j in i:
                self.display.blit(j.surface, (self.x + self.rX, self.y + self.rY))
                self.rX += j.size[0] + 30
            self.rX = 0
            self.rY -= j.size[1] + 40
            
        if self.y >= self.HEIGHT - 130:
            if [self.wordList[0][0].ignore, self.wordList[0][1].ignore, self.wordList[0][2].ignore, self.wordList[0][3].ignore] == [True, True, True, True]:
                del self.wordList[0]
                self.y -= self.wordList[0][3].size[1] + 40 
            else:   
                self.stateMachine.set("GameOver")
        elif dt < 0.1 : self.y += speed*dt
        
        
        
class Word:
    def __init__(self, word: tuple, font):
        self.font = font
        self.word = f'{word[0]}\n{word[1]}'
        self.checking = word[0]
        self.surface = self.font.render(self.word, True, (255,255,255))
        self.size = self.surface.get_size()[0], self.surface.get_size()[1]
        self.ignore = False
    
    def changeBlank(self):
        self.ignore = True
        self.surface = pygame.Surface(self.size)
        self.surface.set_colorkey(pygame.Color('black'))
    
class SpecialWord(Word):
    def __init__(self, word, font):
        self.font = font
        self.word = word
        self.checking = word.split("\n")[0]
        self.surface = self.font.render(self.word, True, (255,255,255))
        self.size = self.surface.get_size()[0], self.surface.get_size()[1]
        self.ignore = False
        self.specialAbility = [
            {"ability" : "timePlus", "color" : (pygame.Color("blue"), pygame.Color("red"))},
            {"ability" : "slowWord", "color" : (pygame.Color("gold"), pygame.Color("goldenrod4"))},
            {"ability" : "slowWord", "color" : (pygame.Color("gold"), pygame.Color("goldenrod4"))},
        ]
        self.ability = random.choice(self.specialAbility)
        self.surface = gradientColorTextRender(self.word, self.font, self.ability["color"])
    def changeBlank(self):
        super().changeBlank()
        
        
class CheckWordTyping:
    def __init__(self) -> None:
        self.typingBox = []
        self.font = pygame.font.Font(fileDir("../Galmuri11.ttf"), size=40)
        
    def drawAndCheck(self, display, WIDTH, HEIGHT, text = None, key = None):
        self.tempTypingBox = []
        if text is not None:
            self.typingBox.append(text)
        if key == pygame.K_BACKSPACE:
                if len(self.typingBox) > 0: self.typingBox.pop()
        elif key == pygame.K_RETURN:
            self.tempTypingBox = self.typingBox
            self.typingBox = []
            return "".join(str(i) for i in self.tempTypingBox)
                

        fontSurface = self.font.render("".join(str(i) for i in self.typingBox), False, pygame.Color("skyblue2"))
        display.blit(fontSurface, (WIDTH//2-fontSurface.get_rect()[2]//2 - 200, HEIGHT - 50))
        