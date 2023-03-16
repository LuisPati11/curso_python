# 4.5 Strings

# Los String pueden crear usando comillas simples o dobles
string1 = 'Hola: \'muy\', "buenas"'
string2 = "Hola: 'muy', \"buenas\""
#print(string1)
#print(string2)

# Los String multilínea pueden definirse con comillas triples (simples o dobles):
string_multilinea1 = '''un
string
largo'''
#print(string_multilinea1)

# Algunas operaciones definidas para listas funcionan también con cadenas
string = 'Eyyy muy buenas a todos guapísimos'
#print(len(string))
#print(string[1:7:2])
#print(type(string[0])) # No existe el tipo char en python

# 4.5.1 Operaciones comunes con cadenas
string = 'Cara anchoa'
# Dividir y unir
palabras = string.split(' ')
#print(palabras)
union = ';'.join(palabras)
#print(union)

# Minúsculas/Mayúsculas
string = 'Que la fuerza te acompañe'
#print(string.upper())
#print(string.lower())
#print(string.swapcase())

# Cambiar partes de un String
string = 'Mucha suerte!'
#print(string.replace('suerte!', 'mierda!'))

# 4.5.2 Formateo de Strings
''' Existen varias maneras de realizar el formateo,
pero yo os voy a mostrar la que para mí es la mejor y más simple
'''
n1 = 11
n2 = 19.11
print(f'Imprimir entero: {n1}, imprimir float: {n2}')


