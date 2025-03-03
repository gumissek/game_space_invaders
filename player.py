from turtle import Turtle
from settings import WINDOW_HEIGHT, WINDOW_WIDTH


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('triangle')
        self.penup()
        self.setpos(0, -WINDOW_HEIGHT / 2 * 0.73)
        self.color('white')
        self.shapesize(WINDOW_WIDTH * 0.003)
        self.setheading(90)

    def player_move_left(self):
        if self.xcor() > -WINDOW_WIDTH / 2 + 20:
            self.goto(self.xcor() - 10, self.ycor())

    def player_move_right(self):
        if self.xcor() < WINDOW_WIDTH / 2 - 30:
            self.goto(self.xcor() + 10, self.ycor())


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.bullets_list = []
        self.bullets_speed = 0.02
        self.bullet_frequency = 25

    def create_bullet(self, x_cor, y_cor):
        new_bullet = Turtle()
        new_bullet.penup()
        new_bullet.color('white')
        new_bullet.shape('square')
        new_bullet.shapesize(0.2, 0.1)
        new_bullet.goto(x_cor, y_cor)
        self.bullets_list.append(new_bullet)

    def bullets_move(self):
        print(len(self.bullets_list))
        for bullet in self.bullets_list:
            bullet.goto(bullet.xcor(), bullet.ycor() + 5)

    def bullet_increase_freq(self):
        self.bullet_frequency -= 1

    def bullet_increase_speed(self):
        self.bullets_speed *= 0.98
