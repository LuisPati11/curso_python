# 3. OPERADORES

# 3.1 Aritmética
# Los operadores aritméticos habituales
#print(20 + 7)
#print(20 - 7)
#print(20 * 7)
#print(20 / 7)
#print(20 % 7) # Resto
#print(20 ** 7) # 20^7

# 3.1.1 División de coma flotante frente a división de enteros
'''El operador / realiza la división en coma flotante y devuelve float,
 incluso si uno o ambos operandos
son ints

El operador // realiza la división de enteros y trunca el resultado a cero decimales.
Devolverá devuelve el resultado como flotante si uno o ambos operandos son flotantes,
pero aún así será truncado.'''
print(2/3)
print(2//3)

# 3.2 Comparación
print(20 == 7)
print(20 != 7)
print(20 > 7)
print(20 >= 7)
print(20 < 7)
print(20 <= 7)

print()
# 3.3 Operadores lógicos
# and/or/not
n1 = 15
n2 = 20
print(n1 == 15 and n2 == 15)
print(n1 == 15 or n2 == 15)
print(not n1 == 15)

# 3.4 Operadores bit a bit
# Bitwise AND
num1 = 0b00001111
num2 = 0b11110000
print(bin(num1 & num2))

# Bitwise OR
num1 = 0b00001111
num2 = 0b11110000
bin(num1 | num2)

# Bitwise NOT
num1 = 0b0111
bin(~num1)

# Bitwise XOR
num1 = 0b00110011
num2 = 0b11110000
bin(num1 ^ num2)

# Bitwise desplazamiento a la izquierda
num1 = 0b00111100
bin(num1 >> 2)

# Bitwise desplazamiento a la derecha
num1 = 0b00111100
bin(num1 << 2)

# 3.5 Operador de aumento
''' En python no existe ++ ó -- en vez de esto usaremos lo siguiente'''
num1=11
num1+=1
num2=10
num2-=1
print(num1,num2)
