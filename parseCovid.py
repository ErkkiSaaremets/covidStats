#!/usr/bin/python3
# https://www.terviseamet.ee/et/koroonaviirus/avaandmed

import requests, json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://opendata.digilugu.ee/opendata_covid19_hospitalization_profile.json")
jprint(response.json())

#patientcount = patients from this age group and sex hospitalized
# {
#        "AgeGroup": "55-59",
#        "Gender": "N",
#        "LastLoadStatisticsDate": "2021-01-07T00:00:00+02:00",
#        "PatientCount": "77"
#    },

