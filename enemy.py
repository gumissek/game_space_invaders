import random
from turtle import Turtle
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Enemy_manager(Turtle):
    def __init__(self):
        super().__init__()
        self.enemies_list = []
        self.enemy_speed = 3
        self.enemy_frequency = 100

    def create_enemy(self):
        new_enemy = Turtle()
        new_enemy.penup()
        new_enemy.shape('circle')
        new_enemy.color('yellow')
        new_enemy.shapesize(0.8)
        new_enemy.goto(random.randint(-int(WINDOW_WIDTH/2+30),int(WINDOW_WIDTH/2-30)), WINDOW_HEIGHT/2*0.75)
        self.enemies_list.append(new_enemy)

    def enemies_move(self):
        for enemy in self.enemies_list:
           enemy.goto(enemy.xcor(),enemy.ycor()-self.enemy_speed)