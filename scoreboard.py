from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.score = 1
        self.hideturtle()
        self.goto(-250,265)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.pu()
        self.goto(0,0)
        self.write(f"GAME OVER", align="Center", font=FONT)

