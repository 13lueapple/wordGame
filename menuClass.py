import pygame, os, sys
from utils import Button, fileDir, baseloop
pygame.init()
        
class GameOver(baseloop):
    def __init__(self, gameSetting, stateMachine) -> None:
        super().__init__(gameSetting, stateMachine)
        self.font = pygame.font.Font(fileDir("../Galmuri11.ttf"), 90)
        self.buttonList = [
            [Button('뒤로가기'), 'MainMenu']
        ]
        
    def run(self):
        super().run()
        self.fontSurface = self.font.render(f"Game Over", False, pygame.Color('red'))
        self.display.blit(self.fontSurface, (self.WIDTH//2 - self.fontSurface.get_size()[0]//2, self.HEIGHT//2 - self.fontSurface.get_size()[1]//2))
        
        for index, (button, func) in enumerate(self.buttonList):
            button.draw((self.WIDTH//2 - button.getSize()[0]//2, 600 + (index * button.getSize()[1])), self.display)
            button.check(self.stateMachine, self.mPos, self.click, func)
            
        pygame.display.update()
        
                    
                    
                    
class HowToPlay(baseloop):
    def __init__(self, gameSetting, stateMachine):
        super().__init__(gameSetting, stateMachine)
        self.buttonList = [
            [Button('뒤로가기'), 'MainMenu']
        ]
    
    def run(self):
        super().run()
        
        for index, (button, func) in enumerate(self.buttonList):
            button.draw((self.WIDTH//2 - button.getSize()[0]//2, 600 + (index * button.getSize()[1])), self.display)
            button.check(self.stateMachine, self.mPos, self.click, func)

        pygame.display.update()

class MainMenu(baseloop):
    def __init__(self, gameSetting, stateMachine):
        super().__init__(gameSetting, stateMachine)
        self.buttonList = [
            [Button('시작하기'), {"state" : "Stage", "refresh" : "Stage"}],
            [Button('게임방법'), 'HowToPlay'],
            [Button('나가기'), 'ExitGame']
        ]
        
        
    def run(self):
        super().run()
    
        for index, (button, func) in enumerate(self.buttonList):
            button.draw((self.WIDTH//2 - button.getSize()[0]//2, 100 + (index * button.getSize()[1])), self.display)
            button.check(self.stateMachine, self.mPos, self.click, func)
                    
        pygame.display.update()