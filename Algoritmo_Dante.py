#!/usr/bin/env python
# coding: utf-8

# In[9]:


def sumArea(arr):
    sumArea = 0
    for i in range(len(arr)):
        sumArea = sumArea + arr[i]
    return sumArea

def algoritmoDante(size, arrRec):
    arrOrd = arrRec.sort()
    areaT = size[0] * size[1]
    n = len(arrRec)
    bestWaste = sumArea(arrRec)
    def contorno(forma1, forma2):
        n1 = len(forma1)
        n2 = len(forma2)
        
    def paso(arr):
        sumArea = sumArea(arr)
        if areaT - sumArea == bestWaste:
            return arr
        


# In[ ]:





# In[ ]:




