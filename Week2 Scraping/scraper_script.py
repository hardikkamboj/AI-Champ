import requests
import pandas as pd
from bs4 import BeautifulSoup

# list of urls all except the first one
urls = ['http://books.toscrape.com/catalogue/page-' + str(i) + '.html' for i in range(2,51)]

# first url 
url = ['http://books.toscrape.com/']

# adding all the urls in a list
url.extend(urls)

print('Number of pages are ',len(url))

names = []
ratings = []
availabilities = []
prices = []
images = []

# iterating through each page
for page in url:
    result = requests.get(page)
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')
    for link in soup.find_all('li',class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3'):
        name = link.find('h3').a['title']
        rating = link.find('p').get('class')[1]
        price = link.find('div',class_ = 'product_price').p.text
        avlb = link.find('div',class_ = 'product_price').find('p',class_ = 'instock availability').text
        img = link.find('img').attrs['src']

        names.append(name)
        ratings.append(rating)
        availabilities.append(avlb)
        prices.append(price)
        images.append(img)




df = pd.DataFrame({'Name':names,'Rating':ratings,'Availability':availabilities,'Price':prices,'Image_src':images})


#saving in a csv file
df.to_csv('all_pages_data.csv')

print('Done')
print('Shape of final df is ',df.shape)
