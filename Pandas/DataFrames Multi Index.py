#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd


# In[ ]:





# In[22]:


outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[24]:


hier_index


# In[27]:


df = pd.DataFrame(np.random.randn(6,2),hier_index,['A','B'])


# In[28]:


df


# In[29]:


df.index.names = ['GROUP','INDEX']


# In[30]:


df


# In[34]:


df.loc['G2'].loc[3]


# In[35]:


df.loc['G2'].loc[3]['B']


# In[36]:


df


# In[39]:


df.xs('G1') # cross section


# In[41]:


df.xs(3,level='INDEX')


# In[ ]:




