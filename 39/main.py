from pprint import pprint
from data_managment import DataManagement
from flights import FlightSearch
from notification_manager import NotificationManager
sheety = DataManagement()
flight = FlightSearch()
notification_manager = NotificationManager()
sheety_data = sheety.get_data()
if sheety_data[0]['iataCode'] == '':
    for data in sheety_data:
        data["iataCode"] = flight.get_destination_code(data["city"])

    sheety.data = sheety_data
    sheety.update_data()
flights_data = []
for dest in sheety_data:
    price = flight.search_flights(dest["iataCode"])
    if price["price"] < dest["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only {price['price']} to fly from Bogota to {dest['city']}, from {price['dateFrom']} to {price['dateTo']}."
        )
        print(
            f"Low price alert! Only {price['price']} to fly from Bogota to {dest['city']}, from {price['dateFrom']} to {price['dateTo']}.")
    else:
        print("no")
