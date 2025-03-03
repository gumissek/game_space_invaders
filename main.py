# zrobic layout ( wynik, zycia etc)
# zrobic gracza
# zrobic movement gracza prawo lewo
# zrobic strzelanie ( kulka)
# zrobic obiekty ( przeciwnikow )
# zrobic movement przeciwkonkow zeby szly w dol
# zrobic dodawanie punktow za kazdego zabitego przeciwnika
# jesli sie skoncza przeciwnicy to przejsc na kolejny lvl

from turtle import Screen
from layout import DownSeparator, UpSeparator
from scoreboard import Scoreboard

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 900

#window config
window = Screen()
window.bgcolor('black')
window.setup(width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
window.title('Space invaders - gumissek')
window.listen()

#layout
down_separator=DownSeparator(WINDOW_WIDTH,WINDOW_HEIGHT)
up_separator=UpSeparator(WINDOW_WIDTH,WINDOW_HEIGHT)
score_counter=Scoreboard(WINDOW_WIDTH,WINDOW_HEIGHT,'score')
lives_counter=Scoreboard(WINDOW_WIDTH,WINDOW_HEIGHT,'lives')

#



window.exitonclick()
