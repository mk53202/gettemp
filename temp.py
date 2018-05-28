import json
import sensor_temperature
from flask import Flask

my_temp = sensor_temperature.temp
my_time = sensor_temperature.timestamp

app = Flask(__name__)

@app.route('/')
def get_temp():
    return json.dumps(
        {
        'temp':str(my_temp),
        'time':str(my_time)
        }
    )
