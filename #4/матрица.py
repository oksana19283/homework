#!/usr/bin/env python
# coding: utf-8

# In[6]:


arr = [[0] * 4 for i in range(3)]
s=0
maximum=0
max_arr=[]
for n in range(3):
    for m in range(4):
        arr[n][m]=int(input())
        s= arr[n][m]+s
        if arr[n][m]>maximum:
            maximum=arr[n][m]
    max_arr.append(maximum)
for i in range(3):
    print(arr[i])
print("the sum of all numbers in the matrix=",s)
print("Max element in matrix=",max(max_arr))

s_1=0
for i in range(4):
    s_1=arr[0][i]+s_1
print("first row sum",s_1)


mins = arr[0][1]
for i in range(3):
    if arr[i][1] < mins:
        mins=arr[i][1]
print("min element of the second column=",mins)
max_d= arr[0][0]
for i in range(3):
    if arr[i][i]>max_d:
        max_d= arr[i][i]
print("max element of the main diagonal=",max_d)


# ##### 
