import requests
from decouple import config

URL = "https://api.sheety.co/1e46fa5fee3bd710df01108f64e3de67/flightDeals/users"
HEADERS = {
    "Authorization": config("SHEETY_FLIHGTS_KEY")
}


class UserManager:
    def __init__(self) -> None:
        self.user_data = {}
        self.data = {}

    def get_data(self):
        response = requests.get(url=URL, headers=HEADERS)
        self.data = response.json()["users"]
        return self.data

    def new_user(self):
        body = {
            "user": self.user_data
        }
        response = requests.post(url=URL, json=body, headers=HEADERS)
        print("OK. You're in the club!")
