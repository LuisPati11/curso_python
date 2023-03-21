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
#print(obj.a)
#print(obj.b)

# Utilizar argumentos por defecto en lugar de inicializadores múltiples
class Clase:
    def __init__(self, a=11, b='Ron Weasly'):
        self.a = a
        self.b = b

obj1 = Clase()
obj2 = Clase(a=777)
obj3 = Clase(a=777, b='Hemione Granger')
#print(obj1.a, obj1.b)
#print(obj2.a, obj2.b)
#print(obj3.a, obj3.b)

# 10.3 Atributos
# Los atributos de instancia se establecen normalmente en el inicializador:
class Clase:
    def __init__(self, nombre):
        self.nombre = nombre

obj1 = Clase('Luis')
obj2 = Clase('Adrián')
#print(obj1.nombre)
#print(obj2.nombre)

# 10.2.1 Propiedades
class PythonGetSet:
    def __init__(self, nombre):
        self._nombre = nombre
    
    @property
    def nombre(self):
        #print('Llamada al get')
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        #print('Llamada al set')
        self._nombre = value

    @nombre.deleter
    def nombre(self):
        #print('Llamada a borrar')
        del self._nombre

obj = PythonGetSet('Luis')

obj.nombre = 'Beatriz'
#print(obj.nombre)
del obj.nombre

# 10.2 Funciones integradas
'''
• hasattr
• getattr
• setattr
• delattr
Útil cuando no se conoce el nombre del atributo en el momento de escribir el código
'''

# hasattr comprueba si el objeto tiene algún atributo
class DemoAtributos:
    def __init__(self, nombre):
        self.nombre = nombre

obj = DemoAtributos('Luispa')
obj.numero = 0

#print(hasattr(obj, 'nombre'))
#print(hasattr(obj, 'numero'))
#print(hasattr(obj, 'apellido'))

# getattr devuelve el valor del atributo especificado. También puede devolver algún valor por defecto, en caso de que el atributo solicitado no exista.
class DemoAtributo:
    def __init__(self, nombre):
        self.nombre = nombre

obj = DemoAtributo('Luis')

#print(getattr(obj, 'nombre'))
#print(getattr(obj, 'no_existe', 'No existe ningún atributo'))

# setattr establece (o sobrescribe) el valor del atributo especificado

class DemoAtributo:
    def __init__(self, nombre):
        self.nombre = nombre

obj = DemoAtributo('Luis')

setattr(obj, 'nuevo_atributo', 'Patiño')
setattr(obj, 'nombre', 'Adrián')
print(obj.nuevo_atributo)
print(obj.nombre)