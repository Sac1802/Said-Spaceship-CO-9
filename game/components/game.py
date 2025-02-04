from game.components.menu import Menu
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.power_ups2.power_up_manager2 import PowerUpManager2
import pygame

from game.components.power_ups3.power_up_manager3 import PowerUpManager3
from game.components.bullets_spaceship.bullet_space_manager import BulletSpaceManager
from game.components.spaceship import Spaceship
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, HEART, ICON_GAME_OVER

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.bullet_space_manager = BulletSpaceManager()
        self.power_up_manager = PowerUpManager()
        self.power_up_manager2 = PowerUpManager2()
        self.power_up_manager3 = PowerUpManager3()
        
        self.menu = Menu("")
        self.score = 0
        self.score_max = 0
        self.death_count = 0
        self.lives = 3

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                self.menu.update_message("Please  press  the  ENTER  key!")
        pygame.display.quit()
        pygame.quit()
        
    def play(self):
        self.playing = True
        self.reset()
        self.bullet_space_manager.resect_bullet()
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()
        if self.score > self.score_max:
                self.score_max = 0
                self.score_max += self.score
               
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on_close()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_space_manager)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.bullet_space_manager.update(self)
        self.power_up_manager.update(self)
        self.power_up_manager2.update(self)
        self.power_up_manager3.update(self)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.player.draw_power_up(self)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.bullet_space_manager.draw(self.screen) 
        self.power_up_manager2.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.power_up_manager3.draw(self.screen)
        self.draw_score()
        self.draw_lives()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score:    {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 35)
        self.screen.blit(text, text_rect)
        
        
    def draw_lives(self):
        self.heart = pygame.transform.scale(HEART, (30, 30))
        self.rect = self.heart.get_rect()
        self.rect.x = 15
        self.rect.y = 20
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f" = {self.lives}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (100, 35)
        self.screen.blit(self.heart, (self.rect.x + 30, self.rect.y))
        self.screen.blit(text, text_rect)

    def show_menu(self):
        HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
        if self.death_count > 0:
            self.menu.icon = pygame.transform.scale(ICON_GAME_OVER, (500, 80))
            self.menu.icon_rect = (300, HALF_SCREEN_HEIGHT - 100)
            self.menu.update_message(f"You have died {self.death_count} times")
            self.menu.update_score(f"Your score is : {self.score}")
            self.menu.update_score_max(f"Your highest score is: {self.score_max}")
        self.menu.draw(self.screen)
        self.menu.events(self.on_close, self.play)
        
    def on_close(self):
        self.playing = False
        self.running = False
        
    def reset(self):
        self.enemy_manager.reset()
        self.bullet_space_manager.resect_bullet()
        self.power_up_manager.reset()
        self.power_up_manager2.reset()
        self.bullet_manager.reset(self)
