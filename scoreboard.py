import settings
from turtle import Turtle


class Scoreboard(Turtle):
    """
    Turtle object that updates the score.
    """
    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = 0
        self.setposition(settings.ARTIST_SCOREBOARD_POS)
        self.pencolor("white")
        self.write(f"Score: {self.points}", False, align="center", font='Courier')
        self.hideturtle()
        self.penup()
        self.setposition(settings.ARTIST_HIGHSCORE_POS)
        self.pendown()
        self.write(f"High Score: {self.high_score}", False, align="center", font='Courier')
        self.penup()


    def add_point(self):
        """
        Increment the score by one and update the high score.
        """
        self.points += 1
        self.clear()
        self.penup()
        self.setposition(settings.ARTIST_SCOREBOARD_POS)
        self.pendown()
        self.write(f"Score: {self.points}", False, align="center", font='Courier')
        self.penup()
        self.setposition(settings.ARTIST_HIGHSCORE_POS)
        self.pendown()
        self.write(f"High Score: {self.high_score}", False, align="center", font='Courier')
        self.penup()


    def erase_points(self):
        """
        Reset the points and update the high score.
        """
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        self.clear()
        self.penup()
        self.setposition(settings.ARTIST_SCOREBOARD_POS)
        self.pendown()
        self.write(f"Score: {self.points}", False, align="center", font='Courier')
        self.penup()
        self.setposition(settings.ARTIST_HIGHSCORE_POS)
        self.pendown()
        self.write(f"High Score: {self.high_score}", False, align="center", font='Courier')
        self.penup()
