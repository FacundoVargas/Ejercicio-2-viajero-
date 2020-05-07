# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 05:28:37 2020

@author: Luz Victoria
"""

import csv
import os

class viajeroFrecuente:
    __numero=0
    __DNI=0
    __nombre=""
    __apellio=""
    __millasAcum=0
    
    def __init__(self,numero,dni,nombre,apellido,millas):
        self.__numero=numero
        self.__DNI=dni 
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millasAcum=millas  
        
        
    def __str__(self):
        s=("{}"+"{}"+"{}"+"{}"+"{}").format(self.__numero,self.__DNI,self.__nombre,self.__apellido,self.__millasAcum)
        return s
        
    def cantidadTotaldeMillas(self):
        return self.__millasAcum
    
    
    def acumularMillas(self,millas):
        self.__millasAcum+=millas
        return self.__millasAcum
        
        
    def canjearMillas(self,millas):
        if (self.__millasAcum >= millas):
            print("Canje realizado con exito, Buen viaje")
        else:
            print("Sus millas son insuficientes para este canje")
            
    
    def getNumero(self):
        return self.__numero
    
    def getNombre(self):
        return self.__nombre
    
    
class manejadordeViajeros:
    
    def __init__(self):
        self.__listaViajeros=[]
        
    def __str__(self):
        s = ""
        for viaj in self.__listaViajeros:
            s += str(viaj) + '\n'
        return s
        
    def agregarViajero(self,viajero):
        self.__listaViajeros.append(viajero)
        
    def buscaViajero(self,nv):
        ban=True
        a=-1
        for i in self.__listaViajeros:
            if (i.getNumero() == nv):
                a=nv
        if (a==-1):
            print ("El numero ingresado no corresponde a ningun viajero")
            ban=False
        else:
            print ("Elija una opcion del menu señor {}".format(self.__listaViajeros[a-1].getNombre()))
        return (ban,self.__listaViajeros[a-1].cantidadTotaldeMillas(),a)
    
    
    def busca2(self,millas,num):        
        nuevasmillas=self.__listaViajeros[num].acumularMillas(millas)
        return nuevasmillas
    
    def busca3(self,millas,num):
        self.__listaViajeros[num].canjearMillas(millas)
    
        
    def cargarViajero(self):
        fila=[]
        archivo = open('viajeros.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            num=int(fila[0])            
            dni=int(fila[1])            
            nom=fila[2]            
            ape=fila[3]            
            mac=int(fila[4])
            unviajero=viajeroFrecuente(num,dni,nom,ape,mac)
            self.agregarViajero(unviajero)
        archivo.close()
        
    
def menu():
    os.system("cls")
    print ("Selecciona una opción")
    print ("\t1 - Consultar Cantidad de Millas")
    print ("\t2 - Acumular Millas")
    print ("\t3 - Canjear Millas")
    print ("\t0 - Salir")
    
    
if __name__== '__main__':

    mv = manejadordeViajeros()
    mv.cargarViajero()
    nv=int(input("Ingrese su numero de viajero para visualizar el menu: "))
    (a,b,c)=mv.buscaViajero(nv)
    if(a==True):
        while True:
            menu()
            opcionMenu = int(input("Ingrese un numero de opcion: "))
            if opcionMenu == 1:
                print("La cantidad total de millas que posee es: {}".format(b))
                input("Has pulsado la opción 1...\npulsa una tecla para continuar")
            elif opcionMenu == 2:
                m=int(input("Ingrese cantidad de millas para acumular: "))
                print("Su nueva cantidad de millas acumuladas es: {}".format(mv.busca2(m,c-1)))
                input("Has pulsado la opción 2...\npulsa una tecla para continuar")
            elif opcionMenu == 3:
                m=int(input("Ingrese cantidad de millas a canjear: "))
                mv.busca3(m,c-1)
                input("Has pulsado la opción 3...\npulsa una tecla para continuar")
            elif opcionMenu == 0:
                break
            else:
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

    
    
    
  
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

