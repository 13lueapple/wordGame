import pygame
from utils import StateMachine, ExitGame
from stageClass import Stage
from menuClass import MainMenu, HowToPlay, GameOver
pygame.init()

WIDTH, HEIGHT = 1200, 900
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

gameSetting = {
    "display" : display,
    "size" : (WIDTH, HEIGHT),
    "clock" : clock
}

stateMachine = StateMachine()
stateMachine.init({
        'MainMenu': MainMenu(gameSetting, stateMachine),
        'HowToPlay': HowToPlay(gameSetting, stateMachine),
        'ExitGame': ExitGame(),
        'Stage': Stage(gameSetting, stateMachine),
        'GameOver': GameOver(gameSetting, stateMachine)
    })

stateMachine.set("MainMenu")

while True:
    pygame.display.set_caption('fps : ' + str(round(clock.get_fps())))
    stateMachine.run()





