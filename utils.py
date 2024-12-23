import pygame, os, sys
pygame.init()

def fileDir(relativeDir: str):
    # return os.path.join(__file__, relativeDir)
    return os.path.join(os.path.dirname(__file__), relativeDir)

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

class baseloop:
    def __init__(self, gameSetting, stateMachine) -> None:
        self.display: pygame.Surface = gameSetting['display']
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

        self.display.fill(pygame.Color("grey6"))
        self.mPos = pygame.mouse.get_pos()
    

class ExitGame:
    def run(self):
        sys.exit()

class StateMachine:    
    def init(self, state):
        self.state = state

    def set(self, funcName: str):
        self.currentState = self.state[funcName]
    
    def run(self):
        self.currentState.run()
        
    def refresh(self, name):
        self.state[name].init()
                    
        
    
        
class Button:
    def __init__(self, name, fg=(255,255,255)) -> None:
        self.name = name
        self.font = pygame.font.Font(fileDir("Galmuri11.ttf"), 40)
        self.surface = self.font.render(self.name, False, fg)
        
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
    
    
    
def gradientColorTextRender(text: str, font: pygame.font, fcolor: list):
    """
    fcolor는 반드시 pygame.Color(색상)을 두개 이상!!
    text는 두줄까지만 표시
    """
    textWidth = []
    surfaceList = []
    textList = text.split("\n")
    startColor: pygame.Color = fcolor[0]
    endColor: pygame.Color = fcolor[1]
    
    for text in textList:
        textWidth.append(0)
        innerSurfaceList = []
        for i, char in enumerate(text):
            color = pygame.Color(
                startColor.r + (endColor.r - startColor.r) * i / len(text),
                startColor.g + (endColor.g - startColor.g) * i / len(text),
                startColor.b + (endColor.b - startColor.b) * i / len(text),
            )
            surface = font.render(char, True, color)
            innerSurfaceList.append(surface)
            textWidth[textList.index(text)] += surface.get_size()[0]
        surfaceList.append(innerSurfaceList)
    
    # breakpoint()
    finalTextSurface = pygame.Surface((max(textWidth), font.get_height() * len(textList)))
    finalTextSurface.set_colorkey(pygame.Color('black'))
    x, y = 0, 0
    for innerSurfaceList in surfaceList:
        for surface in innerSurfaceList:
            finalTextSurface.blit(surface, (x, y))
            x += surface.get_size()[0]
        x = 0
        y += font.get_height()
    
    return  finalTextSurface