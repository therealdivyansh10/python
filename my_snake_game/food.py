from turtle import Turtle
import random
from snake import Snake
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self=Turtle(shape="circle")
        self.penup()
        self.speed("fastest")
        self.color("red")
        self.shapesize(0.5)
        self.penup()
        self.pos()
        
    def positions(self):
        xpos=random.randint(-290,290)
        ypos=random.randint(-290,290)
        self.goto(xpos,ypos)
        
            