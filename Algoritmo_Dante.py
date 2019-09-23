#!/usr/bin/env python
# coding: utf-8

# In[2]:


##input
largo = int(input("Largo (x):"))
ancho = int(input("Ancho (y):"))
n = int(input("Numero de piezas:"))
print("Tamaños separados por comas")
arr = []
for i in range(n):
    aux = input()
    lista = aux.split(',')
    lista[0] = int(lista[0])
    lista[1] = int(lista[1])
    tupla = lista[0], lista[1]
    arr.append(tupla)


# In[5]:


def sumArea(arr): #recibe arr [(ancho, largo),(ancho, largo),(...),...]
    sumArea = 0
    for i in range(len(arr)):
        sumArea = sumArea + arr[i][0]* arr[i][1]
    return sumArea

# ------------Quick Sort modificado--------------
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
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
# ------------Quick Sort modificado--------------
        
def algoritmoDante(size, arrRec):
    # arrRec es arreglo de tuplas ancho, largo, ""posibilidad de un ID.
    # size es ancho, largo
    n = len(arrRec)
    quickSort(arrRec, 0, n-1)
    # arrRec está ordenado de mayor a menor area
    areaT = size[0] * size[1]
    bestWaste = sumArea(arrRec)
    arrRes = []
    # [[(pos.x, pos.y), (ancho_x, largo_y)], [(pos2.x,pos2.y),(ancho2,largo2)], ...]
    girado = [False]*n
    def paso(rec, j, forma):
        # recibe uno de los recortes, la "iteracion" del paso, y la forma que está cortada
        arrAreaCut = []
        for aux in forma:
            arrAreaCut.append(aux[1])
        sumAreaCut = sumArea(arrAreaCut)
    #forma = []
    ##empezar con el recorte de mayor area en la esquina
    #paso(arrRec[0],0, forma)
ejemplo = []
#ejemplo.sort()
print(len(ejemplo))
for ej in ejemplo:
    print("hai")
print(sumArea(ejemplo))


# In[3]:





# In[ ]:


aux = [(0,0),(6,0),(6,2),(4,2),(4,3),(5,3),(5,6),(0,6)]
def 

