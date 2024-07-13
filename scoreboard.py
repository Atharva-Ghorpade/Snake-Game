from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("HighScore.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Arial', 18, 'normal'))

    def increase(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("HighScore.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
