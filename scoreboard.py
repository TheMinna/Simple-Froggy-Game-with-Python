from turtle import Turtle

FONT = ('Courier', 14, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('#CC0000')
        self.hideturtle()
        self.penup()
        self.setpos(-250, 270)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align='center', font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", move=False, align='left', font=FONT)
