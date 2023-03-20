# 9. Gestión de excepciones
# 9.1 Introducción

# Una función sumamente problemática
def dividir(a, b):
    return a / b
# Ejemplo más simple de captura de todas las excepciones (¡NO RECOMENDADO!)
try:
    dividir(11, 'Grogu')
except:
    print('Excepción capturada!')

# Tratamiento de un tipo específico de excepción
try:
    dividir(11, 'Grogu')
except TypeError:
    print('TypeError capturado!')

# Podemos recuperar el objeto de la excepción para obtener información útil
try:
    dividir(11, 'Grogu')
except TypeError as exc:
    print('TypeError capturado!')
    print(exc)

# Gestión de varios tipos de excepción por separado
try:
    dividir(11, 0)
except TypeError:
    print('TypeError capturado!')
except ZeroDivisionError:
    print('ZeroDivisionError capturado!')

# Tratamiento conjunto de varios tipos de excepción
try:
    dividir(11, 0)
except (TypeError, ZeroDivisionError):
    print('Algo fue mal')

# Forzar alguna excepción para que ocurra
try:
    raise Exception('Algo fue mal')
except Exception as err:
    print(err)

# 9.2 Type of erros

# AttributeError
'''
Se produce cuando se accede a un atributo de objeto inexistente

lista = [1, 2, 3]
lista.no_existe
'''
# IndexError
''' Se activa cuando el índice está fuera del rango de una lista

lista = [1, 2, 3]
lista[11]
'''
# KeyError
'''
Aparece cuando no se encuentra la clave de asignación (diccionario)

diccionario = {'a': 1, 'b': 2}
diccionario['Darth_vader']
'''
# NameError
'''
Aparece cuando no se encuentra el nombre local o global

def funcion():
    print(variable)

funcion()
'''
# OSError
'''
Una amplia categoría de excepciones que representan errores relacionados con el sistema o de E/S.

try:
    file = open('X-wing.txt')
except OSError as err:
    raise
'''
# ImportError
'''
Se produce un error al intentar importar un paquete que no existe.
try:
    import owarida
except ImportError as err:
    raise
'''
# SyntaxError
'''
El único tipo de excepción que NO se puede capturar.

try:
    def funcion():
        error de sintaxis en está línea
except:
    print('Capturada!')
'''
# TypeError
'''
Se produce cuando alguna operación o función se aplica a un objeto de tipo incorrecto

'yoda' + 777
'''
# ValueError
'''
Se produce cuando alguna función recibe un argumento de tipo correcto pero de valor incorrecto

print(int("11"))
print(int("Camavinga"))
'''

# 9.3 Assertions
'''
Una aserción es una expresión booleana que siempre debe ser verdadera en el código.
Una aserción fallida indica un error irrecuperable y deben utilizarse para detectar errores
(inesperados) en el código - no para comprobar errores esperados en tiempo de ejecución.
'''
def fibonacci(maximo):
    assert maximo > 0, 'Positive integer expected'
    s1, s2 = 1, 1
    while s1 <= maximo:
        yield s1
        s1, s2 = s2, s1 + s2
secuencia = list(fibonacci(-20))