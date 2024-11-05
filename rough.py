#!/usr/bin/env python
# coding: utf-8

# In[1]:


#revers of the number
num=int(input("Enter ther number: "))
print("Number is",num)
r=0
while(num!=0):
    d=num%10
    r=r*10+d
    num=num//10
print("Reverse: ",r)


# In[7]:


name=set(input("Enter 2 names: ").split(" "))
print(name)


# In[5]:


name=list(input("Enter 3 names:").split(","))
print(name)


# In[8]:


name=tuple(input("Enter 4 names").split(" "))
print(name)


# In[ ]:




