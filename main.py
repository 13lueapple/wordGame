import pygame
from utils import stateMachine
pygame.init()

WIDTH, HEIGHT = 1200, 900
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

stateMachine.stateChange("mainMenu")
while True:
    clock.tick(60)
    stateMachine.currentState()





