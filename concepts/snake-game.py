import time
from turtle import Screen,Turtle, pos, position
import turtle
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
positions=[(0,0),(20,0),(-20,0)]
segments=[]
for i in positions:
    screen.update()
    new_segment=Turtle("square")
    new_segment.penup()
    new_segment.goto(i)
    new_segment.color("white")
    segments.append(new_segment)
    
    
gameis_on=True
while gameis_on:
    screen.update()
    time.sleep(0.5)
    for i in segments:
        i.forward(10)
screen.exitonclick()