from turtle import Turtle, Screen
from random import Random

turtle=Turtle()
screen=Screen()
random=Random()
def random_colour():
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    return (r,g,b)
speed=0
pensize=2
screen.colormode(255)

while True:
    turtle.pensize(pensize)
    turtle.speed(speed)
    turtle.color(random_colour())
    orientation=[0,90,180,270]
    turtle.left(random.choice(orientation))
    turtle.fd(10)
    #speed+=1
    #pensize-=1
    if speed==11:
        speed=0
    if pensize==0:
        pensize=10

screen.exitonclick()
