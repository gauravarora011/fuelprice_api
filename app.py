from flask import Flask,jsonify,render_template
import data
from scrapper import scrapper

app = Flask(__name__)

@app.route('/v1/cities')
def cities():
    scrapper()
    return jsonify({'cities': data.prices.keys()})

@app.route('/v1/fuel-types')
def fuel_list():
    scrapper()
    return jsonify({'fuel_types': data.fuel_type})

@app.route('/v1/price/<city>')
def city_price(city):
    scrapper()
    city = city.title()
    if city in data.prices.keys():
        return jsonify({'price': data.prices[city.title()]})
    else:
        return "city not found"

@app.route('/v1/price/<city>/<fuel>')
def city_fuel_price(city,fuel):
    scrapper()
    city = city.title()
    if fuel not in data.fuel_type:
        return "Fuel Type Invalid"
    if city in data.prices.keys():
        return jsonify({'price': data.prices[city.title()][fuel]})
    else:
        return "city not found"

@app.route('/')
def hello_world():
    scrapper()
    return render_template('index.html',city_list=data.prices.keys(),fuel_type=data.fuel_type)
    #return "Welcome"

if __name__ == "__main__":
    app.run(debug=False)