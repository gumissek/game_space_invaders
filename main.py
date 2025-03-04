# zrobic layout ( wynik, zycia etc) ok
# zrobic gracza ok
# zrobic movement gracza prawo lewo ok
# zrobic strzelanie ( kulka) ok
# zrobic obiekty ( przeciwnikow ) ok
# zrobic movement przeciwkonkow zeby szly w dol ok
# zrobic dodawanie punktow za kazdego zabitego przeciwnika ok
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
enemy_manager = Enemy_manager()
enemies_list = enemy_manager.enemies_list
enemy_manager.create_enemies_grid()

loop_counter = 0
while lives_counter.lives > 0:
    window.update()
    # poruszanie sie pociskow i przeciwnikow
    time.sleep(bullet_manager.bullets_speed)
    bullet_manager.bullets_move()
    enemy_manager.enemies_move()

    #czestotliwosc strzelania
    if loop_counter % bullet_manager.bullet_frequency == 0:
        bullet_manager.create_bullet(player.xcor(), player.ycor())

    # # zmiana ilosci pociskow
    # if score_counter.score % 10 == 0:
    #     bullet_manager.bullet_increase_freq()



    # sprawdzanie czy pocisk trafil
    for enemy in enemies_list:
        for bullet in bullet_list:
            if bullet.distance(enemy) < 12:
                enemy.color('green')
                bullet.color('green')
                enemies_list.remove(enemy)
                bullet_list.remove(bullet)
                score_counter.add_point()
    # usuwanie pociskow ktore sa poza polem gry
    for bullet in bullet_list:
        if bullet.ycor() >= up_separator.ycor():
            bullet.color('red')
            bullet_list.remove(bullet)
    # usuwanie przeciwnikow ktorzy wyszli poza pole
    for enemy in enemies_list:
        if enemy.ycor() <= down_separator.ycor():
            enemy.color('red')
            enemies_list.remove(enemy)
    loop_counter += 1
window.exitonclick()
