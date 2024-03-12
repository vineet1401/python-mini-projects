from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
MODE = 0
RESET = NONE
# ---------------------------- TIMER RESET ------------------------------- # 
def Reset_Count():
    global REPS, MODE, RESET
    REPS = 0
    MODE = 0
    window.after_cancel(RESET)
    background.itemconfig(timer_text, text="00:00")
    timer.config(text="TIMER")
    tick.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def Start_Count():
    global REPS, MODE
    REPS += 1
    if REPS % 8 == 0:
        Count_Down(LONG_BREAK_MIN * 60)
        timer.config(text='LONG BREAK', font=(FONT_NAME, 25, 'bold'))
        MODE = 0
        tick.config(text="")
    elif(REPS % 2 == 1):
        Count_Down(WORK_MIN * 60)
        timer.config(text='DO YOUR WORK', font=(FONT_NAME, 25, 'bold'))
        t = "✔" * MODE
        tick.config(text=t)
    else:
        Count_Down(SHORT_BREAK_MIN * 60)
        timer.config(text='SHORT BREAK', font=(FONT_NAME, 25, 'bold'))
        MODE += 1
        t = "✔" * MODE
        tick.config(text=t)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def Count_Down(count):
    global RESET
    min = count // 60
    sec = count % 60
    if(sec < 10):
        sec = f"0{sec}"
    background.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        RESET = window.after(1000, Count_Down, count-1)
    else:
        Start_Count()

# ---------------------------- UI SETUP ------------------------------- #
window =  Tk()
window.title("POMODORA".center(100))
window.config(height=200, width=400, bg=YELLOW, padx=70, pady=70)

background = Canvas(height=250, width=210, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
background.create_image(105, 110, image=tomato)
timer_text = background.create_text(105, 130, text="00:00", font=(FONT_NAME, 30, 'bold'), fill='white')
background.grid(row=1, column=1)


timer = Label(text="TIMER", bg=YELLOW, font=(FONT_NAME, 50, 'bold'), fg='black')
timer.grid(row=0, column=1)
tick = Label(text=" ✔", bg=YELLOW, font=(FONT_NAME, 20, 'bold'), fg=GREEN)
tick.grid(row=2, column=1)

start = Button(text="Start", background='orange', padx=10, pady=10, command=Start_Count)
reset = Button(text="Reset", background='orange', padx=10, pady=10, command=Reset_Count)
start.grid(row=2, column=0)
reset.grid(row=2, column=2)

window.mainloop()