from turtle import Turtle

STARTING_POSITION = (0, -350)
MOVESENS = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("./img/jedi_small.gif")
        # self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.goto(STARTING_POSITION)

    def go_right(self):
        if self.xcor() < 320 - MOVESENS:
            new_x = self.xcor() + MOVESENS
            self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() > -320 + MOVESENS:
            new_x = self.xcor() - MOVESENS
            self.goto(new_x, self.ycor())
