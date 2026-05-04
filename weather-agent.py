import requests
import os
from dotenv import load_dotenv
from datetime import datetime


def generate_report(weather_data):
    report = f"Relatório Meteorológico - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"•Temperatura: {weather_data['temperature']}°C\n"
    report += f"•Sensação térmica: {weather_data['wind_chill']}°C\n"
    report += f"•Humidade: {weather_data['humidity']}%\n"
    report += f"•Velocidade do vento: {weather_data['wind_speed']} m/s\n"
    report += f"•Nuvens: {weather_data['cloudiness']}%\n"
    report += f"•Descrição: {weather_data['description']}\n"
    report += "\nAnálise:\n"
    report += f"*Análise de vestimenta: {temperature_analysis(weather_data['temperature'])}\n"
    report += f"*Análise do vento: {wind_analysis(weather_data['wind_speed'])}\n"
    report += f"*Análise das nuvens: {claude_analysis(weather_data['cloudiness'])}\n"
    report += f"*Análise da chuva: {rain_analysis(weather_data['description'])}\n"
    return report

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
    elif 2 <= wind_speed <= 8:
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
            file.write(report);
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    main()