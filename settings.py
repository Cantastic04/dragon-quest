# Window settings
WIDTH = 1350
HEIGHT = 900
TITLE = "My Epic Shooter Game"
FPS = 60


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Gameplay Settings
FRAME_COUNTDOWN = FPS / 10
is_space_pressed = False

SELF_SPEED = 7
SHIP_HEART_POINTS = 3

FIREBALL_SPEED = SELF_SPEED * 1.5
FIREBALL_COOLDOWN = FPS / 3
FAST_COOLDOWN = FPS / 6

ENEMY_SPEED = SELF_SPEED
ENEMY_FIRST_MOVE_COOLDOWN = FPS * 3

ARROW_SPEED = SELF_SPEED
ARROW_COOLDOWN = FPS / 10

ITEM_TIMER = FPS * 3

BACKGROUND_SPEED = 6
