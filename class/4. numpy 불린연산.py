
# coding: utf-8

# In[1]:


import numpy as np
array1=np.array([2,3,5,7,11,13,17,19,23,29])


# In[3]:


array1


# In[4]:


array1>4


# In[5]:


array1%2==0


# In[6]:


booleans=np.array([True,True,True,True,False,False,True])


# In[7]:


np.where(booleans) # True인 값만 출력된다


# In[8]:


np.where(array1>4)

