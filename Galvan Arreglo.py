#Variable universal arreglo de rectangulos + dimensiones de la plancha
import matplotlib.pylab as plt
import random as rnd
class Rectangulo:
    def __init__(self,a,l,en,i):
        self.base = l
        self.alto = a
        self.n = en
        self.ids = i
ArrRect = [Rectangulo(rnd.randint(0,15),rnd.randint(0,30),rnd.randint(0,10),i) for i in range(5)] 

altura = 15
base = 30
arr=[[i+1 for i in range(base)] for _ in range(altura)]#matriz plancha

#Probaremos con esto ArrRect[0]
for i in range(ArrRect[0].alto):
    arr[i] = arr[i][ArrRect[0].base:]

print(arr)
print("")


rect = (6,2)
for i in range(rect[0]-1):
    if ArrRect[0].base <= len(arr[i]):
        if len(arr) >= i+1 == True and arr[i+1][0] != arr[i][0]:
            break
        else:
            arr[i] = arr[i][rect[1]:]

            
            
for i in range(len(ArrRect)):
    print("Rectangulo ",ArrRect[i].ids,":",ArrRect[i].base,ArrRect[i].alto,ArrRect[i].n)


    
    

