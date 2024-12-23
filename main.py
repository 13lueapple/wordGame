import pygame
from utils import StateMachine, ExitGame
from stageClass import Stage, GameOver
from menuClass import MainMenu

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
        'ExitGame': ExitGame(),
        'Stage': Stage(gameSetting, stateMachine)
    })
stateMachine.state["GameOver"] = GameOver(gameSetting, stateMachine, stateMachine.state['Stage'])

stateMachine.set("MainMenu")

def main():
    while True:
        pygame.display.set_caption('fps : ' + str(round(clock.get_fps())))
        stateMachine.run()
        
main()



