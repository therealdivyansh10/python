from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()
    
    def create_food(self):
        self.color("red")
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.foodpos()
    
    def foodpos(self):
        self.penup()
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        self.goto(x,y)
    