# 5. Control de flujo

# 5.1 Sentencias condicionales

# 'if-else'
x = 0
if x == 0:
    print('x es 0')
else:
    print('x no es 0')
# Puedes cambiar el valor de x para ver si va por un lado u otro del condicional

# 'if-elif-else'
x = 0
if x == 0:
    print('x es 0')
elif x > 0:
    print('x es positivo')
elif x < 0:
    print('x es negativo')
else:
    print('Nunca llegarás aquí!')

# 5.2 Bucle: for
# Simplest use of for-loop
lista = [1, 2, 3, 4]
for elemento in lista:
    print(elemento)

# Bucle for con break
lista = [-3, -2, -1, 0, 1, 2, 3]
for elemento in lista:
    if elemento < 0:
        print(elemento)
    else:
        break
print('Fin')

# Bucle for con continue
lista = [-3, -2, -1, 0, 1, 2, 3]
for elemento in lista:
    if elemento < 0:
        continue
    print(elemento)
print('Fin')

# Bucle for con else
n = 11
lista = [-3, -2, -1, 0, 1, 2, 3]
for elemento in lista:
    if elemento == n:
        print('Encontrado!')
        break
else:
    # Solo pasa por aquí si el bucle acaba todas sus iteraciones
    print('Elemento no encontrado')

# 5.3 Bucle while
x = 0
while True:
    print(x)
    x += 1
    if x > 4:
        break