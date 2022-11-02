import random
from food import Food
import time
from turtle import Screen
from scoreboard import ScoreBoard
# from scoreboard import ScoreBoard
from snake import Snake
from snake import COORDINATES
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
score=ScoreBoard()
snake=Snake()
newfood=Food()
newfood.positions()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
gameison=True
while gameison:
    # score=ScoreBoard()
    screen.update()
    time.sleep(0.1)
    snake.move()
    if(snake.head.distance(newfood))<20:
        score.increase()
        newfood.positions()
    # if snake.head.xcor()>295 or snake.head.xcor< -295:
        
screen.exitonclick()