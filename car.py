from turtle import Turtle
import random


class Car(Turtle):

    def __init__(self): #speed, x_axel random
        super().__init__()
        y_cordinates = list(range(-240, 280))
        random_y_list = y_cordinates[::40] 
        random_y = random.choice(random_y_list)
        random_speed_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.5, 0.01, 0.001]
        self.penup()
        self.setpos(300, random_y)
        self.speed(random.choice(random_speed_list))
        #print(random.choice(random_speed_list))
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2, outline=None)
        self.x_move = 10
        #self.y_move = 10 # Not needed I think. Perhaps for the frog to jump?
        self.move_speed = 0.1
    
    def move(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, self.ycor())


class Bus(Car):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=3, outline=None)
        
