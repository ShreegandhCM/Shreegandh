#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

n=pd.read_csv('play.csv')

n


# In[2]:


conc=np.array(n)[:,:-1]

conc



# In[3]:


tar=np.array(n)[:,-1:]

tar


# In[4]:


def finds(tar,conc):
    for i,val in enumerate(tar):
        if val == 'yes':
            spec = conc[i].copy()
            break
    for i,val in enumerate(conc):
        if tar[i] == 'yes':
            for x in range(len(spec)):
                if val[x]!=spec[x]:
                    spec[x]='?'
                else:
                    pass
        print("hypothesis",i)
        print(spec)
print('The maximally specific hypothesis is')
print(finds(tar,conc))


# In[ ]:




