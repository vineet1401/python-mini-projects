import smtplib
import datetime as dt
import pandas as pd
import random

now = dt.datetime.now()
month = now.month
day = now.day

GMAIL = "cyrax1401@gmail.com"
PASSWORD = "auvjtglfrqvdxodj."
 
birthday_csv = pd.read_csv("D:\CODING MATERIAL\Python Practise\INTERMEDIATE PYTHON PROGRAMMING\TKINTER PROGRAM\Automated Birthday Wisher\\birthdays.csv")
birthday_dict = birthday_csv.to_dict(orient="records")

for i in birthday_dict:
    letter_sample = ["D:\CODING MATERIAL\Python Practise\INTERMEDIATE PYTHON PROGRAMMING\TKINTER PROGRAM\Automated Birthday Wisher\letter_templates\letter_1.txt", 
            "D:\CODING MATERIAL\Python Practise\INTERMEDIATE PYTHON PROGRAMMING\TKINTER PROGRAM\Automated Birthday Wisher\letter_templates\letter_2.txt", 
            "D:\CODING MATERIAL\Python Practise\INTERMEDIATE PYTHON PROGRAMMING\TKINTER PROGRAM\Automated Birthday Wisher\letter_templates\letter_3.txt"
            ]
    letter = random.choice(letter_sample)

    if(month==i["month"] and day==i["day"]):
        with open(letter, "r") as file:
            birthday_msg = file.read()
            birthday_msg = birthday_msg.replace("[NAME]", i["name"])
        
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=GMAIL, password=PASSWORD)
        connect.sendmail(
            from_addr=GMAIL, 
            to_addrs=i["email"],
            msg=f"Subject:Happy Birthday\n\n{birthday_msg}"
            )

