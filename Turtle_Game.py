import turtle
import random


is_on = False
screen = turtle.Screen()
screen.setup(height=500, width=800)


turtle_in_race = []
turtle_colours = ['red', 'black', 'blue',
                  'green', 'yellow', 'purple', 'orange']
turtle_position = [-180, -120, -60, 0, 60, 120, 180]


def Start_End_Line():
    t = turtle.Turtle()
    t.speed('fastest')
    t.hideturtle()
    t.penup()
    t.goto(-360, 230)
    t.setheading(-90)
    t.pendown()
    t.forward(460)
    t.penup()
    t.goto(360, 230)
    t.setheading(-90)
    t.pendown()
    t.forward(460)


Start_End_Line()


for i in range(7):
    new_turtle_for_race = turtle.Turtle(shape='turtle')
    new_turtle_for_race.speed('fast')
    new_turtle_for_race.penup()
    new_turtle_for_race.color(turtle_colours[i])
    new_turtle_for_race.goto(-380, turtle_position[i])
    turtle_in_race.append(new_turtle_for_race)

user_bet = screen.textinput(
    title="Set Your Bidding", prompt="Enter the colour which will win. ")
if user_bet:
    is_on = True

while is_on:
    for turt in turtle_in_race:
        if (turt.xcor() > 350):
            is_on = False
            winning_colour = turt.pencolor()
            if (user_bet == winning_colour):
                print(
                    f"You have won! {winning_colour} won the round.")
            else:
                print(
                    f"You have lost! {winning_colour} won the round.")
        random_speed = random.randint(0, 10)
        turt.forward(random_speed)


screen.exitonclick()
