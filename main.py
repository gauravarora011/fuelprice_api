from flask import Flask,jsonify
from data import prices,fuel_type
from Scrapper import scrapper

app = Flask(__name__)

@app.route('/<city>')
def city_price(city):
    city = city.lower()
    if city in prices.keys():
        return jsonify({'price': prices[city.lower()]})
    else:
        return "city not found"

@app.route('/')
def hello_world():
    return "Welcome"

if __name__ == "__main__":
    scrapper()
    app.run(debug=True)