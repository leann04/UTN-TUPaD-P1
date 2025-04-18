#Actividad 1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("es mayor de edad")

#----------------------------
#Actividad 2
nota = int(input("Ingrese su nota: "))
if nota >= 6 :
    print("Aprobado")
else:
    print("Desaprobado")

#----------------------------
#Actividad 3
numero = int(input("Ingrese un numero par: "))
if numero % 2 == 0 :
    print("Su numero es par")
else:
    print("Por favor ingrese un numero par")

#----------------------------
#Actividad 4
EDad = int(input("Ingrese su edad: "))
if EDad >=0 and EDad < 12:
    print("Usted es un niño/a")
elif EDad >= 12 and EDad < 18:
    print("Usted es un adolescente")
elif EDad >= 18 and EDad < 30:
    print ("Usted es un adulto/a joven")
else:
    print("Usted es un adulto/a")

#----------------------------
#Actividad 5
contra = input("Ingrese una contraseña: ")
if 8 <= len(contra) <=14:
    print ("Ha ingresado una contraseña correcta")
else :
    print("Ingrese una contraseña entre 8 y 14 caracteres")

#----------------------------
#Actividad 6 
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")

#----------------------------
#Actividad 7
frase = input("Ingrese una palabra o frase: ")

if frase[-1].lower() in "aeiou":
    frase += "!"
    
print(frase)

#----------------------------
#Actividad 8

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese una opcion 1, 2, 3: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("opcion no valida")

#----------------------------
#Actividad 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:  
    print("Extremo (puede causar graves daños a gran escala)")

#----------------------------
#Actividad 10
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = estacion_sur = "Fecha inválida"

if hemisferio == "N":
    print("Estás en", estacion_norte)
elif hemisferio == "S":
    print("Estás en", estacion_sur)
else:
    print("Hemisferio no válido")
