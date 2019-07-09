from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

#################################################
# Flask Routes
#################################################  
    
# Renders index page
@app.route("templates/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("templates/cloudiness")
def cloudiness():
    return render_template("cloudiness.html")
    
@app.route("templates/temperature")
def temperature():
    return render_template("temperature.html")

@app.route("templates/humidity")
def humidity():
    return render_template("humidity.html")

@app.route("templates/windspeed")
def windspeed():
    return render_template("humidity.html")

@app.route("templates/comparison")
def comparison():
    return render_template("comparison.html")

@app.route("templates/data")
def data():
    return render_template("data.html")

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
    
