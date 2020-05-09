import turtle
import random
import time

color_list = ["black", "orange", "purple", "blue", "red"]
shape_list = ["triangle", "circle", "square", "rectangle"]
legnth_list = [20, 75, 50, 24, 60]

winner = False
pen = turtle.Pen()
pen.shape("turtle")
pen.reset()
pen.speed(0)


def draw():
    global pen
    global shape_list
    global length_list
    global color_list
    pen.color(random.choice(color_list))
    shape = random.choice(shape_list)
    length = random.choice(length_list)
    if shape == "triangle":
        pen.begin_fill()
        pen.begin_fill()
        for _ in range(3):
            pen.forward(200)
            pen.left(120)
        pen.end_fill()
    if shape == "circle":
        pen.begin_fill()
        pen.circle(length)
        pen.end_fill()
    if shape == "square":
        pen.begin_fill()
        for _ in range(4):
            pen.forward(length)
            pen.left(90)
        pen.end_fill()
    if shape == "rectangel":
        if length < 50:
            pen.begin_fill()
            for _ in range(2):
                pen.forward(length)
                pen.left(90)
                pen.forward(75)
            pen.end_fill()
        else:
            pen.begin_fill()
            for _ in range(2):
                pen.forward(25)
                pen.left(90)
                pen.forward(length)
            pen.end_fill()


while winner == False:
    draw()
    time.sleep(3)
    pen.reset()