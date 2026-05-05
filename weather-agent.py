import requests
import os
from dotenv import load_dotenv
from datetime import datetime


def generate_report(weather_data):
    report = f"Weather Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"•Temperature: {weather_data['temperature']}°C\n"
    report += f"•Feels like: {weather_data['wind_chill']}°C\n"
    report += f"•Humidity: {weather_data['humidity']}%\n"
    report += f"•Wind speed: {weather_data['wind_speed']} m/s\n"
    report += f"•Cloudiness: {weather_data['cloudiness']}%\n"
    report += f"•Description: {weather_data['description']}\n"
    report += "\nAnalysis:\n"
    report += f"•Clothing: {temperature_analysis(weather_data['temperature'])}\n"
    report += f"•Wind: {wind_analysis(weather_data['wind_speed'])}\n"
    report += f"•Cloud cover: {cloud_analysis(weather_data['cloudiness'])}\n"
    report += f"•Rain: {rain_analysis(weather_data['description'])}\n"
    return report

def temperature_to_celsius(kelvin):
    return round(kelvin - 273.15, 1)

def temperature_analysis(temperature):
    if temperature < 18:
        return "Cold conditions — layer up before heading out."
    elif 18 <= temperature < 28:
        return "Comfortable temperature — a light top should do."
    else:
        return "Hot conditions — opt for light, breathable clothing."

def wind_analysis(wind_speed):
    if wind_speed < 2:
        return "Virtually no wind — ideal conditions outdoors."
    elif 2 <= wind_speed <= 8:
        return "Light to moderate breeze — keep an eye on loose objects."
    else:
        return "Strong winds — secure loose items and skip the umbrella."

def cloud_analysis(cloudiness):
    if cloudiness < 25:
        return "Mostly clear skies — don't forget your sunscreen."
    elif 25 <= cloudiness < 75:
        return "Partly cloudy — a mix of sun and clouds expected."
    else:
        return "Heavily overcast — sunscreen not required."

def rain_analysis(description):
    if "rain" in description or "drizzle" in description or "thunderstorm" in description:
        return "Precipitation likely — bring an umbrella."
    else:
        return "Dry conditions expected — no umbrella needed."
    

def extract_weather_data(data): 
    weather_data = {
        "temperature": temperature_to_celsius(data["main"]["temp"]),
        "wind_chill": temperature_to_celsius(data["main"]["feels_like"]),
        "humidity": round(data["main"]["humidity"], 1),
        "wind_speed": round(data["wind"]["speed"], 1),
        "cloudiness": round(data["clouds"]["all"], 1),
        "description": data["weather"][0]["description"]
    }
    return weather_data

def main():
    # Load environment variables from .env file
    load_dotenv()

    api_key = os.getenv('API_KEY')
    lat = -8.838333
    lon = 13.234444

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    response = requests.get(url)

    if (response.status_code == 200):
        data = response.json()
        weather_data = extract_weather_data(data)
        report = generate_report(weather_data)
        filename = f"weather_report_{datetime.now().strftime('%Y-%m-%d')}.txt"
        with open(filename, "w") as file:
            file.write(report)
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    main()