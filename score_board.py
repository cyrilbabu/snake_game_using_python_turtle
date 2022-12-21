from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = self.read_file()

        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(arg=f"score: {self.score} , high score: {self.high_score}", move=False, align="center", font=("Arial", 24, "normal"))

    def read_file(self):
        file = open("high_score.txt", mode="r")
        self.high_score = int(file.read())
        file.close()
        return self.high_score

    def increse_score(self):
        self.score += 1
        self.update_score_board()

    def update_high_score(self):
        if self.score >= self.high_score:
            file = open("high_score.txt", mode="w")
            file.write(f"{self.score}")
            file.close()

        self.score = 0
        self.high_score = self.read_file()
        self.update_score_board()
