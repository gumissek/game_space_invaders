import random
from turtle import Turtle
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
import numpy as np


class Enemy_manager(Turtle):
    def __init__(self):
        super().__init__()
        self.enemies_list = []
        self.enemy_move = 5
        self.enemy_frequency = 100

    def create_enemy(self, x_cor, y_cor):
        new_enemy = Turtle()
        new_enemy.penup()
        new_enemy.shape('circle')
        new_enemy.color('yellow')
        new_enemy.shapesize(1.1)
        new_enemy.goto(x_cor, y_cor)
        self.enemies_list.append(new_enemy)

    def enemies_move(self):
        tick = 0
        for enemy in self.enemies_list:
            if tick % 2 == 0 and enemy.xcor() > WINDOW_WIDTH / 2 - 50:
                self.enemy_move *= -1
                tick += 1
            elif tick % 2 == 0 and enemy.xcor() < -WINDOW_WIDTH / 2 + 50:
                self.enemy_move *= -1
                tick += 1

            enemy.goto(enemy.xcor() + self.enemy_move, enemy.ycor())

    def create_enemies_grid(self):

        rows = 4
        row_position = WINDOW_HEIGHT / 2 * 0.65
        enemy_size = 60
        x_cor_list = np.linspace(-WINDOW_WIDTH / 2 + 100, WINDOW_WIDTH / 2 - 100,
                                 num=int(WINDOW_WIDTH / enemy_size) + 1)
        for row in range(rows):
            for x_cor in x_cor_list:
                self.create_enemy(x_cor, row_position - row * enemy_size)
