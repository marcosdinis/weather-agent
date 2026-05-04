import requests
import os
from dotenv import load_dotenv


def temperature_to_celsius(kelvin):
    return round(kelvin - 273.15, 1)

def temperature_analysis(temperature):
    if temperature < 18:
        return "Vista um agasalho, pois a temperatura está baixa."
    elif 18 <= temperature < 28:
        return "Vista uma blusa, pois a temperatura está amena."
    else:
        return "Vista roupas leves, pois a temperatura está alta."
    
def wind_analysis(wind_speed):
    if wind_speed < 2:
        return "Vento calmo, sem impacto nas actividades ao ar livre."
    elif 2 <= wind_speed < 5:
        return "Vento moderado, segure objectos leves ao ar livre."
    else:
        return "Vento forte, evite guarda-chuvas e proteja objectos leves."

def claude_analysis(cloudiness):
    if cloudiness < 25:
        return "Céu limpo, use protecção solar."
    elif 25 <= cloudiness < 75:
        return "Céu parcialmente nublado."
    else:
        return "Céu encoberto, sem necessidade de protecção solar."
    
def rain_analysis(description):
    if "rain" in description or "drizzle" in description or "thunderstorm" in description:
        return "Leve guarda-chuva."
    else:
        return "Sem precipitação prevista."
    

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
    print("Dados meteorológicos atuais:")
    print(f"•Temperatura: {weather_data['temperature']}°C")
    print(f"•Sensação térmica: {weather_data['wind_chill']}°C")
    print(f"•Humidade: {weather_data['humidity']}%")
    print(f"•Velocidade do vento: {weather_data['wind_speed']} m/s")
    print(f"•Nuvens: {weather_data['cloudiness']}%")
    print(f"•Descrição: {weather_data['description']}")
    print("\nAnálise de vestimenta:")
    print(temperature_analysis(weather_data['temperature']))
    print(wind_analysis(weather_data['wind_speed']))
    print(claude_analysis(weather_data['cloudiness']))
    print(rain_analysis(weather_data['description']))
else:
    print("Error:", response.status_code)