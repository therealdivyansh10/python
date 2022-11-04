from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        
    def create_ball(self):
        self.shape("circle")
        self.color("red")
        self.x_move=10
        self.y_move=10
    
    def move(self):
        self.penup()
        newx=self.xcor()+self.x_move
        newy=self.ycor()+self.y_move
        self.goto(newx,newy)
        
        
    def bounce(self):
        self.y_move*=-1
    
    def bounce_back(self):
        self.y_move*=-1
        self.x_move*=-1
        