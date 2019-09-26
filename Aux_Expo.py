#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### class Rectangulo:
    pos = (0,0)
    def __init__(self,a,l,en,i,x,y):
        self.base = l
        self.alto = a
        self.n = en
        self.ids = i
        self.pos = (x,y)    
        self.arrhijos = []
        self.horientacion = "N"
        self.visited = False
        self.tabla = 0
        if en > 1:
            for i in range(en):
                self.arrhijos.append(Rectangulo(a,l,0,i,0,0))
                                     
def menu():
    largo = int(input("Ingrese el largo de la placa: "))
    ancho = int(input("Ingrese el ancho de la placa: "))
    n = int(input("Ingrese la cantidad de recortes diferentes que tendra: "))
    arrRec = []*n
    for i in range(n):
        print("Ingrese el largo y el ancho del recorte ", i + 1, ": ")
        a = int(input("Ancho: ")) ##ancho.
        b = int(input("Largo: ")) ##largo
        en = int(input("Cantidad piezas: "))
        arrRec.append(Rectangulo(b,a,en,i,0,0))
    print(arrRec[0].base)
    print("Elija el algoritmo con el cuál se harán los recortes:")
    print("1 = Algoritmo Galván")
    print("2 = Algoritmo Moreno")
    print("3 = Algoritmo Maury")
    c = input("Algoritmo elejido: ") ##algoritmo elegido
    print(c)
    if c == "1":
        Joaquin()
    elif c == "2": 
        Dante(largo,ancho,arrRec)
    elif c == "3":
        Natalia(largo,ancho,arrRec,n)
    #TO DO----------------DEFINIR FUNCIONES POR ALGORITMO
        
def Dante(largo, ancho, arrRec):
    sizePlancha = (largo, ancho)
    arrTraduc = []
    charId = 0
    def retornaId(idc):
        if idc < 26:
            idc = idc + 65
            return chr(idc)
        else:
            aux = idc // 26
            res = idc - aux*26
            for i in range(1,aux):
                charAux = idc - i*26
                charAux = charAux % 26
                res = res + chr(charAux)
            return res
    for elemento in arrRec:
        trueId = retornaId(charId)
        arrTraduc.append([(elemento.base,elemento.alto, trueId)])
        for hijo in elemento.arrhijos:
            charId = charId + 1
            trueId = retornaId(charId)
            arrTraduc.append([(hijo.base,hijo.alto, trueId)])
        charId = charId + 1
    print(arrTraduc)
    return algoritmoDante(sizePlancha, arrTraduc)
def Joaquin(): 
    if(True):
        return

    
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
    placa = [[0] * largo] * ancho
    for i in range(largo):
        for j in range(ancho):
            placa[i][j] = 0
    return placa

def RecortarPlaca(arrRec, placa, largo, ancho, AreaPlaca, PlacaSR):
    ##4. Recortar placa
    vecRU = []
    
    if PlacaSR == True:
        largo = arrRec[0].base
        ancho = arrRec[0].alto
        Recortar(placa, largo, ancho)
        vecRU.append(arrRec[0])
    
    else:
        j = 1
        for i in range(n):
            for j in range(n):
                if vecRU[i].base + arrRec[j].base == largo and vecRU[i].alto + arrRec[j].alto <= ancho:
                    Recortar(placa, largo, arrRec[i].alto)
                    Recortar(placa, largo, arrRec[j].alto)
                    vecRU.append(arrRec[i])
                    vecRU.append(arrRec[j])
                    arrRec.pop(i)
            
                if vecRU[i].alto + arr[j].alto == ancho and vecRU[i].base + arrRec[j].base <= largo:
                    Recortar(placa, arrRec[i].base, ancho)
                    Recortar(placa, arrRec[j].base, ancho)
                    vecRU.append(arrRec[i])
                    vecRU.append(arrRec[j])
                    arrRec.pop(i)
            
            
                if vecRU[i].alto + arrRec[j].alto <= ancho and vecRU[i].base + arrRec[j].base <= largo:
                    Recortar(placa, arrRec[i].base, arrRec[i].alto)
                    Recortar(placa, arrRec[j].base, arrRec[j].alto)
                    vecRU.append(arrRec[i])
                    vecRU.append(arrRec[j])
                    arrRec.pop(i)
    
    
    ##5. Calcular el desperdicio
    for i in range(largo):
        for j in range(ancho):
            if placa[i][j] == 0:
                desperdicio += 1
    
    return desperdicio

def Recortar(placa, largo, ancho):
    for i in range(largo):
        for j in range(ancho):
            if placa[i][j] == 0:
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
    
menu()


# In[ ]:


#Variable universal arreglo de rectangulos + dimensiones de la plancha
import matplotlib.pylab as plt
import random as rnd


class Rectangulo:
    pos = (0,0)
    def __init__(self,a,l,en,i,x,y):
        self.base = l
        self.alto = a
        self.n = en
        self.ids = i
        self.pos = (x,y)    
        self.arrhijos = []
        self.horientacion = "N"
        self.visited = False
        self.tabla = 0
        if en > 1:
            for i in range(en):
                self.arrhijos.append(Rectangulo(a,l,0,i,0,0))

ArrRect = [Rectangulo(rnd.randint(4,4),rnd.randint(5,10),2,i,0,0) for i in range(5)] 

altura = 15
base = 20
arrM = [[i+1 for i in range(base)] for _ in range(altura)]#matriz plancha
ArrArr = [arrM]
contTabla = 0
def display(arr):
    for i in range(len(arr)):
        print(i+1,arr[i])

display(arrM)
print("")
def work(arr,contT):
    for x in range(len(ArrRect)):  #Recore los diferentes rectangulos no considera la cantidad individual
        if ArrRect[x].visited == True:
           # print("\n","Rectangulo",x,"\n")
            continue
        for j in range(len(ArrRect[x].arrhijos)+1): 
            if j > 0 and ArrRect[x].arrhijos[j-1].visited == True:
                continue
            for i in range(len(arr)): 
                if encaja(ArrRect[x],arr,i):
                    aux = i
                    for z in range(ArrRect[x].alto):
                        arr[i] = arr[i][ArrRect[x].base:]
                        i += 1 #muy util
                        if j == 0:
                            ArrRect[x].pos = (i, arr[i][0])
                            ArrRect[x].visited = True
                            ArrRect[x].tabla = contT


                        else:
                            ArrRect[x].arrhijos[(j-1)].pos = (i, arr[i][0])
                            ArrRect[x].arrhijos[(j-1)].visited = True
                            ArrRect[x].arrhijos[(j-1)].tabla = contT


                    ##i = aux
                    break
                voltear(ArrRect[x])
                if encaja(ArrRect[x],arr,i):
                    for z in range(ArrRect[x].alto):
                        arr[i] = arr[i][ArrRect[x].base:]
                        i += 1 #muy util
                        if j == 0:
                            ArrRect[x].pos = (i, arr[i][0])
                            ArrRect[x].visited = True                            
                            ArrRect[x].tabla = contT
                        else:
                            ArrRect[x].arrhijos[(j-1)].pos = (i, arr[i][0])
                            ArrRect[x].arrhijos[(j-1)].visited = True
                            ArrRect[x].arrhijos[(j-1)].tabla = contT


                        ##i = aux
                    break
                else:
                    for ar in range(len(ArrArr)):
                        if encaja(ArrRect[x],ArrArr[ar],i):
                            work(ArrArr[ar],ar)
                            break
                        voltear(ArrRect[x])
                        if encaja(ArrRect[x],ArrArr[ar],i):
                            work(ArrArr[ar],ar)
                        else:
                            ArrArr.append([[i+1 for i in range(base)] for _ in range(altura)])
                            ##contT += 1 no lo se rick
                        ##work(ArrArr[1])
            
            """"print("\n","Número", x,".",j,"\n")
            display(arr)
            input()
            print("")"""


    
for i in range(len(ArrRect)):
    print("Rectangulo ",ArrRect[i].ids,":","| base: ",ArrRect[i].base,"| Altura: ",ArrRect[i].alto,"| n: ",ArrRect[i].n)

def encaja(rect,plancha,y0):
    if len(plancha) < rect.alto or len(plancha) < y0:
        return False
    for i in range(rect.alto):
        if len(plancha[y0]) < rect.base:
            return False
        if len(plancha) - y0 > y0+1 and len(plancha[(y0+1)]) >0:
            if y0 == rect.alto:
                return True
            if plancha[y0][0] != plancha[(y0+1)][0]:#ojo coordenadas
                return False
        if y0+1 <= (len(plancha)-1):
            y0 += 1
        else:
            return False
    
    return True
    
def voltear(rec):
    AuxBase = rec.base
    rec.base = rec.alto
    rec.alto = AuxBase
    rec.horientazion = "I"

##work(arrM,contTabla)
for i in range(len(ArrRect)):
    print(ArrRect[i].visited)
    if len(ArrRect[i].arrhijos) > 0:
        for x in range(len(ArrRect[i].arrhijos)):
            print(ArrRect[i].arrhijos[x].visited)

grafico = [[i+1 for i in range(base)] for _ in range(altura)]#matrices de dibujo
graficos = []
for i in range(len(ArrRect)):
    graficos.append(grafico)
    
def graphcito():
    for a in range(len(ArrRect)):
        for h in range(len(ArrRect[a].arrhijos)+1): 
            if h == 0:
                for y in range(ArrRect[a].alto):
                    for x in range(ArrRect[a].base):
                        graficos[ArrRect[a].tabla][ArrRect[a].pos[1]+y][ArrRect[a].pos[0]+x] = h+a
            else:
                for y in range(ArrRect[a].arrhijos[h-1].alto):
                    for x in range(ArrRect[a].arrhijos[h-1].base):
                        graficos[ArrRect[a].arrhijos[h-1].tabla][ArrRect[a].arrhijos[h-1].pos[1]+y][ArrRect[a].arrhijos[h-1].pos[0]+x] = h+a

graphcito()
for c in range(len(graficos)):                        
    plt.imshow(graficos[c])           


print("end")


# In[7]:


##LO COMENTADO ES UNA VERSION PREVIA QUE FUNCIONA CON DOS ARREGLOS Y ORDENA RARO CON 3 (no he probado más)


def sumArea(arr): #recibe arr [(ancho, largo),(ancho, largo),(...),...]
    sumArea = 0
    for elem in arr:
        sumArea = sumArea + elem[0]* elem[1]
    return sumArea

def chocan(rec1, rec2):
    # rec : [(pos.x,pos.y),(size.x,size.y)]
    print("chocan?")
    print(rec1)
    print(rec2)
    aux = False
    if rec1[0][0] >= rec2[0][0] and rec1[0][0] <= rec2[0][0] + rec2[1][0]:
        ## si pos.x está dentro del rango de x de rec2
        # comprobar los y
        # esquina origen pos (superior izquierda)
        aux = rec1[0][1] >= rec2[0][1] and rec1[0][1] <= rec2[0][1] + rec2[1][1] 
        # esquina inferior izquierda
        aux = aux or (rec1[0][1] + rec1[1][1] >= rec2[0][1] and rec1[0][1] + rec1[1][1] <= rec2[0][1] + rec2[1][1])
        if aux:
            return True
    if rec1[0][0] + rec1[1][0] >= rec2[0][0] and rec1[0][0] + rec1[1][0] <= rec2[0][0] + rec2[1][0]:
        ## si el limite x está en el rango de x de rec 2
        # comprobar los y
        # esquina superior derecha
        aux = rec1[0][1] >= rec2[0][1] and rec1[0][1] <= rec2[0][1] + rec2[1][1]
        aux = aux or (rec1[0][1] + rec1[1][1] >= rec2[0][1] and rec1[0][1] + rec1[1][1] <= rec2[0][1] + rec2[1][1])
        if aux:
            return True
    return aux

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



def algoritmoDante(sizeP, arrRec):
    # arrRec es arreglo de tuplas ancho, largo, ""posibilidad de un ID.
    # size es ancho, largo
    n = len(arrRec)
    quickSort(arrRec, 0, n-1)
    # arrRec está ordenado de mayor a menor area
    
    #------definir el minimo desecho o cuantas planchas usar------
    areaT = sizeP[0] * sizeP[1]
    bestWaste = sumArea(arrRec)
    nPlanchas = 1
    if areaT >= bestWaste:
        bestWaste = areaT - bestWaste
    else:
        nPlanchas = bestWaste//areaT #para que sea entero //
        
    #-------------------------------------------------------------
    
    arrRes = [0]*n
    forma = []
    # [[(pos.x, pos.y), (ancho_x, largo_y)], [(pos2.x,pos2.y),(ancho2,largo2)], ...]
    girado = [False]*n
    # girado ordenado según los ids
    def paso(rec, j, nP):
        # recibe uno de los recortes, la "iteracion" del paso, 
        # el numero de Plancha en que trabaja, y la forma que está cortada
        
        ##----- comprobar si está en alguno de los estados finales
        #if j == n:
        #    return False
        print("iteracion:")
        print(j)
        arrAreaCut = []
        for aux in forma:
            arrAreaCut.append(aux[1])
        sumAreaCut = sumArea(arrAreaCut)
        areaT = nP*sizeP[0]*sizeP[1]
        if nPlanchas == 1:
            if sumAreaCut - areaT == bestWaste and len(forma) == n:
                return True
        elif nP == nPlanchas and len(forma) == n:
            return True
        ##---------------------------------------------------------------
        
        # --------------------------------FUNCIONES AUXILIARES---------------------------------------
        def entra(rec):
            print("Entra")
            return rec[0][0] + rec[1][0] <= nP*sizeP[0] and rec[0][1] + rec[1][1] <= nP*sizeP[1]
        
        def agregar(newRec):
            print("Agregando")
            print(newRec)
            forma.append(newRec)
            arrRes[j] = newRec
            return True
        # ------------------------------------------------------------------------------------------
        
        def auxPosicion(newRec):
            forma.append(newRec)
            print("auxPosicion:")
            print(forma)
            if j < n - 1:
                print("analizando la forma siguiente:")
                if paso(arrRec[j+1],j+1,nP):
                    #si sale bien:
                    return agregar(newRec)
            elif j == n - 1:
                print("Ultima forma:")
                if entra(newRec):
                    return agregar(newRec)
            forma.pop(len(forma) - 1)
            print("regresando")
            print(forma)
            return False
        
        # ------------------------------------------------------------------------------------------
        
        ##posicionar rec en forma:
        newX = 0
        newY = 0
        acomodado = False
        newRec = [(newX,newY), rec]
        print("forma:")
        print(forma)
        for recF in forma:
            if acomodado: 
                break
            if chocan(newRec, recF):
                # mover a la derecha:
                newX = recF[0][0] + recF[1][0]
                newRec = [(newX, newY), newRec[1]]
                print("posiciona a la derecha:")
                print(newRec)
                if entra(newRec) and not acomodado:
                    print("Entra a la derecha")
                    acomodado = auxPosicion(newRec)
                    #comprueba el siguiente
                # mover izquierda:
                newY = recF[0][1] + recF[1][1]
                newRec = [(newX, newY), newRec[1]]
                print("posiciona en la esquina:")
                print(newRec)
                if entra(newRec) and not acomodado:
                    print("Entra en la esquina")
                    acomodado = auxPosicion(newRec)
                #mover abajo
                newX = recF[0][0]
                print("posiciona abajo")
                if entra(newRec) and not acomodado:
                    print("Entra abajo")
                    acomodado = auxPosicion(newRec)
            #si no chocan:
            acomodado = auxPosicion(newRec)
        #despues de pasar por todo lo recortado:
        if entra(newRec):
            ## ejem: el primer corte
            acomodado = agregar(newRec)
        else:
            nP = nP + 1
            areaT = areaT*nP
            return False
        if j < n - 1:
            paso(arrRec[j+1],j+1,nP)
        #for aux in forma:
        #    if chocan(newRecForma,aux):
        #        newX = aux[0][0] + aux[1][0]
        #        # posicionarte a la derecha
        #        print("Aux de Forma:")
        #        print(aux)
        #        if newX + rec[0] <= nP*sizeP[0] and not acomodado:
        #            #SI PUEDE ENTRAR EN LA PLANCHA y no está acomodado
        #            print("probar ancho")
        #            print((newX,newY))
        #            newRecForma = [(newX,newY),rec]
        #            print(newRecForma)
        #            #if auxIt < len(forma) - 1:
        #            #    # para que no de errores
        #            #    if not chocan(newRecForma,forma[auxIt + 1]):
        #            #        print("no choca con el sgte")
        #            #        acomodado = auxPosicion(newRecForma)
        #            #else:
        #            #    acomodado = auxPosicion(newRecForma)
        #            #intentar acomodar al siguiente (retorna si se logró)
        #            acomodado = auxPosicion(newRecForma)
        #        # esquina inferior derecha
        #        newY = aux[1][1] + aux[0][1]
        #        print((newX,newY))
        #        if not acomodado and newY + rec[1] <= nP*sizeP[1] and newX + rec[0] <= nP*sizeP[0]:
        #            # si puede entrar en la plancha y aun no fue acomodado
        #            print("probar en la esquina")
        #            print((newX,newY))
        #            newRecForma = [(newX,newY),rec]
        #            if auxIt < len(forma) - 1:
        #                if not chocan(newRecForma,forma[auxIt + 1]):
        #                    acomodado = auxPosicion(newRecForma)
        #            else:
        #                acomodado = auxPosicion(newRecForma)
        #        #quitar x para ir abajo
        #        newX = aux[0][0]
        #        print((newX,newY))
        #        if not acomodado and newY + rec[1] <= nP*sizeP[1]:
        #            print("probar abajo")
        #            print((newX,newY))
        #            newRecForma = [(newX,newY),rec]
        #            if auxIt < len(forma) - 1:
        #                if not chocan(newRecForma,forma[auxIt + 1]):
        #                    acomodado = auxPosicion(newRecForma)
        #            else:
        #                acomodado = auxPosicion(newRecForma)
        #    auxIt = auxIt + 1
        # paso(arrRec[j+1], j + 1, forma)
        ##--->girar si es necesario------------TO DO !!!!!!!!!!!!!!!!!!!!!!
        
    ##empezar con el recorte de mayor area en la esquina
    paso(arrRec[0],0,1)
    ##arrRes = forma
    print(arrRes)
    return arrRes


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
    vecRU = []
    
    if PlacaSR == True:
        largo = arrRec[0].base
        ancho = arrRec[0].alto
        Recortar(placa, largo, ancho)
        vecRU.append(arrRec[0])
    
    else:
        j = 1
        for i in range(n):
            for j in range(n):
                if vecRU[i].base + arrRec[j].base == largo and vecRU[i].alto + arrRec[j].alto <= ancho:
                    Recortar(placa, largo, arrRec[i].alto)
                    Recortar(placa, largo, arrRec[j].alto)
                    vecRU.append(arrRec[i])
                    vecRU.append(arrRec[j])
                    arrRec.pop(i)
            
                if vecRU[i].alto + arr[j].alto == ancho and vecRU[i].base + arrRec[j].base <= largo:
                    Recortar(placa, arrRec[i].base, ancho)
                    Recortar(placa, arrRec[j].base, ancho)
                    vecRU.append(arrRec[i])
                    vecRU.append(arrRec[j])
                    arrRec.pop(i)
            
            
                if vecRU[i].alto + arrRec[j].alto <= ancho and vecRU[i].base + arrRec[j].base <= largo:
                    Recortar(placa, arrRec[i].base, arrRec[i].alto)
                    Recortar(placa, arrRec[j].base, arrRec[j].alto)
                    vecRU.append(arrRec[i])
                    vecRU.append(arrRec[j])
                    arrRec.pop(i)
    
    
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


# In[ ]:




