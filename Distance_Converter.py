
from tkinter import *
def Convert():
    km = float(miles.get()) * 1.603
    label3 = Label(text=round(km, 2), font=("Arial", 25, 'bold'))
    label3.grid(row=2, column=1)

window = Tk()
window.title("Miles Converter")
window.config(bg='cyan' ,height=300, width=400, padx=50, pady=50)

label1 = Label(text="Miles : ", font=("Arial", 25, 'bold'))
label1.grid(row=0, column=0)
label2 = Label(text="Kilo Meter : ", font=("Arial", 25, 'bold'))
label2.grid(row=2, column=0)

button = Button(text="Calculate", command=Convert, border=1)
button.grid(row=1, column=1)

miles = StringVar()
input = Entry(textvariable=miles)
input.grid(row=0, column=1)

window.mainloop()

