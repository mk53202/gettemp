import json

from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_temp():
    temp = 77
    return json.dumps({'temp':str(temp)})
