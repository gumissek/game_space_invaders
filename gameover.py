from turtle import Turtle
from settings import WINDOW_WIDTH,WINDOW_HEIGHT
FONT = ('Courier', 70, 'normal')
ALIGNMENT = 'center'



class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        background = Turtle()
        background.color('black')
        background.penup()
        background.shape('square')
        background.shapesize(WINDOW_WIDTH,WINDOW_HEIGHT)
        background.goto(0,0)

        text= Turtle()
        text.penup()
        text.color('white')
        text.write('GAME OVER',font=FONT,align=ALIGNMENT)