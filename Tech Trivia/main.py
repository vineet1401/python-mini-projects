import requests
import tkinter
import random

math = "https://opentdb.com/api.php?amount=12&category=19&type=multiple"
vehicle = "https://opentdb.com/api.php?amount=12&category=28&type=multiple"
gk = "https://opentdb.com/api.php?amount=20&category=9&type=multiple"



# que = data['results'][2]['question']
# # print(data['results'][2]['correct_answer'])
# # print(data['results'][2]['incorrect_answers'])


def Maths():
    response = requests.get(url="https://opentdb.com/api.php?amount=12&category=19&type=multiple")
    response.raise_for_status()
    data = response.json()

    number = random.randint(0, 9)
    question = data["results"][number]['question']
    answer = data["results"][number]['correct_answer']
    option = data['results'][number]['incorrect_answers']
    option.append(answer)
    random.shuffle(option)
    
    main_que = {"Question":question, "Answer":answer, "Option":option}

    win_head.config(text="Magic Maths")
    win_que.config(text=main_que["Question"])
    win_opt_1.config(text=main_que["Option"][0])
    win_opt_2.config(text=main_que["Option"][1])
    win_opt_3.config(text=main_que["Option"][2])
    win_opt_4.config(text=main_que["Option"][3])

def General_Knowledge():
    response = requests.get(url="https://opentdb.com/api.php?amount=20&category=9&type=multiple")
    response.raise_for_status()
    data = response.json()

    number = random.randint(0, 9)
    question = data["results"][number]['question']
    answer = data["results"][number]['correct_answer']
    option = data['results'][number]['incorrect_answers']
    option.append(answer)
    random.shuffle(option)
    
    main_que = {"Question":question, "Answer":answer, "Option":option}

    win_head.config(text="General Knowledge")
    win_que.config(text=main_que["Question"])
    win_opt_1.config(text=main_que["Option"][0])
    win_opt_2.config(text=main_que["Option"][1])
    win_opt_3.config(text=main_que["Option"][2])
    win_opt_4.config(text=main_que["Option"][3])

def Vehicle():
    response = requests.get(url="https://opentdb.com/api.php?amount=12&category=28&type=multiple")
    response.raise_for_status()
    data = response.json()

    number = random.randint(0, 9)
    question = data["results"][number]['question']
    answer = data["results"][number]['correct_answer']
    option = data['results'][number]['incorrect_answers']
    option.append(answer)
    random.shuffle(option)
    
    main_que = {"Question":question, "Answer":answer, "Option":option}

    win_head.config(text="Vehicles")
    win_que.config(text=main_que["Question"])
    win_opt_1.config(text=main_que["Option"][0])
    win_opt_2.config(text=main_que["Option"][1])
    win_opt_3.config(text=main_que["Option"][2])
    win_opt_4.config(text=main_que["Option"][3])

def is_correct():
    ans = strVar.get()

def Next_que():
    pass



window = tkinter.Tk()
window.config(width=750, height=700)
window.title("Tech Trivia")
window.config(background="#B1DDC6", padx=20, pady=20)

heading = tkinter.Label(text="Tech Trivia", font=("Ariel", 40, 'italic'), fg="black", background="#B1DDC6")
heading.grid(row=0, column=0, columnspan=3)

math_button = tkinter.Button(text="Magic Maths", command=Maths, width=25)
gk_button = tkinter.Button(text="General Knowledge", command=General_Knowledge, width=25)
vehicle_button = tkinter.Button(text="Vehicles", command=Vehicle, width=25)
math_button.grid(row=1, column=0)
gk_button.grid(row=1, column=1)
vehicle_button.grid(row=1, column=2)

win_head = tkinter.Label(text=f"----------------------------", font=("Ariel", 25, 'italic'), fg="black", background="#B1DDC6")
win_head.grid(row=2, column=0, columnspan=3)


win_que = tkinter.Label(text="", font=("Ariel", 20, 'italic'), fg="black", background="#B1DDC6", wraplength=700)
win_que.grid(row=3, column=0, columnspan=3)

strVar = tkinter.IntVar()
win_opt_1 = tkinter.Radiobutton(text="",font=("Ariel", 12, 'italic'), variable=strVar, value=1, background="#B1DDC6", command=is_correct)
win_opt_1.grid(row=4, column=1, sticky="NW")
win_opt_2 = tkinter.Radiobutton(text="",font=("Ariel", 12, 'italic'), variable=strVar, value=2, background="#B1DDC6", command=is_correct)
win_opt_2.grid(row=5, column=1, sticky="NW")
win_opt_3 = tkinter.Radiobutton(text="",font=("Ariel", 12, 'italic'), variable=strVar, value=3, background="#B1DDC6", command=is_correct)
win_opt_3.grid(row=6, column=1, sticky="NW")
win_opt_4 = tkinter.Radiobutton(text="",font=("Ariel", 12, 'italic'), variable=strVar, value=4, background="#B1DDC6", command=is_correct)
win_opt_4.grid(row=7, column=1, sticky="NW")

next_button = tkinter.Button(text="Next", command=Next_que, width=15)
next_button.grid(row=8, column=2)







# canvas = tkinter.Canvas(width=600, height=500)
# que_heading = canvas.create_text(300, 120, text=f"", font=("Ariel", 20, 'italic'), fill="black")
# can_que = canvas.create_text(300, 120, text=f"", font=("Ariel", 20, 'italic'), fill="black")
# canvas.grid(row=3, column=0, columnspan=3)









window.mainloop()