from tkinter import mainloop
import turtle
screen = turtle.Screen()

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colors in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)
        
mainloop()      