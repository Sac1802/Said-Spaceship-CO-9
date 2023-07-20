from game.utils.constants import SHIELD, SHIELD_TYPE, SPACESHIP_SHIELD
from game.components.power_ups.power_up import PowerUp
class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE, SPACESHIP_SHIELD)
        self.spaceship_image = SPACESHIP_SHIELD