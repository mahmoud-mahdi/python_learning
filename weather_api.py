"""
Script which fetches weather data from api and display it in terminal
"""

import requests

api_url = 'http://api.openweathermap.org/data/2.5/weather'
city = 'Brno'
api_key = 'ccb381dc78f36ad77ea966bd8c5fb2c2'


def kelvin_to_celsius(temp):
    """
    converts tem from kelvin to celsius
    :param temp: temp in Kelvin
    :return: temp in celsius
    """
    return temp - 273.15


def pressure_eval(pressure):
    if pressure <= 800:
        return 'Low'
    elif pressure >= 1300:
        return 'High'
    else:
        return 'Normal'


def wind_eval(wind_spd):
    if wind_spd >= 25:
        return 'Windy'
    else:
        return 'With no Winds'


def humidity_eval(humidity):
    pass


def dangerous_weather(temp, humidity):
    if humidity >= 93:
        if temp >= 30:
            print('!!!!!!!!Warning please stay home or you will be grilled!!!!!!!!')
        elif temp <= -5:
            print('!!!!!!!!Warning: Stay home or your bones will be friezed!!!!!!!!')


def get_weather():
    """
    this function returns the object containing the weather data for City
    :return: dict with weather data
    """
    response = requests.get(api_url, params=dict(q=city, APPID=api_key))

    #check if response is valid
    if response.status_code != 200:
        raise Exception('Unabel to contact Weather API')
    return response.json()


weather_dic = get_weather()
weather_main = weather_dic['weather'][0]['main']
temp = round(kelvin_to_celsius(weather_dic['main']['temp']), 1)
pressure = pressure_eval(weather_dic['main']['pressure'])
humidity = weather_dic['main']['humidity']
temp_min = kelvin_to_celsius(weather_dic['main']['temp_min'])
temp_max = kelvin_to_celsius(weather_dic['main']['temp_max'])
wind_spd = weather_dic['wind']['speed']
wind_activity = wind_eval(wind_spd)

dangerous_weather(temp, humidity)

print(f'The Weather today in {city} is {wind_activity},'
      f'{weather_main}, Tempreture is: {temp} [{temp_min}'
      f'|{temp_max}], humidity is {humidity} and the Press'
      f'ure is:{pressure}')
