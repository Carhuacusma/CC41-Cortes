#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Natalia(largo, ancho, arrRec, n):
    
    ##1. Crear e inicializar matriz
    placa = InicializarMatriz(ancho, largo)
    
    ##2. Crear variables necesarias
    AreaPlaca = largo * ancho
    AreaRecortes = 0
    ContRecortes = 0
    PlacaSR = True ##PlacaSR = Placa sin recortes
    n = len(arrRec)
    vecDesperdicio = []
    
    for i in range(n):
        AreaRecortes = arrRec[i].base * ArrRec[i].alto

        
    DesperdicioOptimo = AreaPlaca - AreaRecortes
        
    ##3. Ordenar arreglo de recortes por sus anchos
    InsertionSort(arrRec, n)
    
    ##4. Recortar placa
    if DesperdicioOptimo >= 0:
        placas = 1
        desperdicio = RecortarPlaca(arrRec, placa, largo, ancho, AreaPlaca, PlacaSR)
    
    else:
        mod = AreaRecortes % AreaPlaca
        if mod == 0:
            placas = AreaRecortes / AreaPlaca
            
        else:
            placas = (AreaRecortes / AreaPlaca) + 1
        
        c = 0
        while(c <= placas):
            placa = InicializarMatriz(ancho, largo)
            desperdicio = RecortarPlaca(arrRec, placa, largo, ancho, AreaPlaca, PlacaSR)
            VecDesperdicio.append(desperdicio)
            c += 1    
    
    ##5. Calcular el desperdicio
    Desperdicios = 0
    for i in range(placas):
        Desperdicios += VecDesperdicio[i]
        
    DespPorcentaje = (Desperdicios/AreaPlaca * placas)*100
    
    ##6. Mostrar Resultados
    print("El desperdicio generado es: " + Desperdicios + " en metros")
    print("El desperdicio generado es: " + DespPorcentaje + "%")
    print("Se utilizaron " + placas + " planchas")

    
 def InicializarMatriz(ancho, largo):
    for i in range(largo):
        for j in range(ancho):
            placa = [i][j]
    return placa

def RecortarPlaca(arrRec, placa, largo, ancho, AreaPlaca, PlacaSR):
    ##4. Recortar placa
    if PlacaSR == True:
        largo = arrRec[0].base
        ancho = arrRec[0].alto
        Recortar(placa, largo, ancho)
    
    else:
        for i in range(n):
            for j in range(n):
                if arrRec[i].base + arrRec[j].base == largo and arrRec[i].alto + arrRec[j].alto <= ancho:
                    Recortar(placa, largo, arrRec[i].alto)
                    Recortar(placa, largo, arrRec[j].alto)
                    
            
                if arrRec[i].alto + arr[j].alto == ancho and arrRec[i].base + arrRec[j].base <= largo:
                    Recortar(placa, arrRec[i].base, ancho)
                    Recortar(placa, arrRec[j].base, ancho)
            
            
                if arrRec[i].alto + arrRec[j].alto <= ancho and arrRec[i].base + arrRec[j].base <= largo:
                    Recortar(placa, arrRec[i].base, arrRec[i].alto)
                    Recortar(placa, arrRec[j].base, arrRec[j].alto)
    
    
    ##5. Calcular el desperdicio
    for i in range(largo):
        for j in range(ancho):
            if placa[i][j] == 0:
                desperdicio += 1
    
    return desperdicio

def Recortar(placa, largo, ancho):
    for i in range(largo):
        for j in range(ancho):
            if placa[i][j] == 0
                placa[i][j] = 1
                
def InsertionSort(arrRec, n):
    for i in range(n):
        j = i
        aux = arrRec[i].base
        while j > 0 and arrRec[j - 1].base < aux:
            arrRec[j].base = arrRec[j - 1].base
            j -= 1
        if j != i:
            arrRec[j].base = aux
