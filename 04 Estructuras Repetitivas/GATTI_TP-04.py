#-------------------
#Actividad 1
for x in range (101):
    print(x)

#-------------------
#Actividad 2
numero = int(input("Ingrese un numero: "))
cantidad_digitos = len(str(numero))
print("la cantidad de digitos es de:",cantidad_digitos)

#-------------------
#Actividad 3
inicio = int(input("ingrese el numeo inicial: "))
fin = int(input("ingrese el numero final: "))
suma = 0
for x in range(inicio+1,fin):
    suma = suma + x
print("la suma del rango es:", suma)

#-------------------
#Actividad 4
total = 0
numerO = int(input("Ingrese un numero(0 si desea terminar): "))

while numerO != 0:
    total = total + numerO 
    numerO = int(input("Ingrese un numero(0 si desea terminar): "))
print("la suma es de:",total)

#-------------------
#Actividad 5
import random
secreto = random.randint(0,9)
intentos = 1
intento = int(input("Ingrese un numero del 0 al 9"))
while intento != secreto:
    intentos += 1
    intento = int(input("Ingrese un numero entre 0 y 9"))
print ("esta fue tu cantidad de intentos:", intentos)

#-------------------
#Actividad 6
for i in range(100, -1, -1): 
    if i % 2 == 0:
        print(i)

#-------------------
#Actividad 7
n = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(n + 1):
        suma += i
print("La suma desde 0 hasta", n, "es:", suma)

#-------------------
#Actividad 8
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):  
    num = int(input(f"Ingrese el número {i+1}: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

#-------------------
#Actividad 9
CANTIDAD_NUMEROS = 100  

suma = 0

for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

media = suma / CANTIDAD_NUMEROS

print("La media (promedio) de los valores ingresados es:", media)

#-------------------
#Actividad 10
numero = int(input("Ingrese un número entero: "))
invertido = 0

while numero > 0:
    digito = numero % 10   
    invertido = invertido * 10 + digito  
    numero = numero // 10

print("Número invertido:", invertido)