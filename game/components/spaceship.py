import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TYPE
from game.components.bullets_spaceship.bullet_spaceship import BulletSpaceship
class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 30
    Y_POS = 500
    
    def __init__(self):
        self.type = PLAYER_TYPE
        self.image = pygame.transform.scale(SPACESHIP, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        
    def update(self, user_input, bullet_manager):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_SPACE]:
            self.shoot(bullet_manager)  

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
        else:
            self.rect.x = SCREEN_WIDTH
    
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        else:
            self.rect.x = -self.rect.width
            
    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10
            
    def move_up(self):
        if self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.y -= 10
            
    def shoot(self, bullet_manager):
        bullet_manager.add_bullet1(self)
            
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))