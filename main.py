import pygame, sys, os
from utils import stateMachine, wordBlock, checkWordTyping, buttonDraw
from stageClass import stage1
from menuClass import mainMenu, levelMenu
from word import englishWord
pygame.init()

WIDTH, HEIGHT = 1200, 900
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def fileDir(relativeDir: str):
    return os.path.join(__file__, relativeDir)

# with open(os.path.join(__file__, "../WordDict.txt"), 'r', encoding='utf-8') as f:
#     englishWord = eval(f.read())

state = stateMachine(
    mainMenu = mainMenu,
    levelMenu = levelMenu,
    exit = sys.exit,
    stage1 = stage1()
)
state.stateChange("mainMenu")
while True:
    clock.tick(60)
    state.currentState()





