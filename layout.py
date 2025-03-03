from turtle import Turtle
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class DownSeparator(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.sety(-WINDOW_HEIGHT / 2 * 0.8)
        self.shapesize(0.2, WINDOW_WIDTH)


class UpSeparator(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.sety(WINDOW_HEIGHT / 2 * 0.8)
        self.shapesize(0.2, WINDOW_WIDTH)
