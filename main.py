# author : https://github.com/gumissek/game_space_invaders
import time
from turtle import Screen
from enemy import EnemyManager, EnemyBulletManager
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from layout import DownSeparator, UpSeparator
from scoreboard import Scoreboard
from player import Player, BulletManager
from barrier import BarrierManager
from gameover import GameOver

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
# barriers
barrier_manager = BarrierManager()
barrier_manager.create_barrier_grid()
barrier_list = barrier_manager.barrier_list

# player
player = Player()
window.onkeypress(player.player_move_left, 'Left')
window.onkeypress(player.player_move_right, 'Right')

# player shooting
bullet_manager = BulletManager()
player_bullets_list = bullet_manager.bullets_list

# enemies
enemy_manager = EnemyManager()
enemies_list = enemy_manager.enemies_list
enemy_manager.create_enemies_grid()

# enemies shooting
enemy_bullet_manager = EnemyBulletManager(enemies_list)
enemies_bullets_list = enemy_bullet_manager.enemy_bullet_list


loop_counter = 1
while lives_counter.lives > 0 and len(enemies_list) > 0:
    window.update()
    # poruszanie sie pociskow i przeciwnikow
    time.sleep(bullet_manager.bullets_speed)
    bullet_manager.bullets_move()
    enemy_bullet_manager.enemy_bullets_move()
    enemy_manager.enemies_move()
    if loop_counter % 170 == 0:
        enemy_manager.enemies_move_down()

    # czestotliwosc strzelania gracza i przeciwnikow
    if loop_counter % bullet_manager.bullet_frequency == 0:
        bullet_manager.create_bullet(player.xcor(), player.ycor())

    if loop_counter % enemy_bullet_manager.enemy_bullets_frequency == 0:
        enemy_bullet_manager.create_enemy_bullet()

    # sprawdzenie czy pociski uderzaja w bariere
    for barrier in barrier_list:
        for bullet_player in player_bullets_list:
            if bullet_player.distance(barrier) < 12:
                barrier.color('black')
                bullet_player.color('black')
                barrier_list.remove(barrier)
                player_bullets_list.remove(bullet_player)

        for bullet_enemy in enemies_bullets_list:
            if bullet_enemy.distance(barrier) < 12:
                barrier.color('black')
                bullet_enemy.color('black')
                barrier_list.remove(barrier)
                enemies_bullets_list.remove(bullet_enemy)

    # sprawdzenie czy przeciwnik uderzyl w gracza
    for enemy in enemies_list:
        if enemy.distance(player) < 20:
            enemy.color('blue')
            enemies_list.remove(enemy)
            lives_counter.lives = 0
            lives_counter.refresh_lives()

    # sprawdzanie czy pocisk przeciwnika trafil w gracza
    for bullet in enemies_bullets_list:
        if bullet.distance(player) < 20:
            bullet.color('black')
            enemies_bullets_list.remove(bullet)
            lives_counter.remove_live()

    if lives_counter.lives == 3:
        player.color('white')
    elif lives_counter.lives == 2:
        player.color('yellow')
    elif lives_counter.lives == 1:
        player.color('orange')

    # sprawdzanie czy pocisk gracza trafil w przeciwnika
    for enemy in enemies_list:
        for bullet in player_bullets_list:
            if bullet.distance(enemy) < 12:
                enemy.color('black')
                bullet.color('black')
                enemies_list.remove(enemy)
                player_bullets_list.remove(bullet)
                score_counter.add_point()

    # usuwanie pociskow przeciwnikow ktore wyszly poza pole gry
    for bullet in enemies_bullets_list:
        if bullet.ycor() <= down_separator.ycor():
            bullet.color('white')
            enemies_bullets_list.remove(bullet)

    # usuwanie pociskow gracza ktore sa poza polem gry
    for bullet in player_bullets_list:
        if bullet.ycor() >= up_separator.ycor():
            player_bullets_list.remove(bullet)

    # # usuwanie przeciwnikow ktorzy wyszli poza pole
    # for enemy in enemies_list:
    #     if enemy.ycor() <= down_separator.ycor():
    #         enemy.color('red')
    #         enemies_list.remove(enemy)
    loop_counter += 1

lives_counter.clear()
score_counter.game_over()
gameover=GameOver()


window.exitonclick()
