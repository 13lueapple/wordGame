import pygame
from utils import stateMachine, exitGame
from stageClass import stage
from menuClass import mainMenu, howToPlay
pygame.init()

WIDTH, HEIGHT = 1200, 900
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


stateMachine.init(
    {
        'mainMenu': mainMenu(display, (WIDTH, HEIGHT)),
        'howToPlay': howToPlay(display, (WIDTH, HEIGHT)),
        'exitGame': exitGame(),
        'stage': stage(display, (WIDTH, HEIGHT))
    }
    
)
stateMachine.set("mainMenu")
while True:
    clock.tick(60)
    pygame.display.set_caption('fps : ' + str(round(clock.get_fps())))
    stateMachine.run()





