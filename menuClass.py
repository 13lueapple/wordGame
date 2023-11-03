import pygame, os, sys
pygame.init()

class menu:
    def __init__(self) -> None:
        pass
    def run(self):
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
class levelMenu(menu):
    def __init__(self):
        pass
    
    def run(self):
        super().run()
        
        display.fill((0,0,0))

        mPos = pygame.mouse.get_pos()
        buttonDraw('Map 1', (30,30), mPos, click, display, "stage1")
        buttonDraw('Map 2', (30,100), mPos, click, display, "mainMenu")
        buttonDraw('Map 3', (30,170), mPos, click, display, "mainMenu")
        buttonDraw('Back', (30,240), mPos, click, display, "mainMenu")
        
        pygame.display.update()

class levelMenu:
    def __init__(self):
        pass
    
    def run(self):
        super().run()
    
    display.fill((0,0,0))

    mPos = pygame.mouse.get_pos()
    buttonDraw('Play', (30,30), mPos, click, display, "levelMenu")
    buttonDraw('Exit', (30,100), mPos, click, display, "exit")
    
    pygame.display.update()