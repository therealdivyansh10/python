from turtle import Turtle,Screen
import time
from player import Player
from carmanager import Car
import random
from score import Score

screen=Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.tracer(0)
player=Player()
score=Score()

screen.listen()
screen.onkey(player.goup,"Up")

car=Car()
gameison=True
while gameison:
    chance=random.randint(1,6)
    if chance==1:
        car.create_cars()
    screen.update()
    time.sleep(0.1)
    car.move()
    score.display_score()
    
    if player.ycor()==300:
        score.update_score()
        player.resetPos()
        
    for i in car.all_cars:
        if player.distance(i)<25:
            gameison=False
            score.gameover()

screen.exitonclick()