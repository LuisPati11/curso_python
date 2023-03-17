# 6 Fucniones
'''
- Las funciones se declaran con la palabra clave def
- No se especifica ningún tipo de retorno ni de parámetro
- Se aplican las mismas reglas de sangrado que en otros bloques de flujo de control (sentencia if, bucle for, etc.).
- Si la función no tiene sentencia return, devuelve None por defecto
- Las funciones pueden devolver varios valores
- Las funciones pueden anidarse
'''
# 6.1 Definición de una función
def suma(n1, n2):
    resultado = n1 + n2
    return resultado
resultado = suma(10, 1)
#print(resultado)

# 6.2 Devolver valores
# Si la función no tiene return devuelve None
def no_return(arg):
    print(arg)
resultado = no_return("No tiene return")
print(resultado)

# Una función puede devolver varios valores como tupla
def devolver_varios():
    val1 = 11
    val2 = 'Grogu'
    val3 = False
    return val1, val2, val3
# Guardar valores por separado
res1, res2, res3 = devolver_varios()
print(res1, res2, res3)
# Guardar valores en una tupla
res_all = devolver_varios()
print(res_all)

# 6.3 Argumentos
# Podemos pasar arguemntos a las funciones
def pasar_a_mayuscula(texto):
    print(texto.upper())
pasar_a_mayuscula("Te elijo a ti!")

# Orgumentos opcionales (debe aparecer como el último argumento tras los requeridos)
def sumar_todo(n, *args):
    total = n + sum(args)
    return total
print(sumar_todo(1))
print(sumar_todo(1, 776))
print(sumar_todo(1, 120, 455))

#Argumentos por defecto
def funcion(arg1=11, arg2='mec', arg3=None):
    print(f'1º argumento: {arg1}, 2º argumento: {arg2}, 3º argumento:{arg3}')
funcion()
funcion(arg1="CR7",arg2=777)
funcion(arg2='Yabo', arg3=112)
funcion(arg3=23, arg2='Messi')
#some_func(unknown_argument='wont work')

# 6.4 Campos de aplicación de las variables
# 6.4.1 Variables globales
variable = 'Hola yo soy una variable global'
def funcion():
    variable += '!!!'
    print(variable)
funcion()




