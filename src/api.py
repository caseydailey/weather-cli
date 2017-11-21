import requests

key = "64683ed7d75439f13859889e3c41bddc"
url = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(zip_code):
    """
    takes a valid zip_code and gets the weather

    args: zip_code string
    returns: weather_report dict

    """
    params = {'zip': zip_code, 'APPID': key}
    weather = requests.get(url, params)    
    report = weather.json()

    conditions = {}

    conditions['city_name'] = report['name']
    conditions['description'] = report['weather'][0]['description']
    conditions['temp'] = kelvin_to_fahrenheit(report['main']['temp'])
    conditions['wind'] = report['wind']['speed']
    conditions['needs_jacket'] = is_cold(kelvin_to_fahrenheit(report['main']['temp']))
    conditions['needs_umbrella'] = True if 'rain' in report else False
    conditions['needs_shades'] = True if report['weather'][0]['description'] == 'sunny' else False

    return conditions
        

def is_cold(temp):
    """
    checks if its cold
    
    args: args int
    returns: bool
    
    """ 
    return True if temp < 60 else False


def kelvin_to_fahrenheit(kelvin_temp):
    """
    helper to convert kelvin_temp to fahrenheit_temp

    args: kelvin_temp int
    returns: fahrenheit_temp int
    """
    fahrenheit_temp = int(1.8 * ( kelvin_temp - 273) + 32)
    return fahrenheit_temp

