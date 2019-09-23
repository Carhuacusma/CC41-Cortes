#!/usr/bin/env python
# coding: utf-8

# In[25]:


def sumArea(arr):
    sumArea = 0
    for i in range(len(arr)):
        sumArea = sumArea + arr[i][0]
    return sumArea

def partition(arr,ini,fin): 
    i = ini-1                       # index of smaller element 
    pivot = arr[fin][0]*arr[fin][1]     # pivot como area
    
    for j in range(ini , fin): 
        if   (arr[j][0] * arr[j][1]) <= pivot: 
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 

    arr[i+1],arr[fin] = arr[fin],arr[i+1] 
    return i+1
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 


def algoritmoDante(size, arrRec):
    ##arrRec es arreglo de tuplas ancho, largo
    n = len(arrRec)
    quickSort(arrRec, 0, n-1)
    areaT = size[0] * size[1]
    bestWaste = sumArea(arrRec)
    arrRes = []*n
    arrPos = []*n
    def contorno(forma1, forma2):
        n1 = len(forma1)
        n2 = len(forma2)
        
    def paso(rec, arr, it):
        ##something
        
        return


# In[28]:


ejemplo = [(5,5), (1,2), (2,3),(2,10)]
quickSort(ejemplo,0,3)
print(ejemplo)


# In[ ]:


with open('ejemplo.in') as f:
    for line in f:
         

