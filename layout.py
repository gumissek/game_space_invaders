from turtle import Turtle

class DownSeparator(Turtle):
    def __init__(self,win_width,win_height):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.sety(-win_height/2*0.8)
        self.shapesize(0.2,win_width)


class UpSeparator(Turtle):
    def __init__(self, win_width, win_height):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.sety(win_height / 2 * 0.8)
        self.shapesize(0.2, win_width)


