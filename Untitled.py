#!/usr/bin/env python
# coding: utf-8

# In[19]:


def menu():
    hola()
    largo = int(input("Ingrese el largo de la placa: "))
    ancho = int(input("Ingrese el ancho de la placa: "))
    n = int(input("Ingrese la cantidad de recortes diferentes que tendra: "))
    arrRec = []
    for i in range(n):
        print("Ingrese el largo y el ancho del recorte ", i + 1, " ")
        a = int(input("Ancho: ")) ##ancho.
        b = int(input("Largo: ")) ##largo
        arrRec.append((a,b))
    print(arrRec)
    print("Elija el algoritmo con el cuál se harán los recortes:")
    print("1 = Algoritmo Galván")
    print("2 = Algoritmo Moreno")
    print("3 = Algoritmo Maury")
    
    c = input("Algoritmo elejido: ") ##algoritmo elegido
    print(c)
    
def Dante():
def Natalia():
def Joaquin(): 
menu()    
    

