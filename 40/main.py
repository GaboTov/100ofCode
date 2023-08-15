from user_manager import UserManager

from flights import FlightSearch
from pprint import pprint
from data_managment import DataManagement
from flights import FlightSearch
from notication_mager import NotifirationManager
user = UserManager()
print("Welcome to flight club \n We find the best flight deals and email you. \n")
flight = FlightSearch()
notification_manager = NotifirationManager()


def valid_email():
    email = input("Whats your email \n")
    check_email = input("Type your email again \n")
    if email == check_email:
        return email
    else:
        print("email incorrect\n")
        valid_email()


user.user_data = {
    "firstName": "test",  # input("what is your first name?\n"),
    "lastName": "test",  # input("what is your last name?\n"),
    "email": "test"  # valid_email(),
}
user.new_user()

sheety = DataManagement()
flight = FlightSearch()

sheety_data = sheety.get_data()
if sheety_data[0]['iataCode'] == '':
    for data in sheety_data:
        data["iataCode"] = flight.get_destination_code(data["city"])

    sheety.data = sheety_data
    sheety.update_data()
for dest in sheety_data:
    price = flight.search_flights(dest["iataCode"])
    if price["price"] < dest["lowestPrice"]:
        notification_manager.send_emails(
            message=f"Low price alert! Only {price['price']} to fly from Bogota to {dest['city']}, from {price['dateFrom']} to {price['dateTo']}."
        )
        print(
            f"Low price alert! Only {price['price']} to fly from Bogota to {dest['city']}, from {price['dateFrom']} to {price['dateTo']}.")
    else:
        print("no", dest["city"])
