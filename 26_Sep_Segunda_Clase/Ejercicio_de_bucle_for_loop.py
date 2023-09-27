# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:51:38 2023

@author: Admin
"""
listaR=[]
listaS=[]
listaV=[]
lista= ["R1", "R2", "R3", "R4",
        "S1", "S2", "S3", "S4", "S5",
        "AP1", "OLT1", "IoT1"]
#print(lista[0])
for item in lista:
    if "R" in item:
        listaR.append(item)
    elif "S" in item:
        listaS.append(item)
    else:
        listaV.append(item)
print(listaR)
print(listaS)
print(listaV)