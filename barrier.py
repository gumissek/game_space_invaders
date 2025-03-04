from turtle import Turtle
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
import numpy as np


class BarrierManager(Turtle):
    def __init__(self):
        super().__init__()
        self.barrier_list = []

    def create_barrier(self, x_cor, y_cor):
        new_barrier = Turtle()
        new_barrier.penup()
        new_barrier.shape('square')
        new_barrier.color('white')
        new_barrier.shapesize(1, 1)
        new_barrier.goto(x_cor, y_cor)
        self.barrier_list.append(new_barrier)

    def create_barrier_grid(self):
        barrier_size = 40
        row_position = -WINDOW_HEIGHT / 2 * 0.5
        rows = 2
        space = 30
        x_cor_list = np.linspace(-WINDOW_WIDTH / 2 + space, WINDOW_WIDTH / 2 - space,
                                 num=int(WINDOW_WIDTH / barrier_size) + 1)
        for row in range(rows):
            for x_cor in x_cor_list:
                self.create_barrier(x_cor, row_position - row * barrier_size)
