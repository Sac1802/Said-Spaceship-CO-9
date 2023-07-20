from game.utils.constants import RESET, TYPE_POWER, ENEMY_UP2
from game.components.power_ups2.power_up2 import PowerUp2
class Shield2(PowerUp2):
    def __init__(self):
        super().__init__(RESET, TYPE_POWER, ENEMY_UP2)
        self.spaceship_image = ENEMY_UP2
        
        