# 4 ESTRUCTURAS DE DATOS BASICAS
'''
- Lista
- DICCIONARIO
- Conjunto
- Tupla
'''

# 4.2 Diccionarios
'''
- Equivalente de matriz asociativa (pares clave-valor)
- Se accede a los elementos mediante claves
- Sólo pueden utilizarse como claves tipos inmutables.
- No se permiten claves duplicadas
- Mutable
- Desordenado (conceptualmente)
- Puede anidarse
'''

# 4.2.1 Crear un diccionario
#Crear un diccionario vacío
diccionario1={}
diccionario2=dict()
#print(diccionario1)
#print(diccionario2)

# Crear un diccionario no vacío
diccionario = {1: "bb8", 2: "r2d2"}
#print(diccionario)

# Crear un diccionario poblado con claves y algún valor por defecto
keys = ['a', 'b', 'c']
valor = 11
diccionario = dict.fromkeys(keys, valor)
#print(diccionario)

# 4.2.2 Acceso a los elementos
# Acceder a un elemento a través de la clave
diccionario = {1: "bb8", 2: "r2d2"}
some_key = 1
#print(diccionario[some_key])

# Acceder a todas las claves
diccionario = {1: "bb8", 2: "r2d2"}
#print(diccionario.keys())

# Acceder a todos los valores
diccionario = {1: "bb8", 2: "r2d2"}
#print(diccionario.values())

# Acceder a todos los pares clave-valor
diccionario = {1: "bb8", 2: "r2d2"}
#print(diccionario.items())

# Usar el operador in para comprobar si una clave existe
diccionario = {1: "bb8", 2: "r2d2"}
#print(1 in diccionario)
#print("r2d2" in diccionario)

# 4.2.3 Añadir elementos
# Añadir un par clave valor
diccionario = {1: "bb8", 2: "r2d2"}
diccionario[3] = "c3po"
#print(diccionario)

# Añadir elementos de otro diccionario
diccionario1 = {1: "bb8", 2: "r2d2"}
diccinario2 = {2: "Anakin", 3: "Yoda"}
diccionario1.update(diccinario2) # Sobrescribe los datos si alguna clave se repite
#print(diccionario1)

# 4.2.5 Borrar elementos
# Borrar un elemento (forma 1)
diccionario = {1: "bb8", 2: "r2d2"}
del diccionario[1]
#print(diccionario)
# Borrar un elemento (forma 2)
diccionario = {1: "bb8", 2: "r2d2"}
diccionario.pop(1)
#print(diccionario)
# Borrar todos los elementos del diccionario
diccionario = {1: "bb8", 2: "r2d2"}
diccionario.clear()
#print(diccionario)

# 4.2.6 Otras operaciones
diccionario = {1: "bb8", 2: "r2d2"}
#print(len(diccionario)) #longitud
diccinario2=diccionario.copy() #copiar diccionario
#print(diccinario2)
