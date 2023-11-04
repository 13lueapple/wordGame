import pygame, os, sys
from utils import button
pygame.init()

class menu:
    def __init__(self, display: pygame.Surface, displaySize: tuple) -> None:
        self.display = display
        self.WIDTH, self.HEIGHT = displaySize
        
    def run(self):
        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
                    
        self.mPos = pygame.mouse.get_pos()
        self.display.fill((0,0,0))
                    
                    
                    
class levelMenu(menu):
    def __init__(self, display, displaySize):
        super().__init__(display, displaySize)
        self.buttonList = [
            [button('Map 1'), 'stage1'], #버튼, 버튼을 눌렀을 때 실행할 것의 이름
            [button('Map 2'), 'mainMenu'],
            [button('Map 3'), 'mainMenu'],
            [button('Back'), 'mainMenu']
        ]
    
    def run(self):
        super().run()
        
        for index, (button, func) in enumerate(self.buttonList):
            button.draw((self.WIDTH//2 - button.getSize()[0]//2, 100 + (index * button.getSize()[1])), self.display)
            button.check(self.mPos, self.click, func)

        pygame.display.update()

class mainMenu(menu):
    def __init__(self, display, displaySize):
        super().__init__(display, displaySize)
        self.buttonList = [
            [button('Play'), 'levelMenu'],
            [button('Exit'), 'exitGame']
        ]
        
        
    def run(self):
        super().run()
    
        for index, (button, func) in enumerate(self.buttonList):
            button.draw((self.WIDTH//2 - button.getSize()[0]//2, 100 + (index * button.getSize()[1])), self.display)
            button.check(self.mPos, self.click, func)
        
        pygame.display.update()