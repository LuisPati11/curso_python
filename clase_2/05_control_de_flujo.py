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