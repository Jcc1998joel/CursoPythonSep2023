# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:30:06 2023

@author: Admin
"""

acl=int(input("Ingrese el valor de ACL:"))
if acl >=1 and acl <=99:
    print("Es un ACL Estandar")
elif acl >=100 and acl <=199:
    print("Es un ACL Extendida")
else:
    print("El valor ingresado no es un ACL")