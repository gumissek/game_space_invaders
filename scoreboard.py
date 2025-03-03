from turtle import Turtle
FONT =('Courier', 25, 'normal')
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self, win_width, win_height, label: str):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.lives = 3
        if label.title() == 'Score':
            self.goto(-win_width / 4, win_height / 2 * 0.85)
            self.refresh_score()
        elif label.title() == 'Lives':
            self.goto(win_width / 4, win_height / 2 * 0.85)
            self.refresh_lives()


    def refresh_lives(self):
        self.write(f'Lives: {self.lives}',font=FONT,align=ALIGNMENT)


    def refresh_score(self):
        self.write(f'Score: {self.score}',font=FONT,align=ALIGNMENT)


    def add_point(self):
        self.clear()
        self.score += 1
        self.refresh_score()

    def remove_point(self):
        self.clear()
        self.score-=1
        self.refresh_score()


    def add_live(self):
        self.clear()
        self.lives+=1
        self.refresh_lives()
    def remove_live(self):
        self.clear()
        self.lives-=1
        self.refresh_lives()

