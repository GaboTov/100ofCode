from decouple import config
import smtplib  
import datetime as dt
import random
email = config('EMAIL','no email')
password = config('PASS','no password')
now =dt.datetime.now()
day = now.weekday()
hour = now.hour

with open('32/quotes.txt','r') as file:
    list_of_quotes = file.readlines()
    print (list_of_quotes)
random_quote = random.choice(list_of_quotes)
# check day and hour to send email
if day == 0 and hour== 9:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email, to_addrs=email,msg=f"Subject:Monday don't sucks\n\n{random_quote} ")
    print('mail sended')

  


