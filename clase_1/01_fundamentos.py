print("1. FUNDAMENTOS EN PYTHON")

# La función de impresión es sólo 'print
print("Hola Mundo!") #Puedes usar tanto comillas simples como comillas dobles

# No es necesario declarar variables: basta con asignarles un valor.
# Una declaración por línea, sin punto y coma
a=1
# Aunque las declaraciones multilínea son técnicamente posibles
total = 123 + \
456 + \
999
print(total)

# El tipo de variable puede cambiar en cualquier momento
variable = 1
print(variable)
variable = 0.123
print(variable)
variable = 'some text'
print(variable)

# Python distingue entre mayúsculas y minúsculas
variable = 1
# VARiable -> está línea de código daría error ya que la variable no está definida

# La sangría  forma parte de la sintaxis y se utiliza para delimitar bloques de código.
# No necesitamos llaves!!!
if 1 == 1:
    print('something')

# Todo es un objeto y tiene un ID
int = 123
float = 0.1
def funcion():
    pass
class clase(object):
    pass
print(type(int), id(int))
print(type(float), id(float))
print(type(funcion), id(funcion))
print(type(clase), id(clase))