import pygame
from utils import stateMachine, exitGame
from stageClass import stage1
from menuClass import mainMenu, levelMenu
pygame.init()

WIDTH, HEIGHT = 1200, 900
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


stateMachine.init(
    {
        'mainMenu': mainMenu(display, (WIDTH, HEIGHT)),
        'levelMenu': levelMenu(display, (WIDTH, HEIGHT)),
        'exitGame': exitGame(),
        'stage1': stage1(display, (WIDTH, HEIGHT))
    }
    
)
stateMachine.set("mainMenu")
while True:
    clock.tick(60)
    stateMachine.run()





