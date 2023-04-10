
import requests

import vars


def sendNewData(i):
    global dataSet
    dataSet =  requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={i}&units=metric&appid={vars.key}').json()
    weatherStat = dataSet['weather'][0]['main']
    weatherTemp = dataSet['main']['temp']
    weatherPressure = dataSet['main']['pressure']
    weatherWindSpeed = dataSet['wind']['speed']
    dataSet =  f'Now in {vars.currentCity} : {weatherStat}, Temperture : {weatherTemp}°C, Pressure : {weatherPressure}, Wind speed : {weatherWindSpeed} '
    print(dataSet)  
    return dataSet