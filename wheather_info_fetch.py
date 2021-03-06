'''---------------------------------------------------------------------------------------------------
                ***     WEATHER INFORMATION USING API IN TEXT FILE      ***
======================================================================================================
        Import modules  ;   Get api -link --key     ;       provide input for location
        send request    ;   store response          ;       varials to store and display data
        generate the text file in project folder containing weather_data/information displayed
---------------------------------------------------------------------------------------------------'''
# import module
import requests
from datetime import datetime
import json

location = input("Enter the city name: ")
api_key = '8593ef4262d25cdeb2d66c4671d6152a'

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
api_data_str = json.dumps(api_data,indent=2)

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#print data to display
print ("-------------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("===================================================================")
print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
print ("-------------------------------------------------------------------")

a = "-------------------------------------------------------------------"
b = "Weather Stats for - {}  || {}".format(location.upper(), date_time)
c = "==================================================================="
d = "Current temperature is: {:.2f} deg C".format(temp_city)
e = "Current weather desc  :",weather_desc
f = "Current Humidity      :",hmdt, '%'
g = "Current wind speed    :",wind_spd, 'kmph'
h = "-------------------------------------------------------------------"

weather_info= '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(a,b,c,d,e,f,g,h)

with open('weather_data.txt','w') as wd:
    wd.writelines(weather_info)

print(api_data_str)
with open('weather_json_str.txt','w') as jd:
    jd.writelines(api_data_str)

print("look in project folder for text file of weather_data")