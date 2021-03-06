import json
import sensor_temperature
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_temp():
    my_datetime = sensor_temperature.get_datetime()
    my_temperature = sensor_temperature.get_temperature()

    return json.dumps(
        {
        'temperature':str(my_temperature),
        'timestamp':str(my_datetime)
        }
    )
