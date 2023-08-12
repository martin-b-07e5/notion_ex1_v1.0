# app.py
import os
import requests
from flask import Flask, render_template, request
from api_key_utils import api_key_utils

app = Flask(__name__)

try:
    api_key = api_key_utils()
except Exception as e:
  print(e)
  

# paso 8
# Ruta de inicio
@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None

    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)

    return render_template('index.html', weather_data=weather_data)


# Función para obtener datos climáticos de OpenWeatherMap
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=8c5a58462c901349b7c58423129a55dd"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather = {
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return weather

    return None


if __name__ == '__main__':
    app.run()
