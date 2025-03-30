
import random
import turtle
from turtle import Turtle, Screen

list_0f_colour = [(245, 246, 250), (252, 251, 247), (188, 74, 20), (56, 34, 13), (149, 26, 9), (237, 226, 77), (24, 31, 60), (113, 167, 210), (45, 85, 143), (227, 243, 238), (217, 154, 82), (34, 50, 124), (191, 144, 25), (26, 51, 29), (201, 93, 126), (242, 214, 6), (250, 244, 249), (119, 35, 51), (120, 187, 149), (55, 129, 74), (70, 82, 17), (36, 84, 40), (142, 51, 58), (74, 128, 200), (205, 86, 62), (82, 31, 44), (104, 180, 70), (148, 204, 223), (197, 120, 162), (23, 77, 100), (160, 217, 197), (157, 194, 229), (222, 179, 168), (218, 175, 190), (71, 145, 172)]
tim = Turtle()
tim.speed("fastest")

rows = 20
num_of_dotes = 30
spacing = 35
tim.penup()
tim.goto(-500,-400)
tim.pendown()
tim.penup()
def next_row():
    tim.backward(num_of_dotes * spacing)
    tim.left(90)
    tim.forward(spacing)
    tim.right(90)

def dotes():
    turtle.colormode(255)
    tim.dot(18, random.choice(list_0f_colour))
    tim.forward(spacing)

for row in range(rows):
    for dot in range(num_of_dotes):
        dotes()
    next_row()
tim.hideturtle()


screen = Screen()
screen.exitonclick()
