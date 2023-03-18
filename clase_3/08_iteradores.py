# 8. Iteradores
'''
- Iteración: el proceso de recorrer los objetos o elementos de una colección.
- Iterable es un objeto sobre el que se puede iterar
- Tiene un método '__iter__' que devuelve su iterador
- Tiene implementado el método '__next__' que devuelve el siguiente elemento de la secuencia
'''
i = 'El mejor profesor el fracaso es'.split(' ')

iterador = iter(i)
print(next(iterador))
print(next(iterador))

# Iterador de los números de fibonacci
class Fibonacci:
    def __init__(self):
        self.ant = 0
        self.act = 1
    def __iter__(self):
        return self
    def __next__(self):
        valor = self.act
        self.act += self.ant
        self.ant = valor
        return valor
fib = Fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

# 8.1 Funciones incorporadas basadas en iteradores
'''
- enumerar
- rango
- comprimir
- invertido
- todos
- cualquiera
'''
# 8.1.1 enumerar
'''
enumerate te permite iterar una secuencia
y también obtener índices de elementos (empezando por 0)
'''
palabras = 'Paciencia debes tener, mi joven padawan'.split(' ')
for i, palabra in enumerate(palabras):
    print(i, palabra)

# 8.1.2 rango
# 'range' devuelve una secuencia de enteros
for numero in range(4):
    print(numero)
# Valores en inicio y fin
for numero in range(2, 5):
    print(numero)
print()

# 8.1.3 Invertido
# 'reversed' devuelve un iterador inverso
for i in reversed(range(5)):
    print(i)
print()

# 8.1.4 zip
# 'zip' te permite iterar varias secuencias simultaneamente
numeros = [1, 2, 3, 4, 5]
palabras = 'Imposible nada es. Difícil, muchas cosas son'.split(' ')
booleanos = [True, False, True, False]
for numero, palabra in zip(numeros, palabras):
    print(numero, palabra)
print()
for numero, palabra, bool in zip(numeros, palabras, booleanos):
    print(numero, palabra, bool)

# 8.1.5 all
# 'all' devuelve True si todos los elementos del iterable son True
booleans = [True, False, True, False]
todos_true = [True, True, True]
todos_false = [False, False, False]
print(all(booleans))
print(all(todos_true))
print(all(todos_false))

# 8.1.6 any
# 'any' devuelve True si al menos un elemento del iterable es True
booleans = [True, False, True, False]
todos_true = [True, True, True]
todos_false = [False, False, False]
print(any(booleans))
print(any(todos_true))
print(any(todos_false))

print()

# 'all' y 'any' se pueden combinar con lambdas
palabras = 'Si creer no puedes, es por eso que fallas'.split(' ')
# ¿Hay al menos una palabra con 4 o más letras?
al_menos_una = any(map(lambda word: len(word) >= 4, palabras))
print(al_menos_una)
# ¿Todas las palabras constan de 4 o más letras?
todas = all(map(lambda word: len(word) >= 4, palabras))
print(todas)

# 8.2 Módulos itertools
import itertools

# Combinaciones
letras = 'abcd'
for i in itertools.combinations(letras, 2):
    print(i)

# Combinaciones (con sustitución)
letras = 'abcd'
for i in itertools.combinations_with_replacement(letras, 2):
    print(i)
print()
# Permutaciones
letras = 'abcd'
for i in itertools.permutations(letras, 2):
    print(i)
print()
# Cartesian product
letras = 'abcd'
jedis = ['Yoda', 'Anakin', 'Obi-wan']
for i in itertools.product(letras, jedis):
    print(i)

# Repetir un objeto un número de veces
for i in itertools.repeat('Clon', 5):
    print(i)
print()

''' Hay algunas otras funciones del sistema de la librería itertools como pueden ser:
- cycle
- chain
- takewhile
- dropwhile
'''
