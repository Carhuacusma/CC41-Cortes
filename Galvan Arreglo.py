#Variable universal arreglo de rectangulos + dimensiones de la plancha
import matplotlib.pylab as plt
import random as rnd
class Rectangulo:
    def __init__(self,a,l,en,i):
        self.base = l
        self.alto = a
        self.n = en
        self.ids = i
ArrRect = [Rectangulo(rnd.randint(1,4),rnd.randint(5,10),rnd.randint(0,10),i) for i in range(2)] 

altura = 15
base = 20
arr=[[i+1 for i in range(base)] for _ in range(altura)]#matriz plancha

#Probaremos con esto ArrRect[0]
"""""for i in range(ArrRect[0].alto):
    arr[i] = arr[i][ArrRect[0].base:]
    """""
    
def display(arr):
    for i in range(len(arr)):
        print(i+1,arr[i])

display(arr)
print("")
def work():
    for x in range(len(ArrRect)):  #Recore los diferentes rectangulos no considera la cantidad individual
        conty = 0
        for i in range(len(arr)): 
            if encaja(ArrRect[x],arr,i):
                aux = i
                for z in range(ArrRect[x].alto):
                    arr[i] = arr[i][ArrRect[x].base:]
                    i += 1
                break
            else:
                continue
            conty +=1
            
        print("\n",x+1,"\n")
        display(arr)
        print("")
    
    
for i in range(len(ArrRect)):
    print("Rectangulo ",ArrRect[i].ids,":","| base: ",ArrRect[i].base,"| Altura: ",ArrRect[i].alto,"| n: ",ArrRect[i].n)

def encaja(rect,plancha,y0):
    if len(plancha) < rect.alto:
        return False
    for i in range(rect.alto):
        if len(plancha[y0]) < rect.base:
            return False
        if len(plancha) - y0 > y0+1:
            if plancha[y0][0] != plancha[(y0+1)][0]:#ojo coordenadas
                return False
        y0 += 1
    
    return True
    


work()