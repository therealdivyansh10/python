import colorgram
import turtle
import random

turtle.colormode(255)
tim=turtle.Turtle()
tim.pensize(30)
tim.turtlesize(5,5,5)
myscreen=turtle.Screen()
colors=colorgram.extract("projectimage.jpg",30)

tim.penup()
tim.setpos(-250,-250)
tim.pendown()
# color_list=[]
# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     tup=(r,g,b)
#     color_list.append(tup)
    
colorlist=[(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]


print(myscreen.canvheight)
print(myscreen.canvwidth)

for _ in range(0,6):
    for i in range(0,6):
        tim.color(random.choice(colorlist))
        tim.dot()
        tim.penup()
        tim.forward(100)
        tim.pendown()
    tim.seth(90)
    tim.penup()
    tim.forward(100)
    tim.seth(180)
    tim.forward(600)
    tim.seth(0)
    tim.pendown


myscreen.exitonclick()