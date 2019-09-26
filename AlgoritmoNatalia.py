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
        AreaRecortes = arrRec[i].largo * ArrRec[i].ancho

        
    DesperdicioOptimo = AreaPlaca - AreaRecortes
        
    ##3. Ordenar arreglo de recortes por sus anchos
    arrRec.Largo.sort(reverse = True)
    
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
        largo = arrRec[0].largo
        ancho = arrRec[0].ancho
        i, j = 0
        Recortar(i, j, placa, largo, ancho)
    
    else:
        for i in range(n):
            for j in range(n):
                if arrRec[i].largo + arr.Rec[j] == largo && arrRec[i].ancho + arrRec[j].ancho <= ancho:
                    anchos = arrRec[i].ancho + arrRec[j].ancho
                    Recortar()
            
                if arrRec[i].ancho + arr[j].ancho == ancho && arrRec[i].largo + arrRec[j].largo <= largo:
                    largos = arrRec[i].largo + arrRec[j].largo
                    Recortar()
            
                if arrRec[i].largo + arrRec[j].largo <= largo && arrRec[i].ancho + arrRec[j].ancho <= ancho:
            
                    Recortar()
            
                if arrRec[i].ancho + arrRec[j].ancho <= ancho && arrRec[i].largo + arrRec[j].largo <= largo:
            
                    Recortar()
    
    
    ##5. Calcular el desperdicio
    for i in range(largo):
        for j in range(ancho):
            if placa[i][j] == 0:
                desperdicio += 1
    
    return desperdicio

def Recortar(i, j, placa, largo, ancho):
    for i in range(largo):
        for j in range(ancho):
            placa[i][j] = 1
    
