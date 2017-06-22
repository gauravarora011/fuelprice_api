from bs4 import BeautifulSoup
import requests
import data
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
                city = city.text.title()
                price = price.text
                if city not in data.prices.keys():
                    data.prices[city] = {}
                data.prices[city][fuel_type] = price
        with open('price_dict.pickle', 'w') as f:
            data.scrap_time = time.gmtime()
            pickle.dump([data.prices,data.scrap_time], f)
    except:
        print "unable to fetch content from destination website"

def scrap_needed():
    print "call to scrapper"
    for fuel, url in data.link.items():
        scrap(link=url, fuel_type=fuel)

def check_for_time(scrap_time):
    cur_time = time.gmtime()
    if scrap_time.tm_mday == cur_time.tm_mday:
        if scrap_time.tm_hour == 0 and scrap_time.tm_hour <= 30:
            if cur_time.tm_hour == 0 and cur_time.tm_hour <= 30:
                return False
            else:
                return True
        else:
            return False
    else:
        if scrap_time.tm_hour == 0 and scrap_time.tm_hour <= 30:
            return False
        else:
            if cur_time.tm_hour == 0 and cur_time.tm_hour <= 30:
                return False
            else:
                return True

def scrapper():
    try:
        if data.prices != {}:
            if check_for_time(data.scrap_time):
                print("exisitng prices old - scrapping again")
                scrap_needed()
        else:
            with open('price_dict.pickle') as f:
                data.prices, data.scrap_time = pickle.load(f)
            if check_for_time(data.scrap_time):
                print("Loaded Prices Expired - scrapping again")
                scrap_needed()
    except:
         scrap_needed()