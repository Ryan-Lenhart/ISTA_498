#!/usr/bin/env python
# coding: utf-8

# In[7]:


pip install selenium


# In[1]:


number_of_pages = 99 * 4


# In[17]:


import os
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
firefox_driver = os.path.join(os.getcwd(),'Drivers',"geckodriver.exe")
firefox_service = Service(firefox_driver)
firefox_options = Options()
firefox_options.set_preference('general.useragent.override',user_agent)

#Launching Browser
browser = webdriver.Firefox(service = firefox_service, options = firefox_options)
browser.get("https://www.thereformation.com/clothing?page=1")


# In[25]:


browser = webdriver.Firefox(service = firefox_service, options = firefox_options)
browser.get("https://www.thereformation.com/clothing?page=1")
clothing_lst = []
clothing_lst_website = browser.find_elements(By.CLASS_NAME,'product-tile__body-section.product-tile__name') 
browser.close


# In[26]:


clothing_lst_website


# In[19]:


#url = 'https://us.shein.com/Women-Clothing-c-2030.html?ici=us_tab01navbar05&scici=navbar_WomenHomePage~~tab01navbar05~~5~~real_2030~~~~0&src_module=topcat&src_tab_page_id=page_home1675721225481&src_identifier=fc%3DWomen%60sc%3DCLOTHING%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar05%60jc%3Dreal_2030&srctype=category&userpath=category-CLOTHING&page='+str(page)
#url = "https://www.thereformation.com/clothing?page=1"
clothing_lst = []
clothing_lst_website = browser.find_elements(By.CLASS_NAME,'product-tile__body-section product-tile__name') 
#print(len(clothing_list))
for thing in range(len(clothing_lst_website)):
    clothing_lst.append(clothing_lst_website[thing].text)    
#---------------------------------------------------------------------------------------------------------------------------    
listed_price_lst = []
listed_price_lst_website = browser.find_elements(By.CLASS_NAME,'price')
#print(len(listed_price_lst_website))
for thing in range(len(listed_price_lst_website)):
    listed_price_lst.append(listed_price_lst_website[thing].text)
#---------------------------------------------------------------------------------------------------------------------------
clothing_lst_website = clothing_lst_website.clear()
listed_price_lst_website = listed_price_lst_website.clear()


# In[7]:


print(len(listed_price))


# In[29]:


def web_scraping_page(page_num):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
    firefox_driver = os.path.join(os.getcwd(),'Drivers',"geckodriver.exe")
    firefox_service = Service(firefox_driver)
    firefox_options = Options()
    firefox_options.set_preference('general.useragent.override',user_agent)
    browser = webdriver.Firefox(service = firefox_service, options = firefox_options)
    

    url = 'https://www.thereformation.com/clothing?page='+str(page_num)
    
    browser.get(url)
    browser.execute_script("window.scrollBy(0,250);")
    
    time.sleep(20)
    
    #clothing names
    clothing_lst = []
    clothing_lst_website = browser.find_elements(By.CLASS_NAME, 'product-tile__body-section.product-tile__name') 
    #prices
    listed_price_lst = []
    listed_price_lst_website = browser.find_elements(By.CLASS_NAME,'price')   
       
    for thing in range(len(clothing_lst_website)):
        clothing_lst.append(clothing_lst_website[thing].text)
        listed_price_lst.append(listed_price_lst_website[thing].text)
       
    browser.close()    
    return clothing_lst, listed_price_lst  


# In[30]:


print(web_scraping_page(1))


# In[31]:


print(web_scraping_page(2))


# In[32]:


entire_clothing_names = []
entire_prices = []

max_num_pages = 50

for i in range(max_num_pages):
    entire_clothing_names.append(web_scraping_page(i)[0])
    entire_prices.append(web_scraping_page(i)[1])


# In[ ]:


print(entire_clothing_names[39],entire_prices[39])


# In[33]:


import pandas as pd
print(entire_clothing_names[0])
print(entire_prices[0])


# In[ ]:





# In[ ]:





# In[34]:


entire_clothing_names.clear()
entire_prices.clear()


# In[35]:


copy_of_entire_clothing_names = entire_clothing_names.copy()
copy_of_entire_prices = entire_prices.copy()


# In[42]:


#copy_of_entire_prices = sum(copy_of_entire_prices,[])
copy_of_entire_clothing_names = sum(copy_of_entire_clothing_names,[])


# In[43]:


len(copy_of_entire_prices)


# In[44]:


copy_of_entire_clothing_names.append('0')
len(copy_of_entire_clothing_names)


# In[45]:


Tf_series = pd.Series(copy_of_entire_prices,index = copy_of_entire_clothing_names)


# In[46]:


Tf_series


# In[68]:


Tf_series.to_csv(r'C:\Users\Braydon\Desktop\Shein_Data\Tf_Series.csv', index = True, header = False)


# In[ ]:




