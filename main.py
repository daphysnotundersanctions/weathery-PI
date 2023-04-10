from fastapi import FastAPI

import dataFormatter
import vars

print(vars.currentCity)

appInit = FastAPI()

@appInit.get("/getCurrentCity")
def get_root():
    print(vars.currentCity)
    return { "city" : vars.currentCity}

@appInit.get('/changeCityName/{newCity}')
def change_city(newCity : str ):
    vars.currentCity = newCity
    return{vars.currentCity}

@appInit.get("/getAllCityData")
def get_dataSet():
    return { "cityData" : dataFormatter.sendNewData(vars.currentCity)  }