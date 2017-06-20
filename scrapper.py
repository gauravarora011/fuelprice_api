from bs4 import BeautifulSoup
import requests
from data import link,price

def parse_web(link,fuel_type):
    try:
        URL = link
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        r = requests.get(URL, headers=headers)
        soup = BeautifulSoup(r.content, "lxml")
        for table in soup.find_all('table', class_="product-table"):
            for table_row  in table.find_all('tr'):
                table_data = table_row.find_all('td')
                print table_data[0].text,table_data[1].text
    except:
        print "unable to fetch content from destination website"
    # for div in divs:
    #     time = div.abbr.text
    #     if 'min' not in time and 'mins' not in time :
    #         print ('leaving because there is no post in last one hour')
    #         return
    #     time = [int(s) for s in time.split() if s.isdigit()][0]
    #     if time > threshold:
    #         print ('leaving as all post are processed')
    #         return
    #
    #     heading = div.find('h2',class_='entry-title').find('a').text
    #
    #     p_tag = div.find('div',class_='entry').find_all('p')
    #     for content in p_tag:
    #         if content.img:
    #             image_link = content.img['src']
    #             message =  html_format.italic(content.text)
    #             message += '\n\n'
    #             continue
    #         if content.a:
    #             for anchor in content.find_all('a'):
    #                 message+=html_format.hyperlink(anchor['href'],anchor.text)
    #                 message += '\n\n'
    #         else:
    #             message+=content.text
    #             message += '\n\n'
    #         message += '\n'
    #     bot.send_image(image_link, heading)
    #     bot.send_message(message)

if __name__ == "__main__":
    parse_web(link = link['petrol'],fuel_type='petrol')
    parse_web(link=link['diesel'], fuel_type='diesel')