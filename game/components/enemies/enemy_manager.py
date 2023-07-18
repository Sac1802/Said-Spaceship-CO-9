import random
from game.components.enemies.enemy2 import Enemy2
from game.components.enemies.enemy import Enemy
class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self, game):
        if not self.enemies:
            choose_ship = random.choice([Enemy2, Enemy])
            self.enemies.append(choose_ship())
            
        for enemy in self.enemies:
            enemy.update(self.enemies, game.bullet_manager)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)