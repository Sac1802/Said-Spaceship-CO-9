import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
class PowerUp3():
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, SCREEN_WIDTH - 100)
        self.rect.y = 0
        
    def update(self, game_speed, power_up):
        self.rect.y += game_speed
        if self.rect.y >= SCREEN_HEIGHT:
            power_up.remove(self)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)