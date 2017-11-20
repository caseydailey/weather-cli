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
    print(weather.text)



if __name__ == '__main__':
    get_weather(37211)