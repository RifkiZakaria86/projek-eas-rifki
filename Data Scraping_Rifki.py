#!/usr/bin/env python
# coding: utf-8

# In[45]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_autoinstaller


# In[106]:


page = requests.get('https://www.indotrading.com/surabaya/jual-tas-kulit')


# In[107]:


soup = BeautifulSoup(page.content, 'html.parser')


# In[79]:


chromedriver_autoinstaller.install()
browser = webdriver.Chrome()


# In[108]:


browser.get('https://www.indotrading.com/surabaya/jual-tas-kulit')


# In[109]:


soup = BeautifulSoup(browser.page_source, 'lxml')


# In[114]:


# ambil 1
soup.find('div', class_='two-lines-elipsis').text.strip()


# In[117]:


# looping ambil semua data
nama_tas = soup.find_all('div', class_='two-lines-elipsis')
daftar_nama = []
for tiap_nama_tas in nama_tas:
    daftar_nama.append(tiap_nama_tas.text.strip())


# In[118]:


daftar_nama


# In[135]:


harga = soup.find_all('div', class_='price')
daftar_harga = []
for tiap_harga in harga:
    daftar_harga.append(tiap_harga.text.strip())


# In[136]:


daftar_harga


# In[138]:


data = {
    'nama_tas' : daftar_nama,
    'harga' : daftar_harga
}


# In[139]:


file = pd.DataFrame(data)


# In[140]:


file


# In[142]:


file.to_csv('Data Scraping_Rifki_002.csv')

