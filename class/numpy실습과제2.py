
# coding: utf-8

# 질문1

# In[8]:


import numpy as np

A=np.array([[1,2,-1],[1,1,-3]])
B=np.array([[3,2,-2],[-1,2,1]])


# In[9]:


C=A+B
C


# In[10]:


C[0,2]


# 질문2

# In[17]:


C=np.array([[1,2,-1],[1,1,-3]])
D=np.array([[3],[1],[2]])


# In[23]:


E=np.dot(C,D)
print(E)
print()
print(E[0])


# In[19]:


F=np.array([[1,2,-1],[1,1,-3]])
G=np.array([[3,2],[1,1],[2,-1]])


# In[24]:


H=np.dot(F,G)
print(H)
print()
print(H[0,1])


# In[27]:


a=np.array([1,3,4,5,7,8,9,12])
print(np.mean(a))
print(np.average(a))
print(np.median(a))

