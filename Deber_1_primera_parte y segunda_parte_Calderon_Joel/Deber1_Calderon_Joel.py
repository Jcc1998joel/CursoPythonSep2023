# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:41:23 2023

@author: Joel Alexander Calderón Cruz
"""

#Ejecutar cada ejercicio
#Primera parte: uso de PEMDAS en Python vs el uso de calculadora

### EJERCICIO 1 ###
a=int(input('Ingrese el primer valor(a):')) #2
b=int(input('Ingrese el segundo valor(b):')) #4
c=int(input('Ingrese el tercer valor(c):')) #5
d=int(input('Ingrese el cuarto valor(d):')) #2
respuesta=a+b*c/d
print('La respuesta es de la operacion:')
print(respuesta)

### EJERCICIO 2 ###
a=int(input('Ingrese el primer valor(a):')) #8
b=int(input('Ingrese el segundo valor(b):')) #2
c=int(input('Ingrese el tercer valor(c):')) #2
d=int(input('Ingrese el cuarto valor(d):')) #2
respuesta=(a/b)*(c+d)
print('La respuesta es de la operacion:')
print(respuesta)

### EJERCICIO 3 ###
a=int(input('Ingrese el primer valor(a):')) #7
b=int(input('Ingrese el segundo valor(b):')) #3
c=int(input('Ingrese el tercer valor(c):')) #2
d=int(input('Ingrese el cuarto valor(d):')) #2
respuesta=a-b*c**d
print('La respuesta es de la operacion:')
print(respuesta)

### EJERCICIO 4 ###
a=int(input('Ingrese el primer valor(a):')) #5
b=int(input('Ingrese el segundo valor(b):')) #3
c=int(input('Ingrese el tercer valor(c):')) #2
d=int(input('Ingrese el cuarto valor(d):')) #6
e=int(input('Ingrese el quinto valor(e):')) #3
respuesta=(a+b)*c-(d/e)
print('La respuesta es de la operacion:')
print(respuesta)

### EJERCICIO 5 ###
a=float(input('Ingrese el primer valor(a):')) #6
b=int(input('Ingrese el segundo valor(b):')) #2
c=int(input('Ingrese el tercer valor(c):')) #5
respuesta=(a*b)%c
print('La respuesta es de la operacion:')
print(respuesta)

### EJERCICIO 6 ###
a=int(input('Ingrese el primer valor(a):')) #2
b=int(input('Ingrese el segundo valor(b):')) #2
c=int(input('Ingrese el tercer valor(c):')) #3
respuesta=(a**b)**c
print('La respuesta es de la operacion:')
print(respuesta)

### EJERCICIO 7 ###
a=int(input('Ingrese el primer valor(a):')) #1
b=int(input('Ingrese el segundo valor(b):')) #1
c=int(input('Ingrese el tercer valor(c):')) #1
d=int(input('Ingrese el cuarto valor(d):')) #1
e=int(input('Ingrese el quinto valor(e):')) #1
respuesta=[(((a+b)-c)*d)/e]
print('La respuesta es de la operacion:')
print(respuesta)


### EJERCICIO 8 ###
a=int(input('Ingrese el primer valor(a):')) #3
b=int(input('Ingrese el segundo valor(b):')) #4
c=int(input('Ingrese el tercer valor(c):')) #2
d=int(input('Ingrese el cuarto valor(d):')) #8
e=int(input('Ingrese el quinto valor(e):')) #2
respuesta=(a*(b+c)/(d-e))/2
print('La respuesta es de la operacion:')
print(respuesta)

### EJERCICIO 9 ###
a=int(input('Ingrese el primer valor(a):')) #2
b=int(input('Ingrese el segundo valor(b):')) #3
c=int(input('Ingrese el tercer valor(c):')) #2
respuesta=((a+b)**c)
print('La respuesta es de la operacion:')
print(respuesta)


### EJERCICIO 10 ###
a=int(input('Ingrese el primer valor(a):')) #4
b=int(input('Ingrese el segundo valor(b):')) #2
c=int(input('Ingrese el tercer valor(c):')) #3
d=int(input('Ingrese el cuarto valor(d):')) #1
e=int(input('Ingrese el quinto valor(e):')) #2
respuesta=(((a-b)*(c+d))/e)
print('La respuesta es de la operacion:')
print(respuesta)


#Segunda parte: Uso de variables y expresiones en Python para resolver ejemplos simples.

## Ejercicio_1 ##
personas=4
rebanada_persona=2
pizza_comprada=5
rebanadaxpizza=8
rebanadascomidas=personas*rebanada_persona
rebanadas_disponibles=pizza_comprada*rebanadaxpizza
rebanadas_sobrantes=rebanadas_disponibles-rebanadascomidas
print('El numero de rebanadas sobrantes es:',rebanadas_sobrantes)

## Ejercicio_2 ##
Camisas=8
preciocamisa=20
descuento=0.2
compra=4
costosindescuento=compra*preciocamisa
montodescuento=costosindescuento*descuento
total=costosindescuento-montodescuento
print('El costo total con descuento es:',total)

## Ejercicio_3 ##
distancia=800
tiempo=4
velocidad=distancia/tiempo
print('la velocidad del avion es:',velocidad)

## Ejercicio_4 ##
camisetas=15
chaquetas=50
descuento=0.1 
compra1=((camisetas)*2+chaquetas)
stotal=compra1*descuento 
total=compra1-stotal
print('El costo con descuento es:',total)

## Ejercicio_5 ##
paginasxdia=500/5
print('El numero de paginas a leer son:',paginasxdia)

## Ejercicio_6 ##
costo_celular=250
tiempo=12
pagos=costo_celular/tiempo
print('El precio mensual a pagar es:',pagos)


## Ejercicio_7 ##
costoviaje=50
descuento=0.15
estudiantes=3
pago=costoviaje*estudiantes
pagodescuento=(pago*descuento)
total=pago-pagodescuento
print('El costo del viaje seria de',total,'Para los 3 estudiantes')


## Ejercicio_8 ##
pesofideos=500
rinde=5
porciones=3
gramosxpersona=100
gramos_a_cocinar=(((rinde*porciones)/pesofideos))*gramosxpersona
print('Los gramos a cocinar son',gramos_a_cocinar*100,'por persona')

## Ejercicio_9 ##
unidades_en_paquete=24
personas=6
corresponden=unidades_en_paquete/personas
print('La cantidad de galletas que les corresponde a cada persona es de:',corresponden)

## Ejercicio_10 ##
dinero_inicial=200
deposito_mensual=50
meses=12
dinero=(deposito_mensual*meses)+dinero_inicial
print('El dinero despues de 12 meses es',dinero)
