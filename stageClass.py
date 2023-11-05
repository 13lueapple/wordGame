import pygame, sys, random, re
from utils import button, fileDir
# from word import englishWord

englishWord = ['a','b','c']

pygame.init()

class stageMaster:
    def __init__(self, display: pygame.Surface, displaySize: tuple) -> None:
        self.wordBlockList = []
        self.display = display
        self.WIDTH, self.HEIGHT = displaySize
    
    def run(self):
        self.click = False
        self.text = None
        self.key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            if event.type == pygame.TEXTINPUT:
                self.text = event.text
            if event.type == pygame.KEYDOWN:
                self.key = event.key

        self.display.fill((0,0,0))
        self.mPos = pygame.mouse.get_pos()

class stage1(stageMaster):
    def __init__(self, display, displaySize) -> None:
        super().__init__(display, displaySize)
        self.buttonList = [
            [button('Back'), 'levelMenu']
        ]
        
    def run(self):
        super().run()
        
        for index, (button, func) in enumerate(self.buttonList):
            button.draw((self.WIDTH//2 - button.getSize()[0]//2-500, 800 + (index * button.getSize()[1])), self.display)
            button.check(self.mPos, self.click, func)
        

        # if wordBlock.instanceNumber < wordBlock.instanceMax:
        #     self.wordBlockList.append(wordBlock())

        # for i in self.wordBlockList:
        #     i.draw(self.display)
        #     i.posYChange(1, self.HEIGHT)
        
        checkWordTyping.draw(self.display, self.WIDTH, self.HEIGHT, self.text, self.key)
        
        pygame.display.update()
        
        
class wordBlock:
    instanceNumber = 0
    instanceMax = 6
    posList = [(x,y) for x in range(6) for y in range(6)]
    font = pygame.font.Font(fileDir("../Galmuri11.ttf"), 30)
    def __init__(self):
        self.word = random.choice(englishWord)
        self.surface = wordBlock.font.render(self.word, False, (255,255,255))
        wordBlock.instanceNumber += 1
        self.posY = 0
        self.posXMultiplier = wordBlock.posList.pop(random.randint(0, len(wordBlock.posList)-1))[0]

    def posYChange(self, amount, HEIGHT):
        if self.posY <= HEIGHT: self.posY += amount
        else: self.posY = 0
    
    def draw(self, display):
        display.blit(self.surface, (250*self.posXMultiplier, self.posY))
        
        
        
class checkWordTyping:
    typingBox = []
    font = pygame.font.Font(fileDir("../Galmuri11.ttf"), size=50)
    @classmethod
    def draw(cls, display, WIDTH, HEIGHT, text = None, key = None):
        if text is not None:
            cls.typingBox.append(text)
        if key == pygame.K_BACKSPACE:
                if len(cls.typingBox) > 0: cls.typingBox.pop()
        elif key == pygame.K_RETURN:
            cls.typingBox = []
                    

        fontSurface = cls.font.render("".join(str(i) for i in cls.typingBox), False, (255,0,0))
        print(cls.typingBox)
        display.blit(fontSurface, (WIDTH//2-fontSurface.get_rect()[2]//2, HEIGHT-100))