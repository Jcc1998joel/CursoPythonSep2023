# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:36:58 2023

@author: franc
"""

import statistics
def estadisticas_descriptivas(arreglo):
    promedio=statistics.mean(arreglo)
    mediana=statistics.median(arreglo)
    varianza=statistics.variance(arreglo)
    desviacion_estandar=statistics.stdev(arreglo)
    maximo=max(arreglo)
    minimo=min(arreglo)
    
    estadisticas={
        "Promedio":promedio,
        "Mediana": mediana,
        "Varianza": varianza,
        "Desviación estándar":desviacion_estandar,
        "Máximo":maximo,
        "Minimo":minimo,
    }
    return estadisticas

def imprimir_estadisticas(nombre,arreglo):
    estadisticas=estadisticas_descriptivas(arreglo)
    print(f"Estadisticas para {nombre}: ")
    for key, value in estadisticas.items():
        print(f"{key}:{value}")
nombres=['Datos A','Datos B']
datos=[[10,32,43,64,85],[11,23,35,47,54]]
for i in range(len(nombres)):
    imprimir_estadisticas(nombres[i], datos[i])