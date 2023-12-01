import pygame
import sys
from settings import *
from gamestatemanager import GameStateManager
from startscreen import Start
from mainscreen import MainScreen


class Game():
    def __init__(self):
        pygame.init
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.fps = FPS
        self.clock = pygame.time.Clock()
        self.initialGameState = "start"
        self.gameStateManager = GameStateManager(self.initialGameState)
        self.start = Start(self.screen, self.gameStateManager)
        self.mainScreen = MainScreen(self.screen, self.gameStateManager)
        
        self.states = {"start":self.start, "main":self.mainScreen}
              
    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False   
                
            self.draw()
            self.clock.tick(self.fps)
            
    def draw(self):
        self.states[self.gameStateManager.get_state()].run()
        pygame.display.update()
        
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit