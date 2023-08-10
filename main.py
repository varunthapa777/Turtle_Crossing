import time
from turtle import Screen
from player import Player
from car_manager import CarManager, LANE
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move()

    # update level
    if player.ycor() > 290:
        car_manager.level_up()
        scoreboard.increment_level()
        player.reset_turtle()

    # Detect collision with cars

    for car in car_manager.cars:
        if car.distance(player) < 20 or player.distance(car) < 20:
            print(player.ycor(), car.ycor())
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()