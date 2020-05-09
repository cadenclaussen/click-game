import turtle
import random
import time
color_list = ["black","orange","purple","blue","red"]
shape_list = ["triangle","circle","square","rectangle"]
legnth_list = [20,75,50,24,60]
winner = False
pen = turtle.Pen()
pen.shape("turtle")
pen.reset()
pen.speed(0);
def draw():
     pen.color(random.choice(color_list))
     color = random.choice(color_list)
     shape = random.choice(shape_list)
     length = random.randint(lenght_list)
     rectangel = random.randint(1, 2)
     if shape == "triangle":
         pen.begin_fill(color)
         for _ in range(3):
             pen.forward(200)
             pen.left(120)
         pen.end_fill(color)
     if shape == "circle":
         pen.begin_fill(color)
         pen.circle(length)
         pen.end_fill(color)
     if shape == "square":
         pen.begin_fill(color)
         for _ in range(4):
             pen.forward(length)
             pen.left(90)
         pen.end_fill(color)   
     if shape == "rectangel":
         if length < 50:
             pen.begin_fill(color)
             for _ in range(2):
                 pen.forward(length)
                 pen.left(90)
                 pen.forward(75)
             pen.end_fill(color)
         else:
             pen.begin_fill(color)
             for _ in range(2):
                 pen.forward(25)
                 pen.left(90)
                 pen.forward(length)
             pen.end_fill(color)
        
        
    


