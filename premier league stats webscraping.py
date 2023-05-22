#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


standings_url = 'https://fbref.com/en/comps/9/Premier-League-Stats'


# In[3]:


data = requests.get(standings_url)


# In[4]:


data.text


# In[5]:


from bs4 import BeautifulSoup


# In[6]:


soup = BeautifulSoup(data.text)


# In[52]:


standings_table = soup.select('table.stats_table')[0]


# In[53]:


standings_table


# In[54]:


links = standings_table.find_all('a')


# In[10]:


links = [l.get('href') for l in links]


# In[11]:


links = [l for l in links if '/squads/' in l]


# In[12]:


links


# In[17]:


team_urls = [f"https://fbref.com{l}"for l in links]
team_urls


# In[22]:


get_ipython().system('pip install html5lib')


# In[27]:


team_url = team_urls[0]


# In[28]:


data = requests.get(team_url)


# In[29]:


import pandas as pd 


# In[36]:


matches = pd.read_html(data.text, match="Scores & Fixtures")
matches[0]

