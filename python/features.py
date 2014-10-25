import re
import os
from os import path
import csv
import json

#Can delete this function when all the data used by the features is saved into json files
def saveData(t):
    with open(path.relpath('FeatureData/Name/names.json'), 'w') as fp:
        json.dump(t, fp)

def isDate(text):
    mat=re.match('([0-2][0-9]|[3][0-1])[/.-]([0][0-9]|[1][0-2])[/.-]([0-2]\d{3})$',text)
    if(mat is None):
        return False;
    return True;


def isPhoneNumber(text):
    mat=re.match('\(?\d{3}\)?\s?\d{3}(\-?|\s?)\d{4}',text)
    if(mat is None):
        return False;
    return True;

def isMonth(text):
    month = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    if text.lower() in month:
        return True
    return False

def isPerson(name):
    with open(path.relpath("FeatureData/Name/names.json")) as f:
        names = json.load(f)
        
    if name in names:
        return True
    return False

def isCountry(country):
    with open(path.relpath("FeatureData/Country/country.json")) as f:
        countries = json.load(f)
    
    if country in countries:
        return True
    return False

def isCity(city):
    with open(path.relpath("FeatureData/City/city.json")) as f:
        cities = json.load(f)
        
    if city in cities:
        return True
    return False


#print(isDate("10.12.2014"))
#print(isPhoneNumber('(805) 280-6071'))
#print(isMonth("January"))
#print(isPerson("Astrid"))
#print(isCountry("Norway"))
#print(isCity("San Francisco"))



    








