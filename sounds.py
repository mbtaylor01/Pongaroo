from multiprocessing import Pool
from playsound import playsound


def paddle_bounce_sound():
    playsound("8-bit-powerup.mp3")

def wall_bounce_sound():
    playsound("blip.mp3")

def game_over_sound():
    playsound("game-over-arcade.mp3")

pool = Pool(2)
