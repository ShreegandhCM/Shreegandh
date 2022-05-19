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


def cand(conc, tar): 
    specific = conc[0].copy()
    
    print("\nSpecific Boundary: ", specific)
    general = [["?" for i in range(len(specific))] for i in range(len(specific))]
    print("\nGeneric Boundary: ",general)  

    
    for i, val in enumerate(conc):
        print("\nInstance", i+1 , "is ", val)

        if tar[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(specific)): 
                if val[x]!= specific[x]:                    
                    specific[x] ='?'                     
                    general[x][x] ='?'
                
        if tar[i] == "no":            
            print("Instance is Negative ")
            for x in range(len(specific)): 
                if val[x]!= specific[x]:                    
                    general[x][x] = specific[x]                              
                else:                    
                    general[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", specific)         
        print("Generic Boundary after ", i+1, "Instance is ", general)
        print("\n")

    indices = [i for i, val in enumerate(general) if val == ['?', '?', '?', '?', '?', '?']]    
    
    for i in indices:   
        general.remove(['?', '?', '?', '?', '?', '?']) 
    
    return specific, general 
s_final, g_final = cand(conc, tar)

print("Final Specific: ", s_final, sep="\n")

print("Final General: ", g_final, sep="\n")


# In[ ]:



.

