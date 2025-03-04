import random
from turtle import Turtle


from settings import WINDOW_WIDTH, WINDOW_HEIGHT
import numpy as np


class EnemyManager(Turtle):
    def __init__(self):
        super().__init__()
        self.enemies_list = []
        self.enemy_move = 1
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

    def enemy_increase_speed(self):
        self.enemy_move+=1

class EnemyBulletManager(Turtle):
    def __init__(self,enemies_list:list):
        super().__init__()
        self.enemy_bullet_list=[]
        self.enemies_list=enemies_list
        self.enemy_bullet_move=-3
        self.enemy_bullets_frequency=150

    def create_enemy_bullet(self):
        random_enemy=random.choice(self.enemies_list)
        new_bullet = Turtle()
        new_bullet.penup()
        new_bullet.color('yellow')
        new_bullet.shape('square')
        new_bullet.shapesize(0.2, 0.1)
        new_bullet.goto(random_enemy.xcor(),random_enemy.ycor())
        self.enemy_bullet_list.append(new_bullet)

    def enemy_bullets_move(self):
        for bullet in self.enemy_bullet_list:
            bullet.goto(bullet.xcor(),bullet.ycor()+self.enemy_bullet_move)