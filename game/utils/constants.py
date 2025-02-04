import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
TEXT_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

WALLPAPER = pygame.image.load(os.path.join(IMG_DIR, "Other/galaxia_juego.png"))

RESET = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))

HEART = pygame.image.load(os.path.join(IMG_DIR, "Other/SmallHeart.png"))

ICON_GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))


DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
ENEMY_TYPE = 'enemy'
PLAYER_TYPE = 'player'
TYPE_SHIP = 'spaceshield'
TYPE_POWER = 'enemy2'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_UP2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_up2.png"))
FONT_STYLE = os.path.join(TEXT_DIR, 'Other/fount.ttf')
