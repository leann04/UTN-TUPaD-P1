# Actividad 1
lista_multiplos_4 = list(range(4, 101, 4))
print(lista_multiplos_4)

# Actividad 2
mis_favoritos = ["skate", "guitarra", "boxeo", "viajes", "gatos"]
print(mis_favoritos[-2])

# Actividad 3
lista_vacia = []
lista_vacia.append("skate")
lista_vacia.append("guitarra")
lista_vacia.append("viaje")
print(lista_vacia)

# Actividad 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro" 
animales[3] = "oso" 
print(animales)

# Actividad 5
# Crea una lista de numeros, elimina al numero mas grande y luego imprime por pantalla el resultado 

# Actividad 6
numeros = list(range(10, 31, 5))
print(numeros[:2])

# Actividad 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "fiat"
autos[2] = "ford"
print(autos)

# Actividad 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# Actividad 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][compras[1].index("fideos")] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(compras)

# Actividad 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)

