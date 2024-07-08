from django.shortcuts import render
import requests
import datetime
from django.views.decorators.csrf import csrf_protect
# Create your views here.
@csrf_protect
def Index(request):
    #load api key
    API_KEY = open("Weather/API_KEY", "r").read().strip()
    #fetches the current weather data from 
    #OpenWeatherMap API and has two placeholders
    #"{}" for the location and unique api key identifier for authencticating the request
      
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}"
    
    #fetches forecast data from the "Openweathermap" api using the "onecall" endpoint
    #including both the latitude and longitude of rhe location
    forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hour,alerts&appid={}"

    if request.method == "POST":
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        try:
            weather_data1, daily_forecasts1 = fetch_weather_forecast(city1, API_KEY, current_weather_url, forecast_url)
        except Exception as e:
            weather_data1, daily_forecasts1 = None, []
            print(f"Error fetching weather for {city1}: {e}")

        weather_data2, daily_forecasts2 = None, []

        if city2:
            try:
                weather_data2, daily_forecasts2 = fetch_weather_forecast(city2, API_KEY, current_weather_url, forecast_url)
            except Exception as e:
                weather_data2, daily_forecasts2 = None, []
                print(f"Error fetching weather for {city2}: {e}")

        context = {
            'weather_data1' : weather_data1,
            'daily_forecasts1' : daily_forecasts1,
            'weather_data2' : weather_data2,
            'daily_forecasts2' : daily_forecasts2
        }

        return render(request, "views/index.html", context)

    else:
        return render(request, "views/index.html")
    
def fetch_weather_forecast(city,api_key, current_weather_url, forecast_url):
    #assume response to be a dictionary obtained from parsing json
    #to obtain weather api
    response = requests.get(current_weather_url.format(city, api_key)).json()

    lat = response.get('coord', {}).get('lat')
    lon = response.get('coord', {}).get('lon')
    if lat is None or lon is None:
        raise ValueError("Could retieve coordinates for the city.")

    forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()

    print(f"Current weather response for {city}: {response}")
    print(f"Forecast response for {city}: {forecast_response}")

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon']
    }

    daily_forecasts = [] #A list that stores dictionaries each representing the forecast for the day
    if 'daily' in forecast_response:
        for daily_data in forecast_response['daily'][:5]:
            daily_forecasts.append(
                {
                    'day': datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
                    "min_temp": round(daily_data['temp']['min'] - 273.15, 2),
                    "max_temp": round(daily_data['temp']['max'] - 273.15, 2),
                    'description': daily_data['weather'][0]['description'],
                    'icon': daily_data['weather'][0]['icon']
                }
            )
    else:
        print(f"Error fetching daily forecast for {city}: 'daily' key is missing in response")

    return weather_data, daily_forecasts