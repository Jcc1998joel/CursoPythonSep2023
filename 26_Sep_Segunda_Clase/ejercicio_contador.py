# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:55:28 2023

@author: Admin
"""

contar=int(input("Ingrese el # a contar:"))
contador=2
while True:
    print(contador)
    #contador+=1
    contador=contador+2 #Acumulador es necesario adaptar el numero dependiendo al bucle 
    if contador>contar:
        break