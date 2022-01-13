import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEED = 10

class SpaceShip:
    def __init__(self):
        self.ships = []
        self.exploding_ships = []
        self.create_ships()
        self.speed = SPEED
        self.counter = 1
        self.direction = 1
        self.turn = False

    def create_ships(self):
        for i in range(7):
            for j in range(6):
                self.ship = Turtle()
                self.ship.shape('./img/tie_small.gif')
                self.ship.shapesize(stretch_wid=5, stretch_len=5)
                # self.ship.shape("square")
                # self.ship.shapesize(stretch_wid=1, stretch_len=1)
                self.ship.color(random.choice(COLORS))
                self.ship.penup()
                x = -355 + i * 70
                y = 50 + j * 40
                self.ship.setpos(x=x, y=y)
                self.ships.append(self.ship)


    def move(self):
        for self.ship in self.ships:
            new_x = self.ship.xcor() + self.speed * self.direction
            if self.counter % 50 == 0:
                new_y = self.ship.ycor() - 20
            else:
                new_y = self.ship.ycor()
            if new_x < -345 or new_x > 345:
                self.turn = True
            self.ship.setpos(x=new_x, y=new_y)

        if self.turn:
            self.direction *= -1
            self.turn = False

        self.counter += 1

        if self.counter % 10 == 0 and self.exploding_ships:
            self.exploding_ships[0].hideturtle()
            self.exploding_ships.pop(0)


    def boom(self, ship):
        self.exploding_ships.append(ship)
        self.ships.remove(ship)

        ship.shape('./img/boom.gif')
        ship.color("red")
        ship.shapesize(stretch_wid=0.5, stretch_len=0.5  )
        # self.ship.hideturtle()
        # self.ships.remove(self.ship)

    def get_random(self):
        firing_ship = random.choice(self.ships)
        coord = [firing_ship.xcor(), firing_ship.ycor()]
        return coord
