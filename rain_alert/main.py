import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("API_KEY")
account_sid=os.environ.get("ACCOUNT_SID")
auth_token=os.environ.get("AUTH_TOKEN")

own_endpoint="https://api.openweathermap.org/data/2.5/forecast"


weather_parameters={
    "lat":28.669155,
    "lon":77.453758,
    # "q": "Delhi, IN",
    "appid": api_key, 
    "exclude":"cloud"
}
response=requests.get(own_endpoint, params=weather_parameters)
response.raise_for_status()
weather_data=response.json()
weater_slice=weather_data["list"][:12 ]


will_rain=False

for hour_data in weater_slice:
    condition_code=int(hour_data["weather"][0]["id"])
    if condition_code<700:
        will_rain=True

if will_rain:
    client=Client(account_sid,auth_token)
    message=client.messages \
        .create(
        body="its going to rain today. Remember to bring an umbrella",
        from_="+12568587780",
        to="+918851062260"
        )
print(message.status)
    
    # print("take umbrella with you")

# print(weather_data["list"][0]["weather"][0]["id"])
# json_data = json.loads(response.text)
# print(json_data)