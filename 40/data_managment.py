import requests
from decouple import config
from pprint import pprint

URL = config("SHEETY_FLIHGTS")
HEADERS = {
    "Authorization": config("SHEETY_FLIHGTS_KEY")
}


class DataManagement:
    def __init__(self) -> None:
        self.data = {}

    def get_data(self):
        response = requests.get(url=URL, headers=HEADERS)
        self.data = response.json()["prices"]
        return self.data

    def update_data(self):
        for data in self.data:
            url = f"{URL}/{data['id']}"
            body = {"price": data}
            response = requests.put(url=url, headers=HEADERS, json=body)
            print(response.text)
