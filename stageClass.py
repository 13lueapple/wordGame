import pygame, sys, os
pygame.init()

class stage1:
    wordBlockList = []
    @classmethod
    def run(cls):
        cls.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cls.click = True

        display.fill((0,0,0))

        cls.mPos = pygame.mouse.get_pos()
        buttonDraw('Quit', (30,HEIGHT - 100), cls.mPos, cls.click, display, 'levelMenu')

        if wordBlock.instanceNumber < wordBlock.instanceMax:
            cls.wordBlockList.append(wordBlock())

        for i in cls.wordBlockList:
            i.draw()
            i.posYChange(1)
        
        checkWordTyping.draw()

        pygame.display.update()