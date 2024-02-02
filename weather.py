from datetime import datetime,timedelta
import requests

# Method for getting latitude and longitude of address provided in headquarter_address variable
def get_lat_long(headquarter_address):
    resp = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={headquarter_address["City"]}&count=10&language=en&format=json').json()
    for data in resp['results']:
        if data.get('country') == headquarter_address['Country'] and data.get('admin1') == headquarter_address['admin1']:
            lat,long = data.get('latitude'), data.get('longitude')
    return lat, long

#Method for retreiving current weather by making an api request, if include_maximum = true then additional fields are returned 
def get_current_weather(lat,long,include_maximum):
        current_time = datetime.now()
        rounded_time = current_time.replace(minute=0, second=0, microsecond=0)
        if current_time.minute >= 30:
            rounded_time += timedelta(hours=1)
        formatted_result = rounded_time.strftime('%Y-%m-%dT%H:%M')
        resp = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,apparent_temperature&timezone=Europe%2FBerlin&forecast_days=1').json()
        time_index = resp.get('hourly').get('time').index(formatted_result)
        # finding current_temperature by index of current_time
        current_temperature = resp.get('hourly').get('temperature_2m')[time_index]
        # finding max_temperature by finding max in list of all temperaures
        max_temperature = max(resp.get('hourly').get('temperature_2m'))
        # finding max_apparent_temperature by finding max_apparent_temperature in list of all apparent_temperatures
        max_apparent_temperature = max(resp.get('hourly').get('apparent_temperature'))
        #getting index of max_temperature
        max_temperature_index = resp.get('hourly').get('temperature_2m').index(max_temperature)
        #getting index of max_apparent_temperature
        max_apparent_temperature_index = resp.get('hourly').get('apparent_temperature').index(max_apparent_temperature)
        max_temperature_time = resp.get('hourly').get('time')[max_temperature_index]
        max_apparent_temperature_time = resp.get('hourly').get('time')[max_apparent_temperature_index]
        if include_maximum :
          TemperatureData = {
               'current_temperature': current_temperature,
               'current_time': formatted_result,
               'max_temperature':max_temperature,
               'max_temperature_time':max_temperature_time,
               'max_apparent_temperature':max_apparent_temperature,
               'max_apparent_temperature_time': max_apparent_temperature_time
               }
        else:
          TemperatureData = {
               'current_temperature': current_temperature,
               'current_time': formatted_result,
               }
        return TemperatureData


def main(headquarter_address,include_maximum):
     lat, long = get_lat_long(headquarter_address)
     return get_current_weather(lat,long,include_maximum)