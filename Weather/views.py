from django.shortcuts import render
import requests
import json


def weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "d604e1fcd97ba3c56baffd849bba5c53"
    parameters = { 
        'q': city,
        'appid' : api_key,
        'units'  : 'metric'    
    }
    response = requests.get(base_url, params = parameters)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"code{response.status_code}")
        print(f"response{response.text}")
        return None

  
def home(request):
    city = request.GET.get("city")
    icon_url = "https://openweathermap.org/img/wn/10d@2x.png"
    print(f" Recived city {city}")
    if city is None:
        city_name = 'Hyderabad'   

    if city:
        weather_data_result = weather(city)        
          # if weather_data_result is not None:
          #  weather_data = json.dumps(weather_data_result,indent=4)
            
        #Extracting Details
        icon = weather_data_result['weather'][0]['icon']
        icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
        main_weather = weather_data_result['weather'][0]['main']
        weather_description = weather_data_result['weather'][0]['description']
        city_name = weather_data_result['name']
        country = weather_data_result['sys']['country']
        wind_speed = weather_data_result['wind']['speed']
        pressure = weather_data_result['main']['pressure']
        humidity = weather_data_result['main']['humidity']
        temp = weather_data_result['main']['temp']

    else:
        return render(request,'index.html')
        
    return render(request, 'index.html', {  
        'main_weather' : main_weather,
        'weather_description' : weather_description,
        'city_name' : city_name,
        'country' : country,
        'wind_speed' : wind_speed,
        'pressure' : pressure,
        'humidity' : humidity,
        'temp' : temp,
        'icon_url' : icon_url,
    })
    


    
