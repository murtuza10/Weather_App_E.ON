# Weather_App_E.ON

The following gives an idea of the functionality of the app:
 
Shell
$ curl "localhost:8000/headquarter-weather"
{"current_temperature":-0.8,"current_time":"2022-12-16T14:00"}
$ curl "localhost:8000/headquarter-weather?include_maximum=true"
{"current_temperature":-0.8,"current_time":"2022-12-16T14:00","max_temperature":-0.6,"max_temperature_time":"2022-12-16T12:00","max_apparent_temperature":-3.6,"max_apparent_temperature_time":"2022-12-16T12:00"}
