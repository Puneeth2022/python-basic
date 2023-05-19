import random
import turtle as t
from turtle import Turtle, Screen
direction=[0,90,180,270]
t.colormode(249)
def color1():
    r=random.randint(0,249)
    g=random.randint(0,249)
    b=random.randint(0,249)
    r=(r,g,b)
    return r


timmy=Turtle("turtle")
timmy.speed(0)
timmy.pensize(2)
def draw_spigot(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        timmy.color(color1())
        current=timmy.heading()
        timmy.setheading(current+size_of_gap)
        timmy.circle(100)

draw_spigot(12)



Screen=Screen()
Screen.exitonclick()