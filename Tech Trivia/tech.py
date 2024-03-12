from tkinter import *
import requests
import html

BACKGROUND = "#8D8DEE"

math = "https://opentdb.com/api.php?amount=1&category=19&type=boolean"
vehicle = "https://opentdb.com/api.php?amount=1&category=28&type=boolean"
gk = "https://opentdb.com/api.php?amount=1&category=9&type=boolean"

TOTAL_SCORE = 0
MY_SCORE = 0
    

def Generate():
    global QUE_LIST
    canvas.config(bg="white")
    response = requests.get(url="https://opentdb.com/api.php?amount=1&type=boolean")
    response.raise_for_status()
    data = response.json()
    question = html.unescape(data["results"][0]['question'])
    answer = data["results"][0]['correct_answer']
    QUE_LIST = [question, answer]
    return QUE_LIST

def Next():
    canvas.config(bg="white")
    score_text.config(text=f"{MY_SCORE} / {TOTAL_SCORE}")
    next_que = Generate()
    canvas.itemconfig(gui_question, text=f"{next_que[0]}")

def is_right():
    Feedback("True")

def is_wrong():
    Feedback("False")

def Feedback(val):
    global TOTAL_SCORE, MY_SCORE
    if(val == QUE_LIST[1]):
        canvas.config(bg="green")
        TOTAL_SCORE += 1
        MY_SCORE += 1
    else:
        TOTAL_SCORE += 1
        canvas.config(bg="red")
    window.after(1000, func=Next)





window = Tk()
window.title("TECH TRIVIA")
window.config(background=BACKGROUND)

heading = Label(
    text="Tech Trivia",
    font=("Sans", 25, "bold"),
    background=BACKGROUND
)
heading.grid(row=0, column=0, columnspan=3, pady=10)

score_text = Label(
    text=f"Score : 0/0",
    font=("Sans", 15, "bold"),
    background=BACKGROUND
)
score_text.grid(row=2, column=1, columnspan=2, pady=10)

canvas = Canvas(height=400, width=500, background="white")
gui_question = canvas.create_text(
        250,
        200,
        text="Question", 
        font=("Ariel", 15, "italic"),
        width=450
    )
canvas.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

wrong_image = PhotoImage(file="D:\CODING MATERIAL\Python Practise\INTERMEDIATE PYTHON PROGRAMMING\TKINTER PROGRAM\Flash Card\images\wrong.png")
wrong_button = Button(image=wrong_image, width=100, height=100, borderwidth=0, highlightthickness=0, command=is_wrong)
wrong_button.grid(row = 4, column=0, padx=10, pady=20)

right_image = PhotoImage(file="D:\CODING MATERIAL\Python Practise\INTERMEDIATE PYTHON PROGRAMMING\TKINTER PROGRAM\Flash Card\images\\right.png")
right_button = Button(image=right_image, width=100, height=100, borderwidth=0, highlightthickness=0, command=is_right)
right_button.grid(row = 4, column=2, padx=10, pady=20)


Next()

window.mainloop()