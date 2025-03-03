# zrobic layout ( wynik, zycia etc) ok
# zrobic gracza ok
# zrobic movement gracza prawo lewo ok
# zrobic strzelanie ( kulka) w trakcie
# zrobic obiekty ( przeciwnikow )
# zrobic movement przeciwkonkow zeby szly w dol
# zrobic dodawanie punktow za kazdego zabitego przeciwnika
# jesli sie skoncza przeciwnicy to przejsc na kolejny lvl
import time
from turtle import Screen
from layout import DownSeparator, UpSeparator
from scoreboard import Scoreboard
from player import Player, Bullet

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 900

# window config
window = Screen()
window.bgcolor('black')
window.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.title('Space invaders - gumissek')
window.tracer(0)
window.listen()

# layout
down_separator = DownSeparator(WINDOW_WIDTH, WINDOW_HEIGHT)
up_separator = UpSeparator(WINDOW_WIDTH, WINDOW_HEIGHT)
score_counter = Scoreboard(WINDOW_WIDTH, WINDOW_HEIGHT, 'score')
lives_counter = Scoreboard(WINDOW_WIDTH, WINDOW_HEIGHT, 'lives')

# player
player = Player(WINDOW_WIDTH, WINDOW_HEIGHT)
window.onkeypress(player.player_move_left, 'Left')
window.onkeypress(player.player_move_right, 'Right')

# pociski
bullet_manager = Bullet()
bullet_list = bullet_manager.bullets_list

loop_counter = 0
# mam zrobione pociski ktore leca do gory, zrobic dodawanie nowych pociskow i te ktore wyleca poza granice to maja zostac usuniete z listy
while lives_counter.lives > 0:
    window.update()
    # poruszanie sie przyciskow do przodu zmiana predkosci przyciskow i strzelania i czestotliwosci tworzenia pociskow
    time.sleep(bullet_manager.bullets_speed)
    bullet_manager.bullets_move()
    if loop_counter % bullet_manager.bullet_frequency == 0:
        bullet_manager.create_bullet(player.xcor(), player.ycor())

    # usuwanie pociskow ktore sa poza polem gry
    for bullet in bullet_list:
        if bullet.ycor() >= up_separator.ycor():
            bullet.color('red')
            bullet_list.remove(bullet)
    loop_counter += 1
window.exitonclick()
