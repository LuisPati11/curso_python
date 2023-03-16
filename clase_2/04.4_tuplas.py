# 4.4 Tuplas
'''
- Similar a las listas, pero inmutable
- Más rápido que las listas (en caso de muchos elementos)
- Suele utilizarse para agrupar valores que lógicamente "van juntos" (pares, triples...)
'''

# Crear una tupla
tupla1 = (1, 2, 3,)
tupla2 = 1, 2, 3
#print(tupla1)
#print(tupla2)

# Las operaciones de lista que no modifican su contenido también funcionan con tuplas
tupla = (1, 2, 3, 4, 5,)
#print(len(tupla))
#print(tupla[1:3])
#print(tupla.index(3))

# Un uso común de las tuplas
valores_empaquetados = 1, 2, 3
a, b, c = valores_empaquetados
#print(a, b, c)

# Cambiar valores
a, b = 11, 777
#print(a, b)
a, b = b, a
#print(a, b)
