from flask import Flask, render_template
from markupsafe import escape

#flask --app server.py run --host=0.0.0.0

app = Flask(__name__)

@app.route('/api/water/amount/<int:amount>')
def water_amount(amount):
    #TODO: add function for watering plants a specific amount
    return {"amount": amount}

@app.route('/api/water/to/<int:amount>')
def water_to(amount):
    #TODO: add function for watering plants to specific level
    return {"amount": amount}

@app.route('/api/waterlevel')
def water_level():
    #TODO: get_water_level function
    return {"waterlevel": "100"}

@app.route('/api/moisture')
def moisture():
    #TODO: get_moisture function
    return {"moisture": "50"}


@app.route('/')
def index():
    return render_template('./index.html')