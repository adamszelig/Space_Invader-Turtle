from turtle import Turtle

SPEED = 15

class BulletTie:
    def __init__(self):
        self.bullets = []
        self.speed = SPEED
        self.stop = 0

    def create_bullets(self, p_x, p_y):
            self.bullet = Turtle()
            self.bullet.shape("square")
            self.bullet.color('red')
            self.bullet.shapesize(stretch_wid=0.8, stretch_len=0.2)
            self.bullet.penup()
            self.bullet.setpos(x=p_x, y=p_y-10)
            self.bullets.append(self.bullet)


    def move(self):
        for self.bullet in self.bullets:
            new_y = self.bullet.ycor() - self.speed
            self.bullet.setpos(x=self.bullet.xcor(), y=new_y)
            if new_y < -400:
                self.bullet.hideturtle()
                self.bullets.remove(self.bullet)