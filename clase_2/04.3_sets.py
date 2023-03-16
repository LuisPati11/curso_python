# 4.3 Sets
'''
- Colección de artículos únicos
- Sin orden
- Sin indexación, segmentación u otros comportamientos secuenciales
- Mutable
- No puede anidarse
- Admite operaciones matemáticas con conjuntos
'''

# 4.3.1 Crear un set
# Crear un set vacío
set_vacio=set()
#print(set_vacio)

# Crear un set no vacío
set1={11,5,8}
#print(set1)

# Crear un set a partir de una lista
set_desde_lista=set(["a","b","c"])
#print(set_desde_lista)

# 4.3.2 Modificar un set
# Añadir un elemento
set1 = {11,5,8}
set1.add(10)
#print(set1)

# Borrar un elemento (forma 1)
set1 = {11,5,8}
set1.remove(8)
#print(set1)
# Borrar un elemento (forma 2)
set1 = {11,5,8}
set1.discard(5)
#print(set1)

# 4.3.3 Operaciones comunes con sets
# Unión, intersección, diferencia
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
#print(set1.union(set2))
#print(set1.intersection(set2))
#print(set1.difference(set2))



