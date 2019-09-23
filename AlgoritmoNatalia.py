#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Natalia(largo, ancho, arrRec, n):
    
    for i in range(largo):
        for j in range(ancho):
            placa[i][j] = 0
    
    arrAreas = [] ##area de los recortes
    arrIdRecortes = [] ##para identificar los recortes utilizados en la placa
    AreaPlaca = largo * ancho
    ContRecortes = 0
        
    for i in range(n):
        area = arrRec[0][1] * arrRec[1][0]
        arrAreas.append(area)
    
    ##Ordenar el arreglo de areas
    
    ##Ordenar arreglo de recortes
    
    ##Sumar el mayor de los recortes con el segundo mayor y comparar con el ancho de la placa
    for i in range(n):
        if arrRec[i] + arrRec[i + 1] == ancho:
            mayor = 0
            
            if arrRec[i][0] > arr[i + 1]:
                mayor = arr[i][0]
            
            else:
                mayor = arr[i + 1][0]
                
            for i in range(largo):
                for j in range(mayor):
                    placa[i][j] = 1
            
        
        else:
            ##Buscar suma más óptima
            LlenarMatriz()

