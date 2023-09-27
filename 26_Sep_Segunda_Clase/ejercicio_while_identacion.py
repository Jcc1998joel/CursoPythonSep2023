# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:15:55 2023

@author: Admin
"""

while True:
    x=int(input('Enter a number to count to: '))
    print(x)
    if x == 'q' or x == 'quit':
        break
    
    x=int(input(x))
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break