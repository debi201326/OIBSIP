import requests
import json

#API details
base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "dc853c14c29492dfd8aecc10230dd593"

try:
    city = input('Enter the location or city name or ZIP code : ')

    #parameters or inputs to API
    api_inputs = {
            "q": city,
            "appid": api_key,
            "units":"metric"
        }
        
    #API request
    response = requests.get(base_url, api_inputs)
    data = response.json()

    if data["cod"] == 200:
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        visibility = data["visibility"]
        min_temp = data["main"]["temp_min"]
        max_temp = data["main"]["temp_max"]

        #Printing the respone or weather information
        print(f"***** The weather of  {city} *****")
        print(f"Description : {description} ")
        print(f"Temperature : {temperature} °C" )
        print(f"Minimum temperature : {min_temp} °C" )
        print(f"Maximum temperature : {max_temp} °C" )
        print(f"Feels like : {feels_like} °C")
        print(f"Humidity : {humidity} %")
        print(f"Wind speed : {wind_speed} km/hr")
        print(f"Pressure : {pressure} mBar")
        print(f"Visibility : {visibility} m")
        
    else:
        print("Location not found. \nPlease check the spelling or try another loaction.")

except Exception as e:
    print('An error occured.',e)