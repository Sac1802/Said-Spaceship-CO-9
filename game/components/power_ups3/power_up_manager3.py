import pygame, random
from game.components.power_ups3.shield3 import Shield3
class PowerUpManager3:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0
        
    def generate_power_up(self):
        current_time = pygame.time.get_ticks()
        if not self.power_ups and current_time >= self.when_appers:
            self.when_appers += random.randint(21000, 23000)
            self.power_ups.append(Shield3())
            
    def update(self, game):
        self.generate_power_up()
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if power_up.rect.colliderect(game.player.rect):
                game.lives += 1
                self.power_ups.remove(power_up)
                
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        