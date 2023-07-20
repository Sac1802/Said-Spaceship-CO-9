import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TYPE, DEFAULT_TYPE, TYPE_SHIP, TYPE_POWER
class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 30
    Y_POS = 500
    SPACESHIP_WIDTH = 60
    SPACESHIP_HEIGHT = 50
    
    def __init__(self):
        self.type = PLAYER_TYPE
        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.power_up_type = DEFAULT_TYPE
        self.power_up_time_up = 0
        
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
            if self.power_up_type != DEFAULT_TYPE :
                self.shoot_power_up(bullet_manager)
            else: 
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
    
    def shoot_power_up(self, bullet_manager):
        bullet_manager.add_bullet_power_up(self)
            
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def pick_power_up(self, time_up, type, image):
        self.image = pygame.transform.scale(image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.power_up_time_up = time_up
        self.power_up_type = type
        
    def draw_power_up(self, game):
        if self.power_up_type != DEFAULT_TYPE:
            time_left = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_left >= 0:
                game.menu.draw_update_power_up(game.screen, f"{self.power_up_type.capitalize()} is enable for {time_left} seconds", y=50, color=(255, 255, 255))
            else:
                self.power_up_type = DEFAULT_TYPE
                self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))