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
diccionario = {'a': 1, 'b': 2}
diccionario['Darth_vader']