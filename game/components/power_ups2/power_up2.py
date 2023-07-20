from game.components.power_ups.power_up import PowerUp
import pygame
class PowerUp2(PowerUp):
    
    def __init__(self, image, type, spaceship_image):
        super().__init__(image, type, spaceship_image)
        self.image = pygame.transform.scale(image, (40, 60))
    
        
        
    