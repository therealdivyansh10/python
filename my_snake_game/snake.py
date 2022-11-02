from tkinter import RIGHT
from turtle import Turtle,Screen
import time
COORDINATES=[(-20,0),(0,0),(20,0)]
MOVE_DISTANCE=20
LEFT=180
RIGHT=0
UP=90
DOWN=-90
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[2]
    
    def create_snake(self):
        for i in COORDINATES:
            new_segment=Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(i)
            self.segments.append(new_segment)


    def move(self):
        for i in range(0,len(self.segments)-1,1):
            newx=self.segments[i+1].xcor()
            newy=self.segments[i+1].ycor()
            self.segments[i].goto(newx,newy)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.seth(UP)
        
    def down(self):
        if self.head.heading()!=UP:
            self.head.seth(DOWN)
    
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.seth(LEFT)
        
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.seth(RIGHT)