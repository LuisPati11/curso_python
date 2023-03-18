# 7. LAMBDA
'''
Las lambdas son funciones anónimas especiales que pueden definirse 
y pasarse en una sola línea de código
'''
# Sin usar lambdas
palabras = ['BB8', 'R2D2', 'C3PO']

def minus(palabra):
    return palabra.lower()

palabras_en_minuscula = map(minus, palabras)
print(list(palabras_en_minuscula))

# Usando lambdas:
palabras = ['BB8', 'R2D2', 'C3PO']
palabras_en_minuscula = map(lambda palabra: palabra.lower(), palabras)
print(list(palabras_en_minuscula))

# Uno de los casos más específicos: ordenar por clave
palabras = 'Este es el camino'.split(' ')
palabras.sort(key=lambda palabra: len(palabra))
print(palabras)

