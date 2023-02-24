from turtle import Turtle
import random
import time

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

car_pics = ['car_small.gif', 'car2_small.gif', 'car3_small.gif',
            'bus_small.gif', 'bus2_small.gif', 'bus3_small.gif']
# bus_pics = ['bus_small.gif', 'bus2_small.gif' , 'bus3_small.gif']


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.all_vehicles = []
        self.create_vehicle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def move_cars(self):
        for car in self.all_vehicles:
            car.backward(self.car_speed)
            # new_x = self.xcor() - self.xcor_car_move
            # self.goto(new_x, self.ycor())

    def create_vehicle(self):
        random_chance = (random.randint(1, 6))
        if random_chance == 1:
            new_vehicle = Turtle()
            new_vehicle.hideturtle()
            new_vehicle.penup()
            new_vehicle.shape(random.choice(car_pics))
            y_cordinates = list(range(-240, 240))
            # Deleted one middle step, a random_y_list
            random_y = random.choice(y_cordinates[::40])
            new_vehicle.setpos(320, random_y)
            random_speed_list = [10, 9, 8, 7, 6,
                                 5, 4, 3, 2, 1, 0.5, 0.01, 0.001]
            new_vehicle.speed(random.choice(random_speed_list))
            new_vehicle.shapesize(stretch_wid=1, stretch_len=2, outline=None)
            new_vehicle.showturtle()
            self.all_vehicles.append(new_vehicle)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT


# class Bus(Car):
#     def __init__(self):
#         super().__init__()
#         self.shapesize(stretch_wid=1, stretch_len=3, outline=None)
