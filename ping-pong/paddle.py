from turtle import Turtle
class Pad(Turtle):
    def __init__(self,xpos,ypos):
        super().__init__()
        self.create_pad(xpos,ypos)
    
    def create_pad(self,xpos,ypos):
        self.color("white")
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(xpos,ypos)
    
    def goup(self):
        self.penup()
        newy=self.ycor()+20
        self.goto(self.xcor(),newy)
        
    def godown(self):
        self.penup()
        newy=self.ycor()-20
        self.goto(self.xcor(),newy)
    