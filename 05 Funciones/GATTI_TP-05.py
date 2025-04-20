#-----------------
#Actividad 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#-----------------
#Actividad 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Ingresá tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

#-----------------
#Actividad 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("¿Dónde vivís?: ")

informacion_personal(nombre, apellido, edad, residencia)

#-----------------
#Actividad 4
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresá el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}")

#-----------------
#Actividad 5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = int(input("Ingresá la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} horas.")

#-----------------
#Actividad 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#-----------------
#Actividad 7
def operaciones_basicas(a, b):
    suma        = a + b
    resta       = a - b
    multiplicar = a * b
    dividir     = a / b
    return suma, resta, multiplicar, dividir


num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))

resultado = operaciones_basicas(num1, num2)
suma, resta, multiplicar, dividir = resultado

print(f"Suma:           {suma}")
print(f"Resta:          {resta}")
print(f"Multiplicación: {multiplicar}")
print(f"División:       {dividir}")

#-----------------
#Actividad 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingresá tu peso en kilogramos: "))
altura = float(input("Ingresá tu altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu índice de masa corporal (IMC) es: {imc}")

#-----------------
#Actividad 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

celsius = float(input("Ingresá la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")

#-----------------
#Actividad 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

numero1 = float(input("Ingresá el primer número: "))
numero2 = float(input("Ingresá el segundo número: "))
numero3 = float(input("Ingresá el tercer número: "))

promedio = calcular_promedio(numero1, numero2, numero3)
print(f"El promedio de los tres números es: {promedio}")