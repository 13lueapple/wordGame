import pygame, sys, random
from utils import Button, fileDir, list_chunk, baseloop
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
    def run(self):
        super().run()
        
        for index, (button, func) in enumerate(self.buttonList):
            button.draw((self.WIDTH//2 - button.getSize()[0]//2-500, 800 + (index * button.getSize()[1])), self.display)
            button.check(self.stateMachine, self.mPos, self.click, func)
        
        self.wordList.draw(self.dt)
        success = self.checkWordTyping.drawAndCheck(self.display, self.WIDTH, self.HEIGHT, self.text, self.key)
        for i, v in enumerate(self.wordList.wordList[0]):
            if v.checking == success:
                self.wordList.wordList[0].pop(i)
            
        
        pygame.display.update()
        
        
class WordList:
    def __init__(self, display: pygame.Surface, HEIGHT, stateMachine) -> None:
        self.tempEnglishWordList = random.sample(list(englishWord.items()), 400)
        self.tempWordList = [Word(i) for i in self.tempEnglishWordList]
        self.wordList = list_chunk(self.tempWordList, 4)
        self.x, self.y = 0,0
        self.display = display
        self.HEIGHT = HEIGHT
        self.stateMachine = stateMachine
        
    def draw(self, dt):
        self.rX, self.rY = 0,0
        for i in self.wordList:
            for j in i:
                self.display.blit(j.surface, (self.x + self.rX, self.y + self.rY))
                self.rX += j.size[0] + 10
            self.rX = 0
            self.rY -= j.size[1] + 10
            
        if self.y >= self.HEIGHT: self.stateMachine.set("GameOver")
        else: self.y += 10*dt
        
        
        
class Word:
    def __init__(self, word: tuple):
        self.font = pygame.font.Font(fileDir("../Galmuri11.ttf"), 25)
        self.word = word[0] + '\n' + word[1]
        self.checking = word[0]
        self.surface = self.font.render(self.word, False, (255,255,255))
        self.size = self.surface.get_size()[0], self.surface.get_size()[1]
    
# class BlankWord:
#     def __init__(self, size) -> None:
#         self.word = ""
#         self.surface = pygame.Surface((1,1))
#         self.size = size
    
        
        
        
class CheckWordTyping:
    def __init__(self) -> None:
        self.typingBox = []
        self.font = pygame.font.Font(fileDir("../Galmuri11.ttf"), size=50)
        
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
                

        fontSurface = self.font.render("".join(str(i) for i in self.typingBox), False, (255,0,0))
        display.blit(fontSurface, (WIDTH//2-fontSurface.get_rect()[2]//2, HEIGHT-100))