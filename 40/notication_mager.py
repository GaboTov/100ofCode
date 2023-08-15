import smtplib
import requests
from decouple import config

email = config('EMAIL', 'no email')
password = config('PASS', 'no password')


class NotifirationManager:

    def send_emails(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=email,
                                msg=message)
        print('mail sended')
