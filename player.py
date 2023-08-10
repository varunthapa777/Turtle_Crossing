from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.setpos(0, -280)

    def move_up(self):
        self.forward(10)

    def reset_turtle(self):
        self.setpos(0, -280)