import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import numpy as np

def website_target(site_page) :
    hdr = {'user-agent': 'GoogleChrome'}
    req = Request(site_page, headers=hdr)
    page = urlopen(req)
    page_soup = BeautifulSoup(page, 'html.parser')
    # print(page_soup.find_all('a'))

    product_raw = page_soup.find(class_='basic-products basic-products--grid')
    product_row = product_raw.find_all(class_='col-12--2')
    productprice =[productprice.find(class_='amount positive').get_text() for productprice in product_row]

    price_no_dot = [i.replace(".", "") for i in productprice]

    productname2 =[x.replace("\n, ' '", '') for x in productname]
    productrating2 = [x.replace('\n', '') for x in productrating]
    productprice2 = [int(i) for i in price_no_dot]



