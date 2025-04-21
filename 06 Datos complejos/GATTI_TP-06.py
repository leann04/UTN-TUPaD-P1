#-------------
#Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#-------------
#Actividad 2
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#-------------
#Actividad 3
lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

#-------------
#Actividad 4
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

#-------------
#Actividad 5
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

#-------------
#Actividad 6
def balanceados(cadena):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    
    for c in cadena:
        if c in pares.values():
            pila.append(c)
        elif c in pares:
            if not pila or pila.pop() != pares[c]:
                return False
    return not pila

#-------------
#Actividad 7
from collections import deque

class Banco:
    def __init__(self):
        self.cola = deque()

    def agregar_cliente(self, nombre):
        self.cola.append(nombre)
        print(f"Cliente {nombre} agregado a la fila.")

    def atender_cliente(self):
        if self.cola:
            cliente = self.cola.popleft()
            print(f"Atendiendo al cliente: {cliente}")
        else:
            print("No hay clientes en la fila.")

    def siguiente_cliente(self):
        if self.cola:
            print(f"El siguiente cliente en la fila es: {self.cola[0]}")
        else:
            print("No hay clientes en la fila.")

#-------------
#Actividad 8
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo
        print(f"Insertado: {valor}")

    def recorrer(self):
        actual = self.inicio
        print("Lista enlazada:")
        while actual:
            print(actual.valor)
            actual = actual.siguiente

#-------------
#Actividad 9
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar_al_final(self, data):
        nuevo_nodo = Nodo(data)
        if not self.head:
            self.head = nuevo_nodo
            return
        ultimo_nodo = self.head
        while ultimo_nodo.next:
            ultimo_nodo = ultimo_nodo.next
        ultimo_nodo.next = nuevo_nodo

    def imprimir_lista(self):
        nodo_actual = self.head
        while nodo_actual:
            print(nodo_actual.data, end=" -> ")
            nodo_actual = nodo_actual.next
        print("None")

    def invertir_lista(self):
       
        prev = None
        actual = self.head
        while(actual is not None):
            siguiente = actual.next  
            actual.next = prev       
            prev = actual          
            actual = siguiente         
        self.head = prev            
