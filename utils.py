import pygame, os, sys
pygame.init()

def fileDir(relativeDir: str):
    return os.path.join(__file__, relativeDir)

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

class baseloop:
    def __init__(self, gameSetting, stateMachine) -> None:
        self.display = gameSetting['display']
        self.WIDTH, self.HEIGHT = gameSetting["size"]
        self.clock = gameSetting['clock']
        self.stateMachine = stateMachine
        
    def run(self):
        self.dt = self.clock.tick(60)/1000
        self.click = False
        self.text = None
        self.key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            if event.type == pygame.TEXTINPUT:
                self.text = event.text
            if event.type == pygame.KEYDOWN:
                self.key = event.key

        self.display.fill((0,0,0))
        self.mPos = pygame.mouse.get_pos()
    

class ExitGame:
    def run(self):
        sys.exit()

class StateMachine:    
    def init(self, state):
        self.state = state

    def set(self, funcName):
        self.currentState = self.state[funcName]
    
    def run(self):
        self.currentState.run()
        
    def refresh(self, name):
        self.state[name].init()
        
        
    
        
class Button:
    def __init__(self, name, fg=(255,255,255), bg=(0,0,0)) -> None:
        self.name = name
        self.font = pygame.font.Font(fileDir("../Galmuri11.ttf"), 40)
        self.surface = self.font.render(self.name, False, fg, bg)
        
    def draw(self, pos, display):
        self.rect = pygame.rect.Rect(pos[0], pos[1], self.surface.get_rect()[2], self.surface.get_rect()[3])
        display.blit(self.surface, pos)
    
    def check(self, stateMachine, mPos, click, func):
        if self.rect.collidepoint(mPos):
            if click == True:
                if type(func) == str: stateMachine.set(func)
                elif type(func) == dict:
                    stateMachine.refresh(func['refresh'])
                    stateMachine.set(func['state'])
                       
    def getSize(self):
        return self.surface.get_size()[0], self.surface.get_size()[1]