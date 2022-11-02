from turtle import Turtle as T,Screen as S
from random import randint
import turtle
tim=T()
turtle.colormode(255)
tim.speed("fastest")
def get_colors():
    r=randint(0,256)
    g=randint(0,256)
    b=randint(0,256)
    tup=(r,g,b)
    return tup

def create_circles(value):
    for i in range(int(360/value)):
        tim.circle(100)
        tim.color(get_colors())
        tim.setheading(tim.heading()+value)

create_circles(5)
myscreen=S()
myscreen.exitonclick()