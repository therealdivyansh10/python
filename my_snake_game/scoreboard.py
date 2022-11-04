from turtle import Turtle 
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points=0
        
    def write_score(self):
        self.color("white")
        self.hideturtle()   
        self.penup()
        self.goto(0,270)        
        self.write(f"score: {self.points}",align="center",font=("ariel",24,"normal"))
        self.penup()
    
    def gameisover(self):
        self.goto(0,0)
        self.write(f"score: game over ",align="center",font=("ariel",24,"normal"))
         