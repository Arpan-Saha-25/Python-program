'''----------------------------------------------------------------------------------------------------------------------------------------------'''
from turtle import *
import turtle
import datetime
turtle.title("Pythontpoint")
tur = turtle.Turtle()

today1 = datetime.datetime.now()
tur.hideturtle()
tur.penup()

tur.backward((tur.getscreen().window_width() / 2) - 10)
message = "Happy Programmer's day \nToday is " + today1.strftime("%A") + ', ' + today1.strftime("%d") \
           + ', ' + today1.strftime("%B") + ', ' + today1.strftime("%Y") 

tur.write(message,move=False, font=('Times New Roman',12,'bold'),align='left')
turtle.exitonclick()
