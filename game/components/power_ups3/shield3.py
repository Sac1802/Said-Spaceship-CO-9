from game.components.power_ups3.power_up3 import PowerUp3
from game.utils.constants import HEART
class Shield3(PowerUp3):
    def __init__(self):
        super().__init__(HEART)
    