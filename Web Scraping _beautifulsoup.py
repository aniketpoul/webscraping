#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen


# In[2]:


import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# In[ ]:


import openpyxl

wb = openpyxl.load_workbook("C://Users//hp//Downloads//Input.xlsx")

ws = wb['Sheet1']


# In[ ]:


ws


# In[ ]:


import pandas as pd
df = pd.read_excel("C://Users//hp//Downloads//Input.xlsx") 


# In[ ]:


df


# In[3]:


urls = "https://www.nature.com/articles/d41586-024-01704-2"


# In[4]:


urls


# In[6]:


from bs4 import BeautifulSoup
import requests
import pprint
import re
#import pyperclip

#scrape elements
#title_1 =[]
#for url in urls:
response = requests.get(urls)
page = urlopen(urls)
soup = BeautifulSoup(response.content, "html.parser")
html_bytes = page.read()
html = html_bytes.decode("utf-8")
title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
#title_1.append(title)

    #print titles only
    #h1 = soup.find("title", class_= "class-headline")
print(title)


# In[ ]:


title.values()


# In[ ]:


title


# In[ ]:


for i in url:
    response = response.get(url)
    soup = 


# In[ ]:


store = []
for i in url:
    page = urlopen(url)
    url.append(store)


# In[ ]:


html_bytes = page.read()
html = html_bytes.decode("utf-8")


# In[ ]:


print(html)


# In[ ]:


title_index = html.find("<title>")


# In[ ]:


start_index = title_index + len("<title>")


# In[ ]:


end_index = html.find("</title>")


# In[ ]:


title = html[start_index:end_index]


# In[ ]:


title


# In[ ]:


############

