from turtle import Turtle,Screen
from food import Food
from scoreboard import Score
from snake import Snake
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

score.write_score()

screen.listen()
screen.onkey(snake.goup,"Up")
screen.onkey(snake.godown,"Down")
screen.onkey(snake.goleft,"Left")
screen.onkey(snake.goright,"Right")

gameison=True
while gameison:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food)<15:
        score.clear()
        score.points+=1
        snake.extend()
        score.write_score()
        food.create_food()
    
    for i in snake.segments:
        if(i==snake.head):
            pass
        else:
            if(snake.head.distance(i)<10):
                gameison=False
                score.gameisover()
            
    
    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor()< -280 or snake.head.ycor() >280:
        score.clear()
        score.gameisover()
        gameison=False
    
screen.exitonclick()