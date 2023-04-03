import csv
import json
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


#UA ISTA 498 CAPSTONE

'''
Mostly a shopify website scraper returns price and clothing item,
-Adjust 'while loop' for page
amount.
-Adjust return by examining products
or request
'''

def get_page(url,csv,pages):
    page = 0
    title_list = []
    variants_list = []
    handle_list = []
    while page != pages+1:
        products_list_url = f'{url}/products.json?page={page+1}'
        time.sleep(1)
        get_products = requests.get(products_list_url)
        products = get_products.json()["products"]
        for i in products:
            title =i['title']
            handle = i['handle']
            variants = i['variants']
            title_list.append(title)
            handle_list.append(handle)
            variants_list.append(variants)
        page += 1
    price_list = []
    for i in variants_list:
        prices = i[0]['price']
        price_list.append(prices)
    dict = {'Product': title_list, 'Price': price_list}
    df = pd.DataFrame(dict)
    df.to_csv(csv)
    print('DONE - # of entries:', len(price_list))




url = str(input('Input Url: '))
csv_name = str(input('Input CSV File Name (ex:website_name.csv): '))
pages = int(input('Input amount of pages wanted scraped: '))
get_page(url,csv_name,pages)

