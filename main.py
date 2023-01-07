import time
from turtle import Screen
from player import Player
from car_manager import CarManager
POSITION = [(100, 50), (100, 0), (100, -50), (100, -100), (100, -150)]
from scoreboard import Scoreboard
player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

car_manager = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    score = Scoreboard()
    for car in car_manager.all_car:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False
    if player.ycor() > 300:
        score.increase_score()
        player.go_to_starting()
        car_manager.level_up()
screen.exitonclick()