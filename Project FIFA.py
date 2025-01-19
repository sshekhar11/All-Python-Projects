#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


fifa = pd.read_csv("players_20.csv")


# In[3]:


fifa.head()


# In[4]:


fifa.shape


# In[5]:


for col in fifa.columns:
    print(col)


# In[6]:


fifa['nationality'].value_counts()


# In[7]:


fifa['nationality'].value_counts()[0:10]


# In[8]:


plt.figure(figsize=(8,5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color="g")
plt.show()


# In[9]:


player_salary = fifa[['short_name','wage_eur']]


# In[10]:


player_salary.head(10)


# In[11]:


player_salary=player_salary.sort_values(by=['wage_eur'],ascending=False)


# In[12]:


player_salary.head()


# In[13]:


plt.figure(figsize=(8,5))
plt.bar(list(player_salary['short_name'])[0:5],list(player_salary['wage_eur'])[0:5],color="r")
plt.show()


# In[14]:


fifa['nationality']=='Germany'


# In[15]:


Germany=fifa[fifa['nationality']=='Germany']
Germany.head(11)


# In[17]:


Germany.sort_values(by=['height_cm'],ascending=False).head()


# In[18]:


Germany.sort_values(by=['weight_kg'],ascending=False).head()


# In[19]:


Germany.sort_values(by=['wage_eur'],ascending=False).head(10)


# In[22]:


Germany[['short_name','wage_eur']].sort_values(by=['wage_eur'],ascending=False).head(11)


# In[39]:


player_shooting=fifa[['short_name','shooting']]


# In[40]:


player_shooting.sort_values(by=['shooting'],ascending=False).head()


# In[34]:


best_defender=fifa[['short_name','defending','club','nationality',]]


# In[35]:


best_defender.head()


# In[36]:


best_defender.sort_values(by=['defending'],ascending=False).head()


# In[41]:


real_madrid=fifa[fifa['club']=='Real Madrid']


# In[42]:


real_madrid.head()


# In[46]:


real_madrid.sort_values(by=['shooting'],ascending=False).head(5)


# In[45]:


real_madrid.sort_values(by=['wage_eur'],ascending=False).head(5)


# In[47]:


real_madrid.sort_values(by=['defending'],ascending=False).head(5)


# In[48]:


real_madrid['nationality'].value_counts().head()


# In[ ]:




