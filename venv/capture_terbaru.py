import requests

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import numpy as np
import site_input as

site = site_terbaru
hdr = {'user-agent' : 'GoogleChrome'}

req = Request(site, headers=hdr)
page = urlopen(req)
page_soup = BeautifulSoup(page, 'html.parser')
#print(page_soup.find_all('a'))

product_raw = page_soup.find(class_ = 'basic-products basic-products--grid' )
product_row = product_raw.find_all(class_ = 'col-12--2')

productprice = [productprice.find(class_='amount positive').get_text() for productprice in product_row]
price_no_dot = [i.replace(".","") for i in productprice]

productname2_relevansi = [x.replace("\n, ' '" , '') for x in productname]
productrating2 = [x.replace('\n', '') for x in productrating]
productprice2_relevansi = np.array([int(i) for i in price_no_dot])