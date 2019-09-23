#!/usr/bin/env python
# coding: utf-8

# In[32]:


def sumArea(arr): #recibe arr [(ancho, largo),(ancho, largo),(...),...]
    sumArea = 0
    for i in range(len(arr)):
        sumArea = sumArea + arr[i][0]* arr[i][1]
    return sumArea

def partition(arr,ini,fin): 
    i = ini-1                       # index of smaller element 
    pivot = arr[fin][0]*arr[fin][1]     # pivot como area
    
    for j in range(ini , fin): 
        if   (arr[j][0] * arr[j][1]) >= pivot: 
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 

    arr[i+1],arr[fin] = arr[fin],arr[i+1] 
    return i+1
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

def algoritmoDante(size, arrRec):
    ##arrRec es arreglo de tuplas ancho, largo
    n = len(arrRec)
    quickSort(arrRec, 0, n-1)
    # arrRec está ordenado de mayor a menor area
    areaT = size[0] * size[1]
    bestWaste = sumArea(arrRec)
    arrRes = []*n
    # (pos.x, pos.y), (ancho_x, largo_y)
    def paso(rec, j):
        # recibe uno de los recortes y la "posicion" del paso
        return
    paso(arrRec[0],0)


# In[30]:


ejemplo = [(5,5), (1,2), (2,3),(2,10)]
quickSort(ejemplo,0,3)
print(ejemplo)


# In[ ]:


with open('ejemplo.in') as f:
    for line in f:
         

