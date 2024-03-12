import requests
import datetime as dt

GENDER = "Male"
WEIGHT = 68
HEIGHT = 170
AGE = 20
NUTRITION_ID = "e42e4304"
NUTRITION_KEY = "165a71e40c6fc005f7959fad58be6077"


nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/a1717b6cfbc3c950b6cb2af8946d0f9a/myWorkout/workouts"


exercise_text = input("What Exercise you did today? ").title()
k

date = dt.datetime.now()
today_date = f"{date.strftime('%d')}/{date.strftime('%m')}/{date.strftime('%Y')}"
today_time = f"{date.strftime('%H')}/{date.strftime('%M')}/{date.strftime('%S')}"

headers = {
    "x-app-id":NUTRITION_ID,
    "x-app-key":NUTRITION_KEY
}
parameters = {
    "query":exercise_text,
    "gender" : GENDER,
    "weight_kg" : WEIGHT,
    "height_cm" : HEIGHT,
    "age" : AGE
}


response = requests.post(url=nutrition_endpoint, json=parameters, headers=headers)
data = response.json()


for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)