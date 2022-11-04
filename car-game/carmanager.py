import random
from turtle import Turtle
STEP=5
COLORS=["red","orange","green","pink","black","blue"]
class Car:
    def __init__(self):
        self.all_cars=[]
        self.create_cars()
    
    def create_cars(self):
        car=Turtle()
        car.color(random.choice(COLORS))
        car.penup()
        car.shape("square")
        car.speed("fastest")
        car.shapesize(stretch_len=2,stretch_wid=1)
        car.goto(300,random.randint(-300,300))
        self.all_cars.append(car)
    
    def move(self):
        for i in self.all_cars:
            i.backward(STEP)
        