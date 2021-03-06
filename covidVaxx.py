#!/usr/bin/python3
# https://www.terviseamet.ee/et/koroonaviirus/avaandmed

import requests, json

def jprint(obj):
    #create formatted string of the python json object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


api_link = "https://opendata.digilugu.ee/opendata_covid19_vaccination_total.json" 

response = requests.get(api_link)
jprint(response.json())


