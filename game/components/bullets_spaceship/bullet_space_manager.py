import pygame
from game.components.bullets_spaceship.bullet_spaceship import BulletSpaceship
from game.utils.constants import PLAYER_TYPE

class BulletSpaceManager:
    def __init__(self):
        self.bullets = []
        
    def update(self, game):
        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    game.score += 1
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    
            
    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
            
    def add_bullet1(self, spaceship):
        if spaceship.type == PLAYER_TYPE and not self.bullets:
            self.bullets.append(BulletSpaceship(spaceship))