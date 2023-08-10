from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.setpos(-290, 250)
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def increment_level(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over", False, align="center", font=("courier", 64, "bold"))
