#!/usr/bin/env python
# coding: utf-8

# In[35]:


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
print("                               ")


rect = (6,2)
for i in range(rect[0]-1):
    if rect[0] <= len(arr[i]):
        if len(arr) >= i+1 and arr[i+1][0] != arr[i][0]:
            break
        else:
            arr[i] = arr[i][rect[1]:]

        
print(arr)

    
    
    

