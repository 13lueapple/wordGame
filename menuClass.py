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
                    
                    
                    
class howToPlay(menu):
    def __init__(self, display, displaySize):
        super().__init__(display, displaySize)
        self.buttonList = [
            [button('뒤로가기'), 'mainMenu']
        ]
    
    def run(self):
        super().run()
        
        for index, (button, func) in enumerate(self.buttonList):
            button.draw((self.WIDTH//2 - button.getSize()[0]//2, 600 + (index * button.getSize()[1])), self.display)
            button.check(self.mPos, self.click, func)

        pygame.display.update()

class mainMenu(menu):
    def __init__(self, display, displaySize):
        super().__init__(display, displaySize)
        self.buttonList = [
            [button('시작하기'), 'stage'],
            [button('게임방법'), 'howToPlay'],
            [button('나가기'), 'exitGame']
        ]
        
        
    def run(self):
        super().run()
    
        for index, (button, func) in enumerate(self.buttonList):
            button.draw((self.WIDTH//2 - button.getSize()[0]//2, 100 + (index * button.getSize()[1])), self.display)
            button.check(self.mPos, self.click, func)
        
        pygame.display.update()