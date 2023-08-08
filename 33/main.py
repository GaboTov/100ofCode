import requests
from datetime import datetime
import smtplib
from decouple import config
import time
MY_LAT = 36.834045 # Your latitude
MY_LONG = -2.463714 # Your longitude



#Your position is within +5 or -5 degrees of the ISS position.
def send_mail():
    email = config('EMAIL','no email')
    password = config('PASS','no password')
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email, to_addrs=email,msg=f"Subject:ISS is up to you\n\nLook up!!!")
def check_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    return(time_now > sunset or time_now < sunrise)

#If the ISS is close to my current position
def status_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG +5:
        return True
    else:
        return False
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    if status_iss() and check_night():
        send_mail()
    else:
        print('no send email')
    time.sleep(60)
