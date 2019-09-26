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
            
