import requests
from decouple import config
from pprint import pprint

kiwi_key = config("KIWI_KEY")
kiwi_endpoint = "https://api.tequila.kiwi.com/v2/search"
headers = {
    "apikey": kiwi_key
}


class FlightSearch:

    def get_destination_code(self, city):
        url = "https://api.tequila.kiwi.com/locations/query"
        params = {
            "term": city
        }
        response = requests.get(url=url, headers=headers, params=params)
        data = response.json()['locations'][0]['code']
        return data

    def search_flights(self, dest):
        params = {
            "fly_from": "BOG",
            "fly_to": dest,
            "date_from": "01/09/2023",
            "date_to": "10/01/2024",
            "sort": "price",
            "limit": "1",
            "return_from": "01/01/2024",
            "return_to": "01/10/2024",
            "nights_in_dst_from": 10,
            "nights_in_dst_to": 20
        }

        response = requests.get(
            url=kiwi_endpoint, params=params, headers=headers)
        try:
            data = response.json()["data"][0]
            mini_data = {
                "price": data["price"],
                "dateFrom": data['route'][0]['local_departure'],
                "dateTo": data['route'][1]['local_departure']
            }
            return mini_data
        except IndexError:
            print(f"No flights found for {dest}.")
            return {"price": 999999}
