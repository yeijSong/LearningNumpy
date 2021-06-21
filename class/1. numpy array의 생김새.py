
# coding: utf-8

# In[1]:


import numpy
array1=numpy.array([2,3,5,7,11,13,17,19])


# In[2]:


array1


# In[14]:


type(array1)


# └ndarray는 n차원의 행렬이라는 뜻

# In[4]:


array1.shape


# In[5]:


array2=numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# In[6]:


array2


# In[7]:


type(array2)


# In[8]:


array2.shape


# In[9]:


array1.size


# In[10]:


array2.size


# ### **실습**

# In[11]:


import numpy

array1=numpy.full(6,0)
array2=numpy.random.random(6)


# In[15]:


array1


# In[16]:


array2


# In[17]:


import numpy as np

array1=numpy.full(6,0)
array2=numpy.random.random(6)


# In[18]:


array1


# In[19]:


array2

