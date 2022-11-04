import time
from paddle import Pad
from turtle import Turtle,Screen
from ball import Ball

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")

ball=Ball()

rpad=Pad(380,0)
lpad=Pad(-380,0)


screen.listen()
screen.onkey(rpad.goup,"Up")
screen.onkey(rpad.godown,"Down")

screen.onkey(lpad.goup,"w")
screen.onkey(lpad.godown,"s")



gameison=True
while gameison:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor()>=290 or ball.ycor()< -290:
        ball.bounce()
    
    if ball.distance(rpad)<50 and ball.xcor()>350 or ball.distance(rpad)<50 or ball.xcor() < -350 :
        print("made contact")
        ball.bounce_back()
    
screen.exitonclick()