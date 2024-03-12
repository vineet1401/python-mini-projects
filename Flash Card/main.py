from tkinter import *
import pandas as pd
import random
import time
from tkinter import messagebox

BACKGROUND = "#B1DDC6"

try:
    word_data = pd.read_csv("D:\CODING MATERIAL\Python Practise\INTERMEDIATE PYTHON PROGRAMMING\TKINTER PROGRAM\Flash Card\data\\french_words.csv")    
except:
    messagebox.showerror(title="FileNotFound", message="File not Found")
else:
    wordlist = word_data.to_dict(orient="records")
word={}

def next_card():
    global word
    global flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(wordlist)
    canvas.itemconfig(card_image, image=front_image)
    canvas.itemconfig(card_lang, text="French", fill="black")
    canvas.itemconfig(card_word, text=word["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global word
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(card_lang, text="English", fill="white" )
    canvas.itemconfig(card_word, text=word["English"], fill="white")

def isknown():
    global word
    wordlist.remove(word)
    print(len(wordlist))
    if(len(wordlist) == 0):
        messagebox.showinfo(message="You Have Learnt all the Words.")
    next_card()

window = Tk()
window.title("Flash Card")
window.config(background="#B1DDC6", padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0)
front_image = PhotoImage(file="D:\CODING MATERIAL\Python Practise\INTERMEDIATE PYTHON PROGRAMMING\TKINTER PROGRAM\Flash Card\images\card_front.png")
back_image = PhotoImage(file="D:\CODING MATERIAL\Python Practise\INTERMEDIATE PYTHON PROGRAMMING\TKINTER PROGRAM\Flash Card\images\card_back.png")
canvas.config(bg=BACKGROUND)
card_image = canvas.create_image(400, 263, image=front_image)
card_lang = canvas.create_text(400, 100, text="", font=("Ariel", 40, 'italic'), fill="black")
card_word = canvas.create_text(400, 300, text="", font=("Courier", 60, "bold"), fill="black")
canvas.grid(row = 0, column=0, columnspan = 2)

wrong_image = PhotoImage(file="D:\CODING MATERIAL\Python Practise\INTERMEDIATE PYTHON PROGRAMMING\TKINTER PROGRAM\Flash Card\images\wrong.png")
wrong_button = Button(image=wrong_image, width=100, height=100, command=next_card, borderwidth=0, justify=CENTER)
wrong_button.grid(row = 1, column=0)

right_image = PhotoImage(file="D:\CODING MATERIAL\Python Practise\INTERMEDIATE PYTHON PROGRAMMING\TKINTER PROGRAM\Flash Card\images\\right.png")
right_button = Button(image=right_image, width=100, height=100, command=isknown, borderwidth=0, justify=CENTER)
right_button.grid(row = 1, column=1)

next_card()

window.mainloop()