import turtle
import random
import time

colors = ["black", "orange", "purple", "blue", "red"]
shapes = ["triangle", "circle", "square", "rectangle"]
lengths = [20, 75, 50, 24, 60]

winner = False
pen = turtle.Pen()
pen.shape("turtle")
pen.speed(0)


def draw():
    global pen, colors, shapes, lengths

    pen.color(random.choice(colors))
    shape = random.choice(shapes)
    length = random.choice(lengths)

    if shape == "triangle":
        pen.begin_fill()
        for _ in range(3):
            pen.forward(200)
            pen.left(120)
        pen.end_fill()

    elif shape == "circle":
        pen.begin_fill()
        pen.circle(length)
        pen.end_fill()

    elif shape == "square":
        pen.begin_fill()
        for _ in range(4):
            pen.forward(length)
            pen.left(90)
        pen.end_fill()

    elif shape == "rectangle":
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
