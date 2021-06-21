
# coding: utf-8

# ### - 행렬의 곱셈

# In[1]:


import numpy as np

a=np.array([[0,1,2],[1,2,3]])
b=np.array([[2,1],[2,1],[2,1]])

print(np.dot(a,b))


# ### - cf. 요소별 곱셈

# In[3]:


c=np.array([[0,1,2],[3,4,5],[6,7,8]])
d=np.array([[0,2,0],[2,0,2],[0,2,0]])

print(c*d)
print()
print(np.dot(c,d))

