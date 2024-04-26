import settings
from turtle import Turtle


class Paddle(Turtle):
    """
    Paddle that hits the ball.
    """
    def __init__(self):
        super().__init__()

        # we don't want to draw
        self.penup()

        # left side of the screen
        self.setposition(settings.PADDLE_POS_START)

        # know its position
        self.coordinates = self.position()

        self.color("white")
        self.shape("rectangle")

        self.paddle_up = lambda y_vector=settings.PADDLE_SPEED:self.move_paddle(y_vector)
        self.paddle_down = lambda y_vector=-settings.PADDLE_SPEED:self.move_paddle(y_vector)


    def move_and_update_coords(self, x, y):
        """
        Move the paddle and update the paddle's coordinates to match.
        """
        self.setposition(x, y)
        self.coordinates = (x, y)


    def move_paddle(self, y_vector):
        """
        Calculate the paddle's new coordinates and call move_and_update_coords to 
        move the paddle.
        """
        current_y = self.position()[1]

        # if it wouldn't go off the screen, then move the paddle
        if settings.PADDLE_STOP_BOTTOM < (current_y + y_vector) < settings.PADDLE_STOP_TOP:
            current_coordinates = list(self.position())

            x_coord = current_coordinates[0]

            new_y_coord = current_coordinates[1] + y_vector

            self.move_and_update_coords(x_coord, new_y_coord)

