from turtle import Turtle

HEIGHT = 600
WIDTH = 450
DISTANCE = 10

class Duck(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.setheading(90)
        self.speed('fastest')
        self.penup()
        self.goto(0, -250)


    def Up(self):
        self.forward(10)

    def Down(self):
        if(self.ycor() > -245):
            self.backward(10)

    def Left(self):
        if(self.xcor() > -200):
            newx = self.xcor() - 20
            newy = self.ycor()
            self.goto(newx, newy)

    def Right(self):
        if(self.xcor() < 200):
            newx = self.xcor() + 20
            newy = self.ycor()
            self.goto(newx, newy)


