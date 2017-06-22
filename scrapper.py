from bs4 import BeautifulSoup
import requests
from data import link,prices
import pickle
import time

def scrap(link,fuel_type):
    try:
        URL = link
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        r = requests.get(URL, headers=headers)
        soup = BeautifulSoup(r.content, "lxml")
        for table in soup.find_all('table', class_="product-table"):
            for table_row  in table.find_all('tr'):
                city,price = table_row.find_all('td')
                city  = city.text.title()
                price = price.text
                if city not in prices.keys():
                    prices[city] = {}
                prices[city][fuel_type] = price
        with open('price_dict.pickle', 'w') as f:
             pickle.dump([prices,time.gmtime()], f)
    except:
        print "unable to fetch content from destination website"

def scrap_needed():
    print "call to scrapper"
    for fuel, url in link.items():
        scrap(link=url, fuel_type=fuel)
    print prices

def scrapper():
    global prices
    try:
        if prices != {}:
            print "Prices Already Exist"
            with open('price_dict.pickle') as f:
                 prices,last_time = pickle.load(f)
        else:
            scrap_needed()
    except:
        scrap_needed()