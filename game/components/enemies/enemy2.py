import pygame, random
from game.components.enemies.enemy import Enemy

from game.utils.constants import ENEMY_2, SCREEN_HEIGHT


class Enemy2(Enemy):
    SPEED_X = 11
    SPEED_Y = 6
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))
        self.count = 0
        self.number_random = random.randint(1, 4)
        self.number = self.number_random
    
    def update(self, enemies, bullet_manager):
        super().update(enemies, bullet_manager)
        if self.number % 2 == 0:
            if self.rect.y > SCREEN_HEIGHT // 2:
                if self.count < 3:
                    self.rect.y = 20
                    self.count += 1
        
                    
    def shoot(self, bullet_manager):
        super().shoot(bullet_manager)