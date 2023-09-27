# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:37:36 2023

@author: franc
"""
import random as rd
import math as mt
def calcular_promedio(arreglo):
    suma=0
    for numero in arreglo:
        suma += numero
    return suma/len(arreglo)
def clasificar_puntuaciones(arreglo):
    promedio=calcular_promedio(arreglo)
    if promedio >=90:
        return 'A'
    elif promedio >=80:
        return 'B'
    elif promedio >= 70:
        return 'C'
    elif promedio >= 60:
        return 'D'
    elif promedio >= 20:
        return 'E'
    else:
        return 'F'
    
arreglo=[rd.randint(0,200) for _ in range (10)]
letra_intervalo=clasificar_puntuaciones(arreglo)
print(letra_intervalo)
