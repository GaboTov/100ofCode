from twilio.rest import Client
import requests
from decouple import config
import os
MY_LAT = 36.834045  # Your latitude
MY_LONG = -2.463714  # Your longitude
api_key = config("KEYWEATHER")
OWM_endpoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}

response = requests.get(
    f"{OWM_endpoint}", params=parameters)
response.raise_for_status()
data = response.json()


account_sid = config("ACCONT_SID")
auth_token = config("TWILIOTOKEN", "NO TOKEN")
client = Client(account_sid, auth_token)
phone = config("PHONE", "NO PHONE")

message = client.messages.create(
    from_='+19062545713',
    body="it'll rain",
    to=phone
)

print(message.sid)
