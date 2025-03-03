from turtle import Turtle


class Player(Turtle):
    def __init__(self, win_width, win_height):
        super().__init__()
        self.win_width = win_width
        self.win_height = win_height
        self.shape('triangle')
        self.penup()
        self.setpos(0, -self.win_height / 2 * 0.73)
        self.color('white')
        self.shapesize(self.win_width * 0.003)
        self.setheading(90)

    def player_move_left(self):
        if self.xcor() > -self.win_width / 2 + 20:
            self.goto(self.xcor() - 10, self.ycor())

    def player_move_right(self):
        if self.xcor() < self.win_width / 2 - 30:
            self.goto(self.xcor() + 10, self.ycor())




class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.bullets_list=[]
        self.bullets_speed=0.01
        self.bullet_frequency=20

    def create_bullet(self,x_cor,y_cor):
        new_bullet=Turtle()
        new_bullet.penup()
        new_bullet.color('white')
        new_bullet.shape('square')
        new_bullet.shapesize(0.2, 0.1)
        new_bullet.goto(x_cor,y_cor)
        self.bullets_list.append(new_bullet)



    def bullets_move(self):
        print(len(self.bullets_list))
        for bullet in self.bullets_list:
            bullet.goto(bullet.xcor(),bullet.ycor()+5)

    def bullet_increase_freq(self):
        self.bullet_frequency-=1
    def bullet_increase_speed(self):
        self.bullets_speed*=0.98