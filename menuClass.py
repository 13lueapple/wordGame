import pygame, os, sys
from utils import Button, fileDir, baseloop, gradientColorTextRender
pygame.init()
        

        

class MainMenu(baseloop):
    def __init__(self, gameSetting, stateMachine):
        super().__init__(gameSetting, stateMachine)
        self.buttonList = [
            [Button('시작하기'), {"state" : "Stage", "refresh" : "Stage"}],
            [Button('나가기'), 'ExitGame']
        ]
        
        self.titleFont = pygame.font.Font(fileDir("../Galmuri11.ttf"), 100)
        self.title = gradientColorTextRender("제목뭐하지", self.titleFont, (pygame.Color("gold"), pygame.Color("goldenrod4")))
        
    def run(self):
        super().run()

        self.display.blit(self.title, (self.WIDTH//2 - self.title.get_size()[0]//2, 100))
        
        for index, (button, func) in enumerate(self.buttonList):
            button.draw((self.WIDTH//2 - button.getSize()[0]//2, (index * button.getSize()[1] + 400)), self.display)
            button.check(self.stateMachine, self.mPos, self.click, func)
        
        
                    
        pygame.display.update()