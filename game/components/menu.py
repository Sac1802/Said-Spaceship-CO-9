import pygame
from game.utils.constants import FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, WALLPAPER
class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    
    def __init__(self, message):
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.icon = pygame.transform.scale(ICON, (120, 80))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        self.update_message(message)
        self.update_score(message)
        self.update_score_max(message)
    
    def events(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    on_start()
    
    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.wallpaper, [0, 0])
        screen.blit(self.text, self.text_rect)     
        screen.blit(self.icon, self.icon_rect)      
        screen.blit(self.text_score, self.text_rect_score)
        screen.blit(self.text_score_max, self.text_rect_score_max)       
        pygame.display.flip()
    
    def update_message(self, message):
        self.message = message
        self.text = self.font.render(self.message, True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        self.wallpaper = pygame.transform.scale(WALLPAPER, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
    def update_score(self, message):
        self.message = message
        self.text_score = self.font.render(self.message, True, (255, 255, 255))
        self.text_rect_score = self.text.get_rect()
        self.text_rect_score.center = (self.HALF_SCREEN_WIDTH + 45, self.HALF_SCREEN_HEIGHT + 50)
        
    def update_score_max(self, message):
        self.message = message
        self.text_score_max = self.font.render(self.message, True, (255, 255, 255))
        self.text_rect_score_max = self.text.get_rect()
        self.text_rect_score_max.center = (self.HALF_SCREEN_WIDTH - 5, self.HALF_SCREEN_HEIGHT + 100)
        
    def draw_update_power_up(self, screen, message, x=HALF_SCREEN_WIDTH, y=HALF_SCREEN_HEIGHT, color=(0,0,0)):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)
    