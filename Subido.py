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
def Dante():
    if(True):
        return
def Natalia(): 
    if(True):
        return
def Joaquin(): 
    if(True):
        return

menu()    
