# zrobic layout ( wynik, zycia etc) ok
# zrobic gracza ok
# zrobic movement gracza prawo lewo ok
# zrobic strzelanie ( kulka) ok
# zrobic obiekty ( przeciwnikow ) ok
# zrobic movement przeciwkonkow zeby szly w dol ok
# zrobic dodawanie punktow za kazdego zabitego przeciwnika
# jesli sie skoncza przeciwnicy to przejsc na kolejny lvl
import time
from turtle import Screen
from enemy import Enemy_manager
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from layout import DownSeparator, UpSeparator
from scoreboard import Scoreboard
from player import Player, Bullet

# window config
window = Screen()
window.bgcolor('black')
window.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.title('Space invaders - gumissek')
window.tracer(0)
window.listen()

# layout
down_separator = DownSeparator()
up_separator = UpSeparator()
score_counter = Scoreboard('score')
lives_counter = Scoreboard('lives')

# player
player = Player()
window.onkeypress(player.player_move_left, 'Left')
window.onkeypress(player.player_move_right, 'Right')

# shooting
bullet_manager = Bullet()
bullet_list = bullet_manager.bullets_list

# enemies
enemy_manager=Enemy_manager()
enemies_list=enemy_manager.enemies_list


loop_counter = 0
# mam zrobione pociski ktore leca do gory, zrobic dodawanie nowych pociskow i te ktore wyleca poza granice to maja zostac usuniete z listy
while lives_counter.lives > 0:
    window.update()
    # poruszanie sie przyciskow do przodu zmiana predkosci przyciskow i strzelania i czestotliwosci tworzenia pociskow
    time.sleep(bullet_manager.bullets_speed)
    bullet_manager.bullets_move()
    enemy_manager.enemies_move()
    if loop_counter % enemy_manager.enemy_frequency==0:
        enemy_manager.create_enemy()
    if loop_counter % bullet_manager.bullet_frequency == 0:
        bullet_manager.create_bullet(player.xcor(), player.ycor())


    #sprawdzanie czy pocisk trafil

    # usuwanie pociskow ktore sa poza polem gry
    for bullet in bullet_list:
        if bullet.ycor() >= up_separator.ycor():
            bullet.color('red')
            bullet_list.remove(bullet)
    #usuwanie przeciwnikow ktorzy wyszli poza pole
    for enemy in enemies_list:
        if enemy.ycor()<=down_separator.ycor():
            enemy.color('red')
            enemies_list.remove(enemy)
    loop_counter += 1
window.exitonclick()
