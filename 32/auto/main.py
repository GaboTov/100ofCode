##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
from decouple import config
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pd.DataFrame(pd.read_csv("32/auto/birthdays.csv"))
data_dict = data.to_dict(orient='records')
now = dt.datetime.now()
email = config('EMAIL','no email')
password = config('PASS','no password')
month = now.month
day = now.day
for person in data_dict:
    if month == person['month'] and day == person['day']:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        path_file = f"32/auto/letter_templates/letter_{random.randint(1,3)}.txt"
        with open(path_file, 'r') as letter:
            content = letter.read()
            modify_content = content.replace("[NAME]", f"{person['name']}")
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=email,password=password)
            connection.sendmail(from_addr=email, to_addrs=email,msg=f"Subject:Happy Birthday {person['name']}!!!!\n\n{modify_content} ")
    






