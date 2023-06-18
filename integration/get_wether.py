import requests
from time import sleep
CITI = "Petersburg,RU"
API_KEY = "eee4903fb6d18bdf8a151e87a4593b3d"

def get_wether():
    print(API_KEY)
    data = requests.get("http://api.openweathermap.org/geo/1.0/direct",
                 params={'q': CITI, 'APPID': API_KEY}).json()
    lat = data[0]['lat']
    lon = data[0]['lon']
    sleep(1)
    weather = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'lat': lat, 'lon':lon, 'units':'metric',  'APPID': API_KEY}).json()
    return weather


if __name__ == '__main__':
    weather = get_wether()
    print(weather)
    print(type(weather))