#!/usr/bin/env python
# coding: utf-8

# In[13]:


def border(dict,name):
    if name in dict:
         dict[name]=dict[name]+1
    else:
        dict[name]=1
    return dict
dict_name={}
a='s'
while a!=True:
    a=input('Хто пеертинає кордон?')
    if a=='END':
        break
    else:
        border(dict_name,a)

for key in dict_name:
    print(key,dict_name[key])


# In[ ]:





# In[ ]:


8

