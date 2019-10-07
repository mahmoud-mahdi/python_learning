"""
Script which fetches weather data from
API and displays in terminal
"""
import requests
import logging

api_url = 'https://api.openweathermap.org/data/2.5/weather'
city = 'Brno'
api_key = 'ccb381dc78f36ad77ea966bd8c5fb2c2'


def start_logger(filename, level='DEBUG'):
    """
    Start the logger with logs redirect to file
    :param filename:
    :param level:
    :return:
    """
    f = '[%(levelname)s]\t %(asctime)s %(name)s: %(message)s'
    logging.basicConfig(format=f, filename=filename, level=level)
    logger = logging.getLogger('weather')
    logger.info('logging starts here')
    return logger


def kelvin_to_celsius(temp):
    """
    Converts temp from kelvin to celsius
    :param temp: temperature in kelvin
    :return: temperature in celsius
    """
    return temp - 273.15


def get_weather():
    """
    This function returns the object containig
    the weather data for city
    :return: dict with weather data
    """
    response = requests.get(api_url, params=dict(
        q=city, APPID=api_key
    ))

    # We check if response was valid
    if response.status_code != 200:
        raise Exception('Unable to contact'
                        'weather API')
    return response.json()


def get_weather_desc(weather_dict):
    """
    Given a parsed weather API response,
    returns the weather description
    supports multiple descriptions by
    merging with `and`
    """
    l = list()
    if not weather_dict.get('weather'):
        raise Exception('Missing weather data')
    for weather in weather_dict.get('weather'):
        l.append(weather.get('description'))
    return ' and '.join(l)


def get_temperatures(weather_dict):
    """
    Given the weather dictionary, returns
    a string with current temperature
    and min-max as a string
    """
    main = weather_dict.get('main')
    if not main:
        raise Exception('Weather data missing')
    current_temp = int(kelvin_to_celsius(
        main.get('temp')))
    min_temp = int(kelvin_to_celsius(
        main.get('temp_min')))
    max_temp = int(kelvin_to_celsius(
        main.get('temp_max')))

    return f'Current temperature {current_temp}°C' \
           f' [min:{min_temp}|max:{max_temp}]'


def get_humidity(weather_dict):
    """
    Returns humanly perceived humidity based
    on temperatures and relative air humidity
    """
    # dry = humidity < 20% or temp > 20 and humidity < 45
    # normal = temperature -5|28 humidity 45-55
    # humid = temperature 18-32 humidity 56/85
    # very humid = humidity > 85
    # if none of the above, show numerical value
    humidity = weather_dict['main']['humidity']
    temperature = int(kelvin_to_celsius(
        weather_dict['main']['temp']
    ))
    if humidity < 20 or (temperature > 20 and humidity < 45):
        return 'dry'
    elif (temperature > -5 and temperature < 28) and (humidity > 45 and humidity < 55):
        return 'normal'
    elif (temperature > 18 and temperature < 32) and (humidity > 56 and humidity < 85):
        return 'humid'
    elif humidity > 85:
        return 'very humid'
    else:
        return str(humidity)


if __name__ == '__main__':
    start_logger('weather.log')
    w = get_weather()
    description = get_weather_desc(w)
    temperature = get_temperatures(w)
    humidity = get_humidity(w)

    print(f'Weather in {city}, the {temperature}'
          f' sky condition is: {description}, air'
          f' is: {humidity}')