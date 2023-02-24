from turtle import Turtle, Screen
import random
from car import Car
from froggy import Froggy
from scoreboard import Scoreboard
import turtle
import time



screen = Screen()
screen.bgpic('road.gif')
screen.setup(600, 600)
screen.title('Froggy Game')
screen.addshape('car_small.gif')
screen.addshape('car2_small.gif')
screen.addshape('car3_small.gif')
screen.addshape('bus_small.gif')
screen.addshape('bus2_small.gif')
screen.addshape('bus3_small.gif')
screen.tracer()

screen.listen()

scoreboard = Scoreboard()

#### car list moved to car.py:
# car = Car()
# car.shape(random.choice(car_pics))
# #car.resizemode('user')

car_manager = Car()

# bus_pics = ['bus_small.gif', 'bus2_small.gif' , 'bus3_small.gif']
# bus = Bus()
# bus.shape(random.choice(bus_pics))
# #bus.resizemode('user')

froggy = Froggy()

screen.onkey(fun = froggy.move, key = 'Up')


# print(f"car y : {car.ycor()}")
# print(f"bus y : {bus.ycor()}")
# print(f"froggy y : {froggy.ycor()}")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_vehicle()
    car_manager.move_cars()

    for car in car_manager.all_vehicles:
        if froggy.distance(car) < 35 and froggy.ycor() == car.ycor():
            scoreboard.game_over()
            game_on = False
    
    # if froggy.distance(bus) < 55 and froggy.ycor() == bus.ycor():
    #     scoreboard.game_over()
    #     game_on = False

    if froggy.ycor() >= 280:
        scoreboard.increase_score()
        froggy.restart_level()
        car_manager.level_up()
        

screen.mainloop()
screen.exitonclick()
