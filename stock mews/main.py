import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY="QQVDU0LXEH9YQOBD"
NEWS_API_KEY="7ba2f0fd57c14f82846797040aba061d"

account_sid=os.environ.get("ACCOUNT_SID")
auth_token=os.environ.get("AUTH_TOKEN")

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price. 

stock_parameter={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY,
}



rresponse=requests.get(STOCK_ENDPOINT,params=stock_parameter)
data=(rresponse.json()["Time Series (Daily)"])
data_list=[value for (key,value) in data.items()]
yesterdays_data=data_list[0]
yesterday_closing_price=yesterdays_data["4. close"]
print(yesterday_closing_price)
#Get the day before yesterday's closing stock price
day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference=abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)
#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_percent=(difference/float(yesterday_closing_price))*100
up_down=None
if difference>0:
    print(difference)
#     up_down="⬆️"
# else:
#     up_down="⬇️"



    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if difference_percent>4:
    news_parameter={
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME ,
    }
    news_response=requests.get(NEWS_ENDPOINT,params=news_parameter)
    articles=news_response.json()["articles"]
    print(type(articles))
    print(articles)

    
#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles= articles[:3]
    print(three_articles)

    #Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#Create a new list of the first 3 article's headline and description using list comprehension.
    # for arlicle in three_articles:
    #     print()
    formatted_articles=[f"Headline:{arlicle['title']}.\nBreif:{arlicle[ 'description']}" for arlicle in three_articles]
    
#Send each article as a separate message via Twilio. 
    client=Client(account_sid,auth_token)

    for article in formatted_articles:
        message=client.messages.create(
            body=article,
            from_="+12568587780",
            to="+918851062260"
        )
#Optional Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

