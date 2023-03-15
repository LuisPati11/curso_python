# 4 ESTRUCTURAS DE DATOS BASICAS
'''
- Lista
- Diccionario
- Conjunto
- Tupla
'''

# 4.1 Lista
'''
- Equivalente de una matriz
- Mutable
- Ordenada
- Índice cero
- Puede anidarse
- Puede contener elementos de distintos tipos
- Puede utilizarse como pila o cola
'''

# 4.1.1 Crear una lista
# Crear una lista vacía
lista_vacia = []
otra_lista_vacia = list()
print(lista_vacia)
print(otra_lista_vacia)

# Crear una lista no vacía
lista_no_vacia = [0, 1, 2, 3, 4,]
print(lista_no_vacia)

# Creación de una lista rellenada con el valor especificado
lista = [14] * 10
print(lista)

# En una lista puede haber varios tipos
lista_mixta = [1, 0.3, False, 'mixta', None]
print(lista_mixta)

# 4.1.2 Añadir elementos
# Añadir un elemento al final de la lista
lista = [1, 2, 3, 4, 5]
lista.append(6)
print(lista)

# Añadir un elemento en una posición específica
lista = [1, 2, 3, 4, 5]
lista.insert(2, 'python')
print(lista)

# Añadir otra lista (forma 1)
lista1 = [1, 2]
lista2 = [3, 4]
lista1 += lista2
print(lista1)

# Añadir otra lista (forma 2)
lista1 = [1, 2]
lista2 = [3, 4]
lista1.extend(lista2)
print(lista1)

# 4.1.3 Borrar elementos
# Borrar un elemento especifico
lista = [1, 2, 3, 4]
lista.remove(3)
print(lista)

# Borrar un elemento por el índice (forma 1)
lista = [1, 2, 3, 4, 5]
lista.pop(2) #Recuerda que el primer elemento de la lista es el 0 por lo que el elemento 2 sería realmente el tercer elemento
print(lista)

# Borrar un elemento por el índice (forma 2)
lista = [1, 2, 3, 4, 5]
del lista[2]
print(lista)

# Borrar el último elemento
lista = [1, 2, 3, 4, 5]
lista.pop()
print(lista)

# Borrar todos los elementos
lista = [1, 2, 3, 4, 5]
lista.clear()
print(lista)

# 4.1.4 Otras operaciones comunes con listas
# Longitud de la lista
lista = [1, 2, 3, 4, 5]
print(len(lista))

# Ordenar la lista
lista = [5, 1, 4, 2, 3]
lista.sort()
print(lista)

# Invertir la lista
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)

# Comprobar si un elemento está en la lista
lista = [1, 2, 3, 4, 5]
print(1 in lista)
print(11 in lista)

# Contar cuantas veces aparece un elemento en una lista
lista = [11, 3, 5, 11, 11]
n = lista.count(11)
print(n)

# Hacer una copia de una lista
lista = [1, 2, 3, 4, 5]
copia = lista.copy()
print(lista)
print(copia)

# Encontrar el índice de un elemento concreto de la lista
lista = [1, 2, 3, 4, 5,11]
elemento = lista.index(11)
print(elemento)

# 4.1.5 Indexación
# Acceso a un solo elemento utilizando la notación de corchetes
# Accessing a single element using bracket notation
lista = [1, 2, 3, 4, 5]
print(lista[2])
# Indexación negativa - contando desde el final de la lista
lista = [1, 2, 3, 4, 5]
print(lista[-2])

# 4.1.6 Slicing
# Obtener un rango de valores con slicing
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista[:5])
print(lista[5:])
print(lista[2:8])
