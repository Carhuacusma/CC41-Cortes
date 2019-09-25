#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Rectangulo:
    def __init__(self,l,a,en,i):
        self.largo = l
        self.ancho = a
        self.n = en
        self.ids = i

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


# In[39]:


def sumArea(arr): #recibe arr [(ancho, largo),(ancho, largo),(...),...]
    sumArea = 0
    for elem in arr:
        sumArea = sumArea + elem[0]* elem[1]
    return sumArea

def chocan(rec1, rec2):
    # rec : [(pos.x,pos.y),(size.x,size.y)]
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
        if nPlanchas == 1:
            arrAreaCut = []
            for aux in forma:
                arrAreaCut.append(aux[1])
            sumAreaCut = sumArea(arrAreaCut)
            if sumAreaCut == bestWaste and len(forma) == n:
                return True
        elif nP == nPlanchas and len(forma) == n:
            return True
        ##---------------------------------------------------------------
        
        ##posicionar rec en forma:
        newX = 0
        newY = 0
        acomodado = False
        print("forma:")
        print(forma)
        def auxPosicion(newRec):
            forma.append(newRec)
            if j < n - 1:
                print("analizando la forma siguiente:")
                if paso(arrRec[j+1],j+1,nP):
                    #si sale bien:
                    print("agregando")
                    arrRes[j] = newRec
                    return True
            elif j == n - 1:
                print("Ultima forma:")
                if newRec[0][0] + newRec[1][0] <= nP*sizeP[0] and newRec[0][1] + newRec[1][1] <= nP*sizeP[1]:
                    print("Entra")
                    arrRes[j] = newRec
                    return True
            forma.pop(len(forma) - 1)
            print("regresando")
            print(forma)
            return False
        
        auxIt = 0
        for aux in forma:
            newRecForma = [(newX,newY),(rec[0],rec[1])]
            if chocan(newRecForma,aux):
                # probar por ancho
                newX = aux[1][0] + aux[0][0]
                print("Aux de Forma:")
                print(aux)
                if newX + rec[0] <= nP*sizeP[0] and not acomodado:
                    #SI PUEDE ENTRAR EN LA PLANCHA
                    print("probar ancho")
                    print((newX,newY))
                    newRecForma = [(newX,newY),rec]
                    if auxIt < len(forma) - 1:
                        if not chocan(newRecForma,forma[auxIt + 1]):
                            print("no choca con el sgte")
                            acomodado = auxPosicion(newRecForma)
                # esquina inferior derecha
                newY = aux[1][1] + aux[0][1]
                if not acomodado and newY + rec[1] <= nP*sizeP[1] and newX + rec[0] <= nP*sizeP[0]:
                    print("probar en la esquina")
                    print((newX,newY))
                    newRecForma = [(newX,newY),rec]
                    if auxIt < len(forma) - 1:
                        if not chocan(newRecForma,forma[auxIt + 1]):
                            acomodado = auxPosicion(newRecForma)
                #quitar x para ir abajo
                newX = aux[1][0]
                if not acomodado and newY + rec[1] <= nP*sizeP[1]:
                    print("probar abajo")
                    print((newX,newY))
                    newRecForma = [(newX,newY),rec]
                    if auxIt < len(forma) - 1:
                        if not chocan(newRecForma,forma[auxIt + 1]):
                            acomodado = auxPosicion(newRecForma)
            auxIt = auxIt + 1
        newRecForma = [(newX,newY),rec]
        if acomodado:
            print("acomodado after for")
            print(forma)
            arrRes[j] = newRecForma
            return True
        return auxPosicion(newRecForma)
        # paso(arrRec[j+1], j + 1, forma)
        ##--->girar si es necesario------------TO DO !!!!!!!!!!!!!!!!!!!!!!
        
    ##empezar con el recorte de mayor area en la esquina
    paso(arrRec[0],0,1)
    print(arrRes)
    return arrRes


ejemplo = [(2,3,'A'),(2,2,'B'),(2,1,'C')]
plancha = (6,3)
algoritmoDante(plancha,ejemplo)


# In[4]:


arr = [0]*5
arr[1] = (2,5)
print(arr)


# In[6]:


aux = 0
asmr = aux < 5 and aux > 3
print(asmr)
asmr = asmr or aux == 0
print(asmr)


# In[ ]:




