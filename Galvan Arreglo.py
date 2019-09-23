#!/usr/bin/env python
# coding: utf-8

# In[22]:


def lenarr(arr):
    arrlen = []
    for x in range(len(arr)):
        arrlen.append(len(arr[x]))
    return arrlen
    
arr=[[1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10],

    ]
rect = (5,2)
for i in range(rect[0]):
    arr[i] = arr[i][rect[1]:]
print(arr)
    
    
    

