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
    
    for i in range(n):
        AreaRecortes = arrRec[0][1] * arrRec[1][0]

        
    DesperdicioOptimo = AreaPlaca - AreaRecortes
        
    ##3. Ordenar arreglo de recortes por sus anchos
    sort(arrRec[0][1][0][0])
    
    ##4. Recortar placa
    for i in range(n):
        if arrRec[i] + arrRec[i + 1] == ancho:
            MayorAncho = 0
            
            if arrRec[i][0] > arr[i + 1]:
                MayorAncho = arr[i][0]
            
            else:
                MayorAncho = arr[i + 1][0]
            
            if PlacaSR == True:
                for i in range(largo):
                    for j in range(MayorAncho):
                        placa[i][j] = 1
                PlacaSR = False
                
            else:
                for i in range(largo):
                    for j in range(mayor):
                        if placa[i][j] == 0:
                            placa == 1
            
        
        else:
            ##Buscar suma más óptima
    
    Desperdicio = 0
    do{
    if DesperdicioOptimo < 0:
        Placas.append(InicializarMatriz(largo, ancho))
        ##Realizar los recortes en la siguiente placa
        
        ##Calcular el desperdicio
        for i in range(largo):
            for j in range(ancho):
                if placa[i][j] == 0:
                    desperdicio += 1
    
    else:
        break
    }while(Desperdicio >= 0)
    
    ##5. Calcular el desperdicio                
    DespPorcentaje = (desperdicio/AreaPlaca)*100
    
    ##6. Mostrar Resultados
    print("El desperdicio generado es: "+ desperdicio + " en metros")
    print("El desperdicio generado es: "+ DespPorcentaje + "%")
    print("Se utilizaron "+ Placas + " planchas")
    
 def InicializarMatriz(ancho, largo):
    for i in range(largo):
        for j in range(ancho):
            placa = [i][j]
    return placa

