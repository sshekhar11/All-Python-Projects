#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


IPL= pd.read_csv("matches.csv")


# In[3]:


IPL.head()


# In[4]:


IPL.shape


# In[5]:


IPL['player_of_match'].value_counts()


# In[6]:


# To know the Frequency use .value_counts function
IPL['player_of_match'].value_counts()[0:5]


# In[7]:


# making bar chart
plt.figure(figsize=(8,5))
plt.bar(list(IPL['player_of_match'].value_counts()[0:5].keys()),list(IPL['player_of_match'].value_counts()[0:5]),color="g")
plt.title("Most Player Of The Match Award")
plt.show()


# In[8]:


# Function of Keys
IPL['player_of_match'].value_counts()[0:5].keys()


# In[9]:


IPL['result'].value_counts()


# In[10]:


IPL['toss_winner'].value_counts()


# In[11]:


batting_first=IPL[IPL['win_by_runs']!=0]


# In[12]:


batting_first.head(5)


# In[13]:


plt.figure(figsize=(5,5))
plt.hist(batting_first['win_by_runs'])
plt.title("Distribution of Runs")
plt.xlabel("Runs")
plt.ylabel("Matches")
plt.show()


# In[14]:


batting_first['winner'].value_counts()


# In[18]:


plt.figure(figsize=(7,7))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=["blue","yellow","orange"])
plt.ylabel("Number of matches")
plt.show()        


# In[21]:


plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[23]:


batting_second=IPL[IPL['win_by_wickets']!=0]
batting_second.head()


# In[31]:


plt.figure(figsize=(4,4))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()


# In[33]:


batting_second['winner'].value_counts()


# In[39]:


plt.figure(figsize=(7,5))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=["blue"])
plt.show()      


# In[47]:


plt.figure(figsize=(9,9))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()        


# In[48]:


IPL['season'].value_counts()
#in 2013 most matches are played.


# In[49]:


IPL['city'].value_counts()


# In[52]:


IPL.head(-5)


# In[51]:


np.sum(IPL['toss_winner']==IPL['winner'])


# In[54]:


393/751*100


# In[ ]:




