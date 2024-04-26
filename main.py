import settings
import sounds
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from table_art import Artist
from time import sleep
from tkinter import TclError


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=settings.SCREEN_WIDTH, height=settings.SCREEN_HEIGHT)

    screen.register_shape("rectangle", settings.PADDLE_COORDINATES)

    # delay (seconds) before the game loop repeats, effectively setting the speed
    SPEED = settings.GAME_STARTING_SPEED

    screen.bgcolor("black")
    screen.title("Pongaroo")

    # show every screen update
    screen.tracer(0)

    paddle1 = Paddle()
    ball = Ball()
    scoreboard = Scoreboard()

    # turtle object that draws the score
    artist = Artist()

    # slight delay before the game starts
    sleep(1)

    # close the game
    screen.onkeypress(
        key=settings.GAME_EXIT_KEY, 
        fun=screen.bye
    )

    # paddle keys
    screen.onkeypress(
        key=settings.PADDLE_UP_KEY, 
        fun=paddle1.paddle_up
    )
    screen.onkeypress(
        key=settings.PADDLE_DOWN_KEY, 
        fun=paddle1.paddle_down
    )

    try:
        while True:
            screen.listen()

            #the loop delay controls how fast the ball moves
            sleep(SPEED) 

            ball.move()
    
            wall_collision = ball.wall_collision()
            paddle_collision = ball.paddle_collision(paddle1.coordinates)
            
            if wall_collision or paddle_collision:
                collision = wall_collision if wall_collision else paddle_collision
                
                ball.set_bounce_angle(collision)

                if wall_collision:
                    sounds.pool.apply_async(sounds.wall_bounce_sound)

                elif paddle_collision:
                    sounds.pool.apply_async(sounds.paddle_bounce_sound)

                    scoreboard.add_point()

                    SPEED *= .95

            # if the ball escaped, pause and then create a new ball and  
            # reset the score and speed
            if ball.ball_escaped():

                sleep(1.5)

                ball.hideturtle()
                ball = Ball()

                scoreboard.erase_points()

                SPEED = settings.GAME_STARTING_SPEED

                paddle1.setposition(settings.PADDLE_POS_START)

            screen.update()

    # handle error when closing the game in the middle of a loop
    except TclError:
        pass