import pygame, sys, random, re
from utils import buttonDraw, fileDir
from main import display, HEIGHT, WIDTH, englishWord

pygame.init()

class stage1:
    wordBlockList = []
    def run(self):
        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

        display.fill((0,0,0))

        self.mPos = pygame.mouse.get_pos()
        buttonDraw('Quit', (30,HEIGHT - 100), self.mPos, self.click, display, 'levelMenu')

        if wordBlock.instanceNumber < wordBlock.instanceMax:
            self.wordBlockList.append(wordBlock())

        for i in self.wordBlockList:
            i.draw()
            i.posYChange(1)
        
        checkWordTyping.draw()

        pygame.display.update()
        
        
class wordBlock:
    instanceNumber = 0
    instanceMax = 6
    posList = [0,1,2,3,4,5]
    font = pygame.font.Font(fileDir("../Galmuri11.ttf"), WIDTH//4//15)
    def __init__(self):
        self.word = random.choice(englishWord)
        self.surface = wordBlock.font.render(self.word, False, (255,255,255))
        wordBlock.instanceNumber += 1
        self.posY = 0
        self.posXMultiplier = wordBlock.posList.pop(random.randint(0, len(wordBlock.posList)-1))

    def posYChange(self, amount):
        if self.posY <= HEIGHT: self.posY += amount
        else: self.posY = 0
    
    def draw(self):
        display.blit(self.surface, (250*self.posXMultiplier, self.posY))
        
        
        
class checkWordTyping:
    typingBox = []
    font = pygame.font.Font(fileDir("../Galmuri11.ttf"), size=50)
    @classmethod
    def draw(cls):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if re.compile("[a-zA-Z]").match(event.unicode):
                    cls.typingBox.append(event.unicode)
                elif event.key == pygame.K_BACKSPACE:
                    if len(cls.typingBox) > 0:
                        cls.typingBox.pop()

        
        fontSurface = cls.font.render("".join(cls.typingBox), False, (255,0,0))
        print(cls.typingBox)
        display.blit(fontSurface, (WIDTH//2, HEIGHT-100))