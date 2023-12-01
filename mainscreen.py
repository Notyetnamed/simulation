import pygame

class MainScreen():
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    
    def run(self):
        self.display.fill("blue")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.gameStateManager.set_state("start")