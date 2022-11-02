import random
from turtle import Turtle,Screen, onclick, screensize
import turtle
screen=Screen()
screen.screensize(canvheight=400,canvwidth=500)
all_turtles=[]
raceison=False
userbet=screen.textinput(title="make your bet",prompt="which turtle is gonna win the race? Enter a color: ")
colors=["red","green","pink","black","blue","yellow"]
ypos=[-150,-100,-50,0,50,100]
for i in range(0,6):
    new_turtle=Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.setpos(x=-350,y=ypos[i])
    all_turtles.append(new_turtle)
    
if userbet:
    raceison=True

while raceison:
    for i in all_turtles:
        if i.xcor()>230:
            raceison=False
            winning_turtle=turtle.pencolor()
            if userbet==winning_turtle:
                print(f"You've won !!{winning_turtle} is the winner.")
            else:
                print(f"You've lost!!{winning_turtle} is the winner.")
            
        distance=random.randint(0,10)
        i.forward(distance)
    
    
screen.exitonclick()