import requests
import os
from dotenv import load_dotenv


def extract_weather_data(data): 
    weather_data = {
        "temperature": round(data["main"]["temp"] - 273.15, 1),  # Convert from Kelvin to Celsius
        "wind_chill": round(data["main"]["feels_like"] - 273.15, 1),  # Convert from Kelvin to Celsius
        "humidity": round(data["main"]["humidity"], 1),
        "wind_speed": round(data["wind"]["speed"], 1),
        "cloudiness": round(data["clouds"]["all"], 1),
        "description": data["weather"][0]["description"]
    }
    return weather_data

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv('API_KEY')
lat = -8.923685505546363
lon = 13.183318976842212

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url)

if (response.status_code == 200):
    data = response.json()
    weather_data = extract_weather_data(data)
    print(weather_data)
else:
    print("Error:", response.status_code)