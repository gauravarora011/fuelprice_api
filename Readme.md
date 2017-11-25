# Fuel Price API for India
Get Latest fuel prices for different Indian Cities

view the live version : https://dailyfuelprice.herokuapp.com/

## API Endpoint :

Base URL: ```http://dailyfuelprice.herokuapp.com/v1```
* GET ```/cities```

List all the possible city options
* GET ```/fuel_types```

List all the possible fuel options
* GET ```/price/<city>```

List all fuel prices for the supported citites (this includes all possible fuel options)
* GET ```/price/<city>/<fuel>```

Returns the price for specific city and fuel-type

