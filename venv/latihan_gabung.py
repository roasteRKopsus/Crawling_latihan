import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 100000)
pd.set_option('display.precision', 0)


from terlaris_bl import productprice2_terlaris
from terbaru_bl import  productprice2_terbaru
from relevansi_bl import productprice2_relevansi

from terlaris_bl import productname2_terlaris
from terbaru_bl import productname2_terbaru
from relevansi_bl import productname2_relevansi


harga_df = pd.DataFrame({
    'product name terlaris' : productname2_terlaris,
    'harga terlaris' : productprice2_terlaris,
    'product name terbaru' : productname2_terbaru,
    'harga terbaru' : productprice2_terbaru,
    'product name relevansi' : productname2_relevansi,
    'harga relevansi' : productprice2_relevansi
})

count1= harga_df['harga terlaris'].value_counts()
count2= harga_df['harga terbaru'].value_counts()
count3= harga_df['harga relevansi'].value_counts()

harga_count = pd.DataFrame({

    'terlaris' : count1,
    'terbaru' :count2,
    'relevansi' :count3

})

harga_count.index = harga_count.index.set_names(['foo'])

harga_count2 = harga_count.reset_index().rename(columns={harga_count.index.name:'harga'})



harga_count_bersih = harga_count2.fillna(0)
harga_count_bersih_sum = harga_count_bersih.sum(axis= 1)
harga_count_bersih['sum'] = harga_count_bersih_sum



harga_v2 = pd.DataFrame({

    'terlaris' : count1,
    'terbaru' :count2,
    'relevansi' :count3
})


harga_v2_clean = harga_v2.fillna(0)
harga_v2_clean['sum'] =  harga_v2_clean.sum(axis= 1)




print('x'*100)
print(harga_df)
print(harga_df.describe())
print(harga_count_bersih)
print(harga_count_bersih.shape)
print(harga_count_bersih.describe())
print(harga_v2_clean)
harga_v2_clean.to_csv('bl_1.csv')








