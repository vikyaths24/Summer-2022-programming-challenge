#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[13]:


from bs4 import BeautifulSoup
import urllib3.request,sys,time
import requests
import re 
import json


# In[14]:


url = 'https://www.aljazeera.com/where/mozambique/'
#Use the browser to get the URL. This is a suspicious command that might blow up.

try:
    page= requests.get(url)
    page.raise_for_status()
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)


# In[ ]:





# In[ ]:





# In[15]:


soup = BeautifulSoup(page.text, "html.parser")


# In[ ]:





# In[ ]:





# In[16]:


links2=soup.find_all('a', 
     attrs={'class':'u-clickable-card__link'})


# In[17]:


articlesdata={}
for j,i in enumerate(links2):
    #get top 10 latest articles
    if j<=9:
        try:
            articlesdata[j]=requests.get(
                           'https://www.aljazeera.com'
                                 +str(i['href']))
            articlesdata[j].raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        
        


# In[ ]:





# In[20]:


textvals={}
for i in articlesdata.values():
    soup = BeautifulSoup(i.text, "html.parser")
    #find all headlines in h1 tag
    head=soup.find_all('h1')
    #get all article data in p tag 
    links=soup.find_all('p')
   
    textvals[str(head)]=str(links)


# In[ ]:





# In[21]:


with open('article.json', 'w') as json_file:
    json.dump(textvals, json_file)


# In[ ]:




