from turtle import Turtle
ALIGN="center"
FONT=("ariel",24,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.write(f"Score : {self.score}",align=ALIGN,font=FONT)
        
    def increase(self):
        self.score+=1
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.write(f"Score : {self.score}",align="center",font=("ariel",24,"normal"))