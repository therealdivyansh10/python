from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=-90
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    
    def create_snake(self):
        for i in POSITIONS:
            self.add_segment(i)
      
    def add_segment(self,i):
        segment=Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(i)
        self.segments.append(segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            newx=self.segments[i-1].xcor()
            newy=self.segments[i-1].ycor()
            self.segments[i].goto(newx,newy)
        self.head.forward(MOVE_DISTANCE )      

    def goup(self):
        if self.head.heading()!=DOWN:
            self.head.seth(UP)
    
    def godown(self):
        if self.head.heading()!=UP:
            self.head.seth(DOWN)
    
    def goleft(self):
        if self.head.heading()!=RIGHT:
            self.head.seth(LEFT)
        
    def goright(self):
        if self.head.heading()!=LEFT:
            self.head.seth(RIGHT)