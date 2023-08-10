import random
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANE = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
NUM_OF_CARS = 20


def change_color():
    rand_color = random.choice(COLORS)

    return rand_color


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car(NUM_OF_CARS)

    def create_car(self, n_cars):
        for _ in range(n_cars):
            new_car = Turtle()
            new_car.shape("square")
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.color(change_color())
            new_car.penup()
            rand_x = random.randint(-300, 300)
            rand_y = random.choice(LANE)
            new_car.setpos(rand_x, rand_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.color(change_color())
                x_cor = car.xcor() * -1
                y_cor = random.choice(LANE)
                car.setpos(x_cor, y_cor)

            new_x = car.xcor() - self.car_speed
            car.setx(new_x)

    def level_up(self):
        for car in self.cars:
            car.hideturtle()

        self.cars.clear()
        n_car = NUM_OF_CARS - 1
        self.create_car(n_car)
        self.car_speed += MOVE_INCREMENT


