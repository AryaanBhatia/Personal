from turtle import *
from colorsys import hsv_to_rgb

bgcolor("black")
speed(0)

pensize(8)
pencolor("white")

pendown()

for i in range(255):
    for j in range(4):
        color(hsv_to_rgb(i/25, j/4, 0.8))
        right(90)
        circle(200-j*4, 90)
        left(90)
        circle(200-j*4, 90)
        right(180)
        circle(50, 24)



hideturtle()
done()