GAME_STARTING_SPEED = .003

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

PADDLE_SPEED = 10

PADDLE_UP_KEY = 'w'
PADDLE_DOWN_KEY = 's'
GAME_EXIT_KEY = 'c'

PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20

PADDLE_POS_START = (-1 * SCREEN_WIDTH / 2 + 40, 0)

# add a rectangle shape to use as a paddle
PADDLE_COORDINATES = (
    (-1 * PADDLE_HEIGHT / 2, PADDLE_WIDTH / 2), 
    (PADDLE_HEIGHT / 2, PADDLE_WIDTH / 2), 
    (PADDLE_HEIGHT / 2, -1 * PADDLE_WIDTH / 2), 
    (-1 * PADDLE_HEIGHT / 2, -1 * PADDLE_WIDTH / 2)
)

PADDLE_STOP_TOP = SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2
PADDLE_STOP_BOTTOM = -1 * SCREEN_HEIGHT / 2 + PADDLE_HEIGHT / 2

SCREEN_TOP = SCREEN_HEIGHT / 2 - 5
SCREEN_BOTTOM = -1 * SCREEN_HEIGHT / 2 + 15
SCREEN_RIGHT = SCREEN_WIDTH / 2 - 20

ARTIST_SCOREBOARD_POS = (0, SCREEN_TOP - 40)
ARTIST_HIGHSCORE_POS = (-200, -1 * SCREEN_HEIGHT / 2 + 40)

RANDOM_START_ANGLE = (30, 330)
MOVEMENT_LENGTH = 1
ANGLE_VARIANCE = (-5, 0, 5)
LOGGING = True


