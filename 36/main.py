from decouple import config
import requests
import datetime
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
apikey = config("STOCK_API_KEY")
new_api_key = config("NEW_API_KEY")
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def get_data():
    response = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={apikey}")
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    today = datetime.datetime.now().date()
    yesterday = str(today - datetime.timedelta(days=1))
    before_yesterday = str(today - datetime.timedelta(days=2))

    return ({
        'yesterday': float(data[yesterday]["4. close"]),
        'before_yesterday': float(data[before_yesterday]["4. close"])
    })


def get_news():
    url = ('https://newsapi.org/v2/everything?'
           f'q={COMPANY_NAME}&'
           'from=2023-08-09&'
           'sortBy=popularity&'
           f'apiKey={new_api_key}')
    response = requests.get(url)

    return response.json()['articles'][:3]


data = get_data()
difference = abs(data["yesterday"]-data["before_yesterday"])
diff_percent = difference/data["yesterday"] * 100
if data["yesterday"] > data["before_yesterday"]:
    real_percent = f" 🔺{round(diff_percent)}%"
else:
    real_percent = f" 🔻{round(diff_percent*-1)}%"
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if diff_percent > 1:
    news = get_news()
# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
    messages = [
        f"TSLA: {real_percent}\n Headline: {article['title']}\n Brief: {article['description']}" for article in news]

    account_sid = config("ACCONT_SID")
    auth_token = config("TWILIOTOKEN", "NO TOKEN")
    client = Client(account_sid, auth_token)
    phone = config("PHONE", "NO PHONE")
    for txt in messages:
        message = client.messages.create(
            from_='+19062545713',
            body=txt,
            to=phone
        )
        print(txt)
else:
    print('none')


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
