from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        with open('HighScore.txt', 'r+') as file:
            self.highscore = file.read()

        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 220)
        self.write(arg=f"High Score : {self.highscore} | Score : {self.score}", align='center',
                   font=('Arial', 25, 'normal'))

    def Update_Score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"High Score : {self.highscore} | Score : {self.score}", align='center',
                   font=('Arial', 25, 'normal'))

    def Game_Over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over \n Score : {self.score}", align='center', font=("Arial", 20, 'bold'))

        with open('HighScore.txt', 'w+') as file:
            if int(self.highscore) < int(self.score):
                file.write(str(self.score))
