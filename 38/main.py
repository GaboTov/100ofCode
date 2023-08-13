import requests
from decouple import config
from datetime import datetime

KEY = config("NUTRION_KEY")
ID = config("NUTRION_ID")
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT = 107
HEIGHT = 167
AGE = 27
headers = {
    "x-app-id": ID,
    "x-app-key": KEY,
    "x-remote-user-id": "0"
}
body = {
    "query":  input("Tell me which exercises yuo did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=END_POINT, json=body, headers=headers)
data = response.json()
result = data["exercises"]
today = datetime.now()
now_time = datetime.now().strftime("%X")
for exercice in result:
    sheet_input = {
        'workout': {
            "exercise": exercice["name"].title(),
            "duration": exercice["duration_min"],
            "calories":  exercice["nf_calories"],
            "date": today.strftime("%d/%m/%Y"),
            "time": now_time
        }

    }
SHEETY = config("SHEETY")
sheety_headers = {
    "Authorization": config("SHEETY_KEY")
}
save_workout = requests.post(
    url=SHEETY, json=sheet_input, headers=sheety_headers)
print(save_workout.text)
