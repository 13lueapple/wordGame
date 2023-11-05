import pygame, os, sys
pygame.init()

def fileDir(relativeDir: str):
    return os.path.join(__file__, relativeDir)

class exitGame:
    def run(self):
        sys.exit()

class stateMachine:    
    @classmethod
    def init(cls, stateList):
        cls.state = stateList
        
    @classmethod 
    def set(cls, funcName):
        cls.currentState = cls.state[funcName]
    
    @classmethod
    def run(cls):
        cls.currentState.run()
    
        
class button:
    def __init__(self, name, fg=(255,255,255), bg=(0,0,0)) -> None:
        self.font = pygame.font.Font(fileDir("../Galmuri11.ttf"), 40)
        self.surface = self.font.render(name, False, fg, bg)
        
        
    def draw(self, pos, display):
        self.rect = pygame.rect.Rect(pos[0], pos[1], self.surface.get_rect()[2], self.surface.get_rect()[3])
        display.blit(self.surface, pos)
    
    def check(self, mPos, click, func):
        if self.rect.collidepoint(mPos):
            if click == True:
                stateMachine.set(func)
                
    def getSize(self):
        return self.surface.get_rect()[2], self.surface.get_rect()[3]