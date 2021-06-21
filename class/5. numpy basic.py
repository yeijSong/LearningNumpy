
# coding: utf-8

# * 2중 리스트, NumPy의 2차원 배열(왼쪽 부분에 대괄호가 2개)

# In[1]:


import numpy as np

b=np.array([[0,1,2],[3,4,5]])
print(b)


# * 3중 리스트, NumPy의 2차원 배열(왼쪽 부분에 대괄호가 3개)

# In[2]:


c=np.array([[[0,1,2],[3,4,5]],[[5,4,3],[2,1,0]]])
print(c)


# * 배열을 생성하는 여러가지 함수

# In[4]:


d=np.zeros(8)
e=np.ones(8)
f=np.arange(8)

print(d)
print(e)
print(f)


# * shape()함수에 의해 배열의 형태를 얻는다

# In[5]:


a=np.array([[0,1,2],[3,4,5]])
print(np.shape(a))


# * len()에 의해 가장 바깥쪽의 요소 수를 얻는다

# In[6]:


print(len(a)) #a의 행의 수를 얻는다


# * 배열끼리의 연산

# In[7]:


a=np.array([[0,1,2],[3,4,5]])

print(a)
print()
print(a+3)
print()
print(a*3)


# In[8]:


b=np.array([[0,1,2],[3,4,5]])
c=np.array([[2,0,1],[5,3,4]])

print(b)
print()
print(c)
print()
print(b+c)
print()
print(b*c) # 행렬의 곱셈이 아닌 [0,1,2]와[2,0,1] 
            # 그리고 [3,4,5]와 [5,3,4]가 곱해진 상태


# * 인덱스 지정하고 요소를 바꾸기

# In[9]:


a=np.array([1,2,3,4,5])
print(a)


# In[10]:


a[2]=7
print(a)


# In[11]:


b=np.array([[0,1,2],[3,4,5]])
print(b[1,2])


# In[12]:


b[1,2]=9
print(b)


# In[13]:


print(b[1,:]) #인덱스가 1인 행을 취득


# In[14]:


c[:,1]=np.array([6,7])
print(c)


# In[15]:


a=np.array([[0,1,2],[3,4,5]])

print('합계 : ',np.sum(a))
print('평균 : ',np.average(a))
print('최대값 : ',np.max(a))
print('최소값 : ',np.min(a))


# ### 예제 : numpy 2차원 배열 기술 수 사칙연산해보기

# In[16]:


a=np.array([[0,1,2],[3,4,5]])
b=np.array([[5,4,3],[2,1,0]])


# In[19]:


print('a+b=',a+b)
print()
print('a-b=',a-b)
print()
print('a*b=',a*b)

