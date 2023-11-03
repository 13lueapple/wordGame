import pygame, os, sys
pygame.init()

class stateMachine:
    def __init__(self, **state):
        self.state = state

    def stateChange(self, funcName):
        self.currentState = self.state[funcName]
        
class menuButton:
    font = pygame.font.Font(fileDir("../Galmuri11.ttf"), 40)
    def __init__(self, name, pos, fg=(255,255,255), bg=(0,0,0)) -> None:
        self.pos = pos
        self.surface = menuButton.font.render(name, False, fg, bg)
        self.rect = pygame.rect.Rect(pos[0], pos[1], self.surface.get_rect()[2], self.surface.get_rect()[3])
        
def buttonDraw(name, pos, mPos, click, display, func, fg=(255,255,255), bg=(0,0,0)):
    btn = menuButton(name, pos, fg, bg)
    display.blit(btn.surface, btn.pos)
    if btn.rect.collidepoint(mPos):
        if click == True:
            state.stateChange(func)
        
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