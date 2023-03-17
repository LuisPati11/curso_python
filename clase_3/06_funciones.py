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
