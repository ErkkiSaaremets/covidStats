#!/usr/bin/python3
# https://www.terviseamet.ee/et/koroonaviirus/avaandmed
# patientcount = patients from this age group and sex hospitalized
# {
#        "AgeGroup": "55-59",
#        "Gender": "N",
#        "LastLoadStatisticsDate": "2021-01-07T00:00:00+02:00",
#        "PatientCount": "77"
#    },


import requests, json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

api_link = "https://opendata.digilugu.ee/opendata_covid19_hospitalization_profile.json"

response = requests.get(api_link)
jprint(response.json())

