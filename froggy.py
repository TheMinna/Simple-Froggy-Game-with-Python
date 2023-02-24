from turtle import Turtle


MOVE_DISTANCE = 40


class Froggy(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1, outline=None)
        self.restart_level()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def restart_level(self):
        self.hideturtle()
        self.setpos(0, -280)
        self.setheading(90)
        self.showturtle()
