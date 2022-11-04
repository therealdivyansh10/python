from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
    
    def display_score(self):
        self.penup()
        self.hideturtle()
        self.goto(230,270)
        self.write(f"LEVEL: {self.score}",align="center",font=("courier",20,"normal"))
        
    def update_score(self):
        self.clear()
        self.score+=1
        
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("courier",20,"normal"))