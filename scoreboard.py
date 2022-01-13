from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONT2 = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.life = 3
        self.update_score()

    def update_score(self):
        self.goto(-250, 350)
        self.write(f"Score: {self.score}", align="center", font=FONT)
        self.goto(250, 350)
        self.write(f"LIFE: {self.life}", align="center", font=FONT)

    def increase_score(self):
        self.score += 100
        self.clear()
        self.update_score()

    def decrease_life(self):
        self.life -= 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT2)

    def win(self):
        self.goto(0, 0)
        self.write("YOU WON JEDI", align="center", font=FONT2)