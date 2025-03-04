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
from enemy import EnemyManager, EnemyBulletManager
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from layout import DownSeparator, UpSeparator
from scoreboard import Scoreboard
from player import Player, BulletManager

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
bullet_manager = BulletManager()
player_bullets_list = bullet_manager.bullets_list

# enemies
enemy_manager = EnemyManager()
enemies_list = enemy_manager.enemies_list
enemy_manager.create_enemies_grid()

enemy_bullet_manager = EnemyBulletManager(enemies_list)
enemies_bullets_list = enemy_bullet_manager.enemy_bullet_list

loop_counter = 0
while lives_counter.lives > 0 and len(enemies_list) > 0:
    window.update()
    # poruszanie sie pociskow i przeciwnikow
    time.sleep(bullet_manager.bullets_speed)
    bullet_manager.bullets_move()
    enemy_manager.enemies_move()
    enemy_bullet_manager.enemy_bullets_move()

    # czestotliwosc strzelania gracza
    if loop_counter % bullet_manager.bullet_frequency == 0:
        bullet_manager.create_bullet(player.xcor(), player.ycor())

    # # zmiana ilosci pociskow na sekunde
    # if score_counter.score % 10 == 0:
    #     bullet_manager.bullet_increase_freq()
    if loop_counter % enemy_bullet_manager.enemy_bullets_frequency == 0:
        enemy_bullet_manager.create_enemy_bullet()

    # sprawdzanie czy pocisk przeciwnika trafil w gracza
    for bullet in enemies_bullets_list:
        if bullet.distance(player) < 20:
            player.color('pink')
            bullet.color('pink')
            lives_counter.remove_live()

            enemies_bullets_list.remove(bullet)

    # sprawdzanie czy pocisk gracza trafil w przeciwnika
    for enemy in enemies_list:
        for bullet in player_bullets_list:
            if bullet.distance(enemy) < 12:
                enemy.color('green')
                bullet.color('green')
                enemies_list.remove(enemy)
                player_bullets_list.remove(bullet)
                score_counter.add_point()

    # usuwanie pociskow przeciwnikow ktore wyszly poza pole gry
    for bullet in enemies_bullets_list:
        if bullet.ycor() <= down_separator.ycor():
            bullet.color('red')
            enemies_bullets_list.remove(bullet)

    # usuwanie pociskow gracza ktore sa poza polem gry
    for bullet in player_bullets_list:
        if bullet.ycor() >= up_separator.ycor():
            bullet.color('red')
            player_bullets_list.remove(bullet)

    # # usuwanie przeciwnikow ktorzy wyszli poza pole
    # for enemy in enemies_list:
    #     if enemy.ycor() <= down_separator.ycor():
    #         enemy.color('red')
    #         enemies_list.remove(enemy)
    loop_counter += 1
window.exitonclick()
