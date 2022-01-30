#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from numpy.random import randn


# In[2]:


np.random.seed(101)


# In[3]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[4]:


df


# In[5]:


df['W']


# In[6]:


type(df['W'])


# In[7]:


type(df)


# In[8]:


df.W


# In[9]:


df[['W','Y']]


# In[10]:


df['W + Y'] = df['W'] + df['Y']


# In[11]:


df


# In[12]:


df.drop('W + Y',1)


# In[13]:


df


# In[14]:


dropped_new = df.drop('W + Y',1)


# In[15]:


dropped_new


# In[16]:


df['W + Y'] = df['W'] + df['Y']


# In[17]:


df.drop('W + Y',1,inplace = True)


# In[18]:


df


# In[19]:


df.drop('E',0,inplace=True)


# In[20]:


df


# In[21]:


df.shape


# In[22]:


df.loc['D']


# In[23]:


df.iloc[2] # uses index of row


# In[24]:


df.iloc[2,1:3] # selecting chunks of data (row,column)


# In[25]:


df.loc[['A','B'],['Y','Z']]


# In[26]:


df.iloc[1:3,0:2]


# In[ ]:





# In[27]:


# conditional selection


# In[28]:


df>0


# In[29]:


booldf = df>0


# In[30]:


df[booldf] # null for false


# In[31]:


df['W']>0


# In[48]:


df[df['W']>0]


# In[33]:


df[df['Y']>0]


# In[34]:


df


# In[35]:


df[(df['W']>2) & (df['Z']<1)] # & for and


# In[36]:


df[(df['W']>2) | (df['Z']<0.5)] # |(pipe) for or


# In[ ]:





# In[37]:


df


# In[38]:


df.reset_index()


# In[39]:


df


# In[40]:


df.reset_index(inplace=True)


# In[41]:


df


# In[42]:


newind = 'JAIPUR MUMBAI DELHI BANGLORE'.split()


# In[ ]:





# In[43]:


df['CITIES'] = newind


# In[44]:


df


# In[ ]:





# In[45]:


df.set_index('CITIES')


# In[46]:


df


# In[ ]:




