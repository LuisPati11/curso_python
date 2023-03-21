# 10. Clases y objetos

# 10.1 Introducción
class Clase: # Las clases siempre van en mayúsculas
    pass

# Creando una estancia de una clase
obj = Clase()

# 10.2 Inicialización
'''
El inicializador se define como método __init__. Toma al menos un argumento, que representa la
instancia de la clase que se está inicializando.
Técnicamente, esto no es un constructor, ya que no es la primera cosa que se llama cuando el objeto se crea.
'''
class Clase:
    def __init__(self):
        self.a = 11
        self.b = 'Draco Malfoy'

obj = Clase()
print(obj.a)
print(obj.b)

# Utilizar argumentos por defecto en lugar de inicializadores múltiples
class Clase:
    def __init__(self, a=11, b='Ron Weasly'):
        self.a = a
        self.b = b

obj1 = Clase()
obj2 = Clase(a=777)
obj3 = Clase(a=777, b='Hemione Granger')
print(obj1.a, obj1.b)
print(obj2.a, obj2.b)
print(obj3.a, obj3.b)

# 10.3 Atributos
# Los atributos de instancia se establecen normalmente en el inicializador:
class Clase:
    def __init__(self, nombre):
        self.nombre = nombre

obj1 = Clase('Luis')
obj2 = Clase('Adrián')
print(obj1.nombre)
print(obj2.nombre)

