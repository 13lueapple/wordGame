import pygame, os, sys
from menuClass import mainMenu, levelMenu
from stageClass import stage1
pygame.init()

def fileDir(relativeDir: str):
    return os.path.join(__file__, relativeDir)

class stateMachine:
    state = {
        "mainMenu" : mainMenu(),
        "levelMenu" : levelMenu(),
        "exit" : sys.exit,
        "stage1" : stage1()
    }
    @classmethod 
    def stateChange(cls, funcName):
        cls.currentState = cls.state[funcName]
        
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
            stateMachine.stateChange(func)