import requests
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

api_key = os.getenv('API_KEY')

lat = -8.838333
lon = 13.234444

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url)

if (response.status_code == 200):
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)