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
        placas = 2
        c = 0
        while(c <= 2):
            desperdicio = RecortarPlaca(arrRec, placa, largo, ancho, AreaPlaca, PlacaSR)
            VecDesperdicio.append(desperdicio)
            c += 1
    
    ##5. Calcular el desperdicio
    Desperdicios = 0
    for i in range(placas):
        Desperdicios += VecDesperdicio[i]
        
    DespPorcentaje = (Desperdicios/AreaPlaca * placas)*100
    
    ##6. Mostrar Resultados
    print("El desperdicio generado es: "+ Desperdicios + " en metros")
    print("El desperdicio generado es: "+ DespPorcentaje + "%")
    print("Se utilizaron "+ placas + " planchas")
    
 def InicializarMatriz(ancho, largo):
    for i in range(largo):
        for j in range(ancho):
            placa = [i][j]
    return placa

def RecortarPlaca(arrRec, placa, largo, ancho, AreaPlaca, PlacaSR):
    for i in range(n):
        if arrRec[i].ancho + arrRec[i + 1].ancho <= ancho && arrRec.largo + arrRec[i + 1].largo == largo:
            MayorAncho = 0
            MenorLargo = 0
            
            if arrRec[i].ancho > arr[i + 1].ancho:
                MayorAncho = arr[i].ancho
            
            if arrRec[i].ancho < arr[i + 1].ancho:
                MayorAncho = arr[i + 1].ancho
            
            if arrRec[i].largo < arr[i + 1].largo:
                MenorLargo = arrRec[i].largo
                
            else:
                MenorLargo = arrRec[i + 1].largo
            
            if PlacaSR == True:
                for i in range(largo):
                    for j in range(ancho):
                        placa[i][j] = 1
                PlacaSR = False
                
            else:
                i = largo - MenorLargo
                for i in range(largo):
                    for j in range(MayorAncho):
                        if placa[i][j] == 0:
                            placa == 1

    
    
    ##5. Calcular el desperdicio
    for i in range(largo):
        for j in range(ancho):
            if placa[i][j] == 0:
                desperdicio += 1
    
    return desperdicio
