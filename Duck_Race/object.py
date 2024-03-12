from turtle import Turtle
import random


COLOR = ['red', 'white', 'green', 'yellow', 'orange']
TIME = [float(i * 0.1) for i in range(1, 8)]
POS = 195


class Object:
    def __init__(self):
        self.my_object = [[], [], [], [], [], [], []]

    def Create_Obj(self):
        for i in range(7):
            for j in range(6):
                self.obj = Turtle()
                self.obj.penup()
                self.obj.color('white')
                self.obj.shape('square')
                self.obj.setheading(180)
                self.obj.color(random.choice(COLOR))
                self.obj.goto((random.randint(-200, 200), 195 - (65*i)))
                self.my_object[i].append(self.obj)

    def Move(self):
        for i in self.my_object:
            for j in i:
                j.forward(random.choice(TIME))
                if j.xcor() < -250:
                    j.goto(220, j.ycor())
