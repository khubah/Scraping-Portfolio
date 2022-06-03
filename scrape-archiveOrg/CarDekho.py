#CarDekho
import requests
from bs4 import BeautifulSoup as bs
import csv
url = 'https://web.archive.org/web/20110924050541/http://www.cardekho.com/search/AllBrands/AllVehicleStyles/AllPriceRanges/Price-Low-High'
page = requests.get(url)
soup = bs(page.content, 'html.parser')

cars = soup.findAll('div', {'class' : 'comparediv'})

#find cars brand name
cars_brand = []
for b in soup.findAll('span', {'class': 'vechilediv'}):
  p = b.text.find('\xa0')
  brand = b.text[0:p]
  cars_brand.append(brand.strip())
results = []
for car in cars:
    titles = car.findAll('div', {'class':'widthfiftyfour leftfloat'})
    prices = car.findAll('div', {'class':'pricereal'})
    # r = {}
    for t in range(len(titles)):
        title = titles[t].text.strip()
        price = prices[t].find('span').text
        for car_brand in cars_brand:
            if title.find(car_brand) != -1:
                brand = car_brand
                car_model = title.replace(brand,'').strip()
                r = {'Brand' : brand, 'Car Model': car_model, 'Price': price}
                results.append(r)
csv_columns = ['Brand', 'Car Model', 'Price']
csv_file = 'results.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=csv_columns)
    writer.writeheader()
    for data in results:
        writer.writerow(data)