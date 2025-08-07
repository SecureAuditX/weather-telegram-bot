# Weather Request logic
import requests # for sending http request
from Config import WEATHER_API_KEY

# function that get weather info using the API key
def get_weather(city):
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    # send get response to OpenWeatherMap
    response = requests.get(URL)
    
   # If response is successfully Exract the actual data
    if response.status_code == 200:
        # convert response to dictionary
        data = response.json()
        temperature = data['main']['temp'] # get temperature
        condition = data['weather'][0]['description'] # get weather condition
        return temperature, condition
    # If is invalid of API fails, returns None
    else:
        return None, None
    