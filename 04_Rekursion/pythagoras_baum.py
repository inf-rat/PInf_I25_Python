import math
from turtle import *
speed(10)
setup(800, 800)
colors = ("#2274a5", "#f75c03", "#f1c40f", "#d90368", "#00cc66")

def square(width, col):
    color(col)
    fillcolor(col)
    begin_fill()
    for i in range(4):
        forward(width)
        left(90)
    end_fill()

def tree(width, angle, steps):
    square(width, colors[steps % len(colors)])
    if steps > 1:
        penup()
        left(90)
        forward(width)
        right(90 - angle)
        pendown()
        tree(width * math.cos(math.radians(angle)), angle, steps - 1)
        right(90)
        tree(width * math.sin(math.radians(angle)), angle, steps - 1)
        penup()
        right(angle)
        forward(width)
        left(90)
        pendown()
    else:
        penup()
        forward(width)
        pendown()

penup()
goto(-70, -200)
pendown()
tree(100, 55, 5)
mainloop()