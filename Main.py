import requests, json
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = input("City name ")
API_KEY = "2b62511b3bb14c8fbb75f8103ccb9f73"
URL = BASE_URL +"appid=" + API_KEY+"&q="+CITY
response = requests.get(URL)
if response.status_code == 200:
   data = response.json()
   main = data['main'] 
   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   print("Error in the HTTP request")
