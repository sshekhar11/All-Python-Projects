#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


dataset = pd.read_csv("covid19_Confirmed_dataset.csv")
dataset.head()


# In[3]:


dataset.shape


# In[4]:


#deleting the useless columns.
df =dataset.drop(["Lat","Long"], axis=1, inplace= True)


# In[ ]:





# In[5]:


dataset.head()


# In[6]:


#aggregating data
aggregated_data = dataset.groupby("Country/Region").sum()


# In[7]:


aggregated_data.head(100)


# In[8]:


#visulizing data
aggregated_data.loc["India"].plot()
aggregated_data.loc["Spain"].plot()
plt.legend()


# In[9]:


aggregated_data.loc["Spain"][:5].plot()


# In[10]:


#calculating the first derivative of the curve.
aggregated_data.loc["India"].diff().plot()


# In[11]:


#maximum infection rate
aggregated_data.loc["India"].diff().max()


# In[12]:


aggregated_data.loc["Libya"].diff().max()


# In[30]:


countries= list(aggregated_data.index)
max_infection_rates = []
    
for c in countries:
    max_infection_rates.append(aggregated_data.loc[c].diff().max())
aggregated_data["Max_infection_rates"] = max_infection_rates


# In[18]:


aggregated_data


# In[23]:


#improrting new dataset happiness datset
happiness_data= pd.read_csv("worldwide_happiness_report.csv")


# In[24]:


happiness_data


# In[25]:


useless_one =["Overall rank","Generosity","Score","Perceptions of corruption"]


# In[27]:


happiness_data.drop(useless_one, axis=1, inplace= True)
happiness_data


# In[ ]:




