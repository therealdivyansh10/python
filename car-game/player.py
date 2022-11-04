from turtle import Turtle
INITIAL_POS=(0,-300)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()
    
    def create_player(self):
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(INITIAL_POS)
    
    def goup(self):
        ypos=self.ycor()+10
        self.goto(self.xcor(),ypos)
    
    def resetPos(self):
        self.goto(INITIAL_POS)