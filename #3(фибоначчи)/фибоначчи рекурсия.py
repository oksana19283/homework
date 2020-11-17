#!/usr/bin/env python
# coding: utf-8

# In[7]:


def fibonacci(number):
    if number == 0:
        return 0 
    if number == 1:
        return 1
    return fibonacci(number-1) + fibonacci(number-2);
a=int(input())
for i in range (a):
    print(fibonacci(i))


# In[ ]:





# In[ ]:




