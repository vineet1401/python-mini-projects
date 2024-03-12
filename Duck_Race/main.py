import time
from turtle import Screen
from duck import Duck
from object import Object
from score import Scoreboard

screen = Screen()
screen.setup(height=540, width=450)
screen.bgcolor('black')
screen.bgpic('r2.png')
screen.tracer(0)

duck = Duck()
obstacle = Object()
score = Scoreboard()

# time.sleep(0)
screen.listen()
screen.onkeypress(fun=duck.Up, key='Up')
screen.onkeypress(fun=duck.Down, key='Down')
screen.onkeypress(fun=duck.Right, key='Right')
screen.onkeypress(fun=duck.Left, key='Left')

obstacle.Create_Obj()

is_on = True
while is_on:
    obstacle.Move()
    screen.update()

    if duck.ycor() > 260:
        score.Update_Score()
        time.sleep(0.2)
        duck.goto(0, -255)

    for i in obstacle.my_object:
        for j in i:
            if duck.distance(j) < 20:
                score.Game_Over()
                is_on = False

screen.exitonclick()
