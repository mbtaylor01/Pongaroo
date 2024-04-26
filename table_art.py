from turtle import Turtle


class Artist(Turtle):
    """
    Turtle object that draws the score and the dividing line.
    """
    def __init__(self):
        super().__init__()
        self.points = 0
        self.setposition(0, 180)
        self.pencolor("white")
        self.setposition(0, -200)
        self.hideturtle()