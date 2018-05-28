from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_temp():
    temp = 77
    return str(temp)
