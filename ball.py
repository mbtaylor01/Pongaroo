import settings
import random
import sounds
from turtle import Turtle
from math import cos, sin, radians


class Ball(Turtle):
    """
    Ball that bounces around the screen.
    """
    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("circle")
        # don't want to draw
        self.penup()

        # shoot the ball at a random start angle
        self.travel_angle = random.choice(settings.RANDOM_START_ANGLE)

        self.coordinates = self.position()

        self.allow_snug = True


    def move_and_update_coords(self, x, y):
        """
        Move the ball and update the ball's coordinates to match.
        """
        self.setposition(x, y)
        self.coordinates = (x, y)


    def move(self):
        """
        Calculate how much the ball shifts in the x and y direction, then call 
        move_and_update_coords to move the ball.
        """
        current_y = self.coordinates[0]
        current_x = self.coordinates[1]
        # MOVEMENT_LENGTH is length of side C of a right triangle

        if self.travel_angle < 90:
            # cos(radians(self.travel_angle)) is cos(angle A)
            # C * cos(A) = length of side B
            # we add the length of side B to the x-coord of where the ball is now
            x_shift = settings.MOVEMENT_LENGTH * cos(radians(self.travel_angle)) + current_y

            # sin(radians(self.travel_angle)) is sin(angle A)
            # C * sin(A) = length of side A
            # we add the length of side A to the y-coord of where the ball is now
            y_shift = settings.MOVEMENT_LENGTH * sin(radians(self.travel_angle)) + current_x

        elif self.travel_angle < 180:
            # we want an angle < 90 for right triangle math
            angle = 180 - self.travel_angle

            # same math as if the angle was < 90, but make the shift negative
            x_shift = -1 * settings.MOVEMENT_LENGTH * cos(radians(angle)) + current_y

            # same math as if the angle was < 90
            y_shift = settings.MOVEMENT_LENGTH * sin(radians(angle)) + current_x

        elif self.travel_angle < 270:
            angle = self.travel_angle - 180
            x_shift = -1 * settings.MOVEMENT_LENGTH * cos(radians(angle)) + current_y
            y_shift = -1 * settings.MOVEMENT_LENGTH * sin(radians(angle)) + current_x

        elif self.travel_angle < 360:
            angle = 360 - self.travel_angle
            x_shift = settings.MOVEMENT_LENGTH * cos(radians(angle)) + current_y
            y_shift = -1 * settings.MOVEMENT_LENGTH * sin(radians(angle)) + current_x

        self.move_and_update_coords(x_shift, y_shift)


    def wall_collision(self):
        """
        Checks for and returns the wall the ball has collided with.
        """
        current_x = self.coordinates[0]
        current_y = self.coordinates[1]

        potential_obstacle = []

        distances = {
            "top": self.distance(current_x, settings.SCREEN_TOP),
            "bottom": self.distance(current_x, settings.SCREEN_BOTTOM),
            "right": self.distance(settings.SCREEN_RIGHT, current_y),
        }

        # the wall that is the closest to the ball
        potential_obstacle = [
            key for (key,value) in distances.items() if min(distances.values()) == value
        ]
        potential_obstacle = potential_obstacle[0]

        # if close enough to count as a collision
        if distances[potential_obstacle] < 1:
            return potential_obstacle
        

    def set_bounce_angle(self, obstacle):
        """
        Sets the new angle of the ball depending its current angle and the given obstacle.
        """
        if (obstacle == "top" and self.travel_angle < 180) or (obstacle == "bottom" and self.travel_angle > 180):
            self.travel_angle = 360 - self.travel_angle

        elif obstacle == "right":
            if 270 < self.travel_angle < 360:
                self.travel_angle = 540 - self.travel_angle 

            elif 0 < self.travel_angle < 90:
                self.travel_angle = 180 - self.travel_angle

        elif obstacle == "paddle":
            if 180 < self.travel_angle < 270:
                self.travel_angle = abs(540 - self.travel_angle)
                
            elif 180 > self.travel_angle > 90:
                self.travel_angle = abs(180 - self.travel_angle)
 

    def logging(self):
        """
        Log the ball's position and travel angle after every collision.
        """
        obstacle = ""
        current_x = self.coordinates[0]
        current_y = self.coordinates[1]

        if current_x == settings.SCREEN_RIGHT:
            obstacle = "right wall"
        elif current_y == settings.SCREEN_TOP:
            obstacle = "top wall"
        elif current_y == settings.SCREEN_BOTTOM:
            obstacle = "bottom wall"
        else:
            obstacle = "left paddle"

        print(f"position is now {self.coordinates} after hitting {obstacle}")
        print(f"travel angle is now {self.travel_angle} after hitting {obstacle}")

            
    def paddle_collision(self, paddle_coordinates):
        """
        """
        paddle_x = paddle_coordinates[0]
        paddle_y = paddle_coordinates[1]

        # extreme north and south y-coordinates of the paddle (must be ints for range)
        north_point = int(paddle_y + settings.PADDLE_HEIGHT / 2)
        south_point = int(paddle_y - settings.PADDLE_HEIGHT / 2)

        # for each y-coordinate in the paddle
        for y_coord in range(south_point, north_point + 1):
            # if ball is basically touching the paddle
            if self.distance((paddle_x + 15, y_coord)) < 1: 
                return "paddle"
        

    def ball_escaped(self):
        """
        Return True if the ball's coordinates are to the left of the paddle.
        """
        if self.coordinates[0] < -1 * settings.SCREEN_WIDTH / 2:
            sounds.pool.apply_async(sounds.game_over_sound)

            return True




