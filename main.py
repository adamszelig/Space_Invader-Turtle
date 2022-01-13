import time
from turtle import Screen, register_shape
from player import Player
from spaceship import SpaceShip
from scoreboard import Scoreboard
from bullet import Bullet
from bullet_tie import BulletTie
import random

REFRESH_TIME = 0.1
speed = REFRESH_TIME


screen = Screen()
screen.setup(width=800, height=800)
# screen.bgcolor("red")
screen.bgpic('./img/battle.gif')
screen.register_shape('./img/tie_small.gif')
screen.register_shape('./img/jedi_small.gif')
screen.register_shape('./img/boom.gif')
screen.tracer(0)

player = Player()
space = SpaceShip()
score = Scoreboard()
rambo = Bullet()
imperial = BulletTie()


def shoot():
    rambo.create_bullets(p_x=player.xcor(), p_y=player.ycor())

def shoot_tie():
    imperial.move()
    if random.randint(1, 4) % 4 == 0:
        coord = space.get_random()
        imperial.create_bullets(p_x=coord[0], p_y=coord[1])


screen.listen()
# screen.onkey(player.go_left, "Left")
# screen.onkey(player.go_right, "Right")
# screen.onkey(shoot, "space")
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")
screen.onkeypress(shoot, "space")


# def motion(event):
#     x, y = event.x, event.y
#     x = x - 400
#     y = (y - 400) * -1
#     print('{}, {}'.format(x, y))
#
# canvas = screen.getcanvas()
# canvas.bind('<Motion>', motion)


i = 0
game = True
while game:
    time.sleep(speed)
    screen.update()

    if not space.ships:
        game = False
        score.win()

    if score.life == 0:
        game = False
        score.game_over()

    space.move()
    shoot_tie()
    rambo.move()

    # HIT
    for ship in space.ships:
        for bullet in rambo.bullets:
            if ship.distance(bullet) < 20:
                bullet.hideturtle()
                rambo.bullets.remove(bullet)
                space.boom(ship)
                score.increase_score()

    # PLAYER HIT
    for bullet in imperial.bullets:
        if player.distance(bullet) < 20:
            bullet.hideturtle()
            imperial.bullets.remove(bullet)
            score.decrease_life()

    # Collision
    for ship in space.ships:
        if player.distance(ship) < 40:
            game = False
            score.game_over()


screen.exitonclick()