#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv(r"C:\Users\SUVAM\Desktop\Time series datasets\AirPassengers.csv")
data.head()


# In[3]:


M = data.Month
P = data["#Passengers"]


# In[4]:


#moving average
   
YP = P.rolling(12).mean()               


# In[5]:


# visualizing the trend

plt.figure(figsize=(10,5))
plt.plot(M,P,color='red')                  
YP.plot()
plt.title('Time Series Graph')
plt.xlabel('Date')
plt.ylabel('No. of Passengers')
plt.show()


# In[ ]:


SP1 = []
for i in range(0,len(P)):
    SP1.append(h[i]/YP[i])


# In[ ]:


#Seasonality after eliminating the trend

plt.figure(figsize=(10,5))
plt.plot(SP1)
plt.title('Seasonality')
plt.xlabel('Date')
plt.ylabel('No. of Passengers')
plt.show()


# In[10]:


import statsmodels.tsa.seasonal as sm


# In[15]:


#seasonal decomposition 

data_com = sm.seasonal_decompose(P,period=12)       
data_com.plot()


# In[ ]:





# In[ ]:




