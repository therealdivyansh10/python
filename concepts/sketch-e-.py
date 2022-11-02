from turtle import Turtle,Screen, forward, seth
tim=Turtle()
def ahead():
    tim.forward(100)

def back():
    tim.seth(180)
    
def right():
    newdirection=tim.heading()-10
    tim.seth(newdirection)
    
def left():
    newdirection=tim.heading()+10
    tim.seth(newdirection)

screen=Screen()
screen.listen()
screen.onkey(ahead,"w")
screen.onkey(back,"s")
screen.onkey(left,"a")
screen.onkey(right,"d")

screen.exitonclick()
