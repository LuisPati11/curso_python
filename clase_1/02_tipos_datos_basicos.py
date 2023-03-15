# 2. TIPOS DE DATOS BÁSICOS
'''
• Integers
• Floats
• Booleans
• None

'''
# 2.1 Integers
int_dec = 18
int_hex = 0xFF
int_bin = 0b00001111
print(int_dec)
print(int_hex)
print(int_bin)

# 2.2 Floats
# La precisión de los floats es específica de la implementación
float1 = 0.852
float2 = 1 / 3
print(float1)
print(float2)
# Notación científica
float_sci = 2.3e-6
print(float_sci)

# 2.3 Booleans
esto_es_True = True
esto_es_False = False

# 2.4 None
# Una constante especial que representa un valor nulo.
nada = None
print(type(nada))

# 2.5 Conversiones de tipos
# Conversión de int a float
n_int = 15
n_float = float(n_int)
print(n_float)
# La conversión de float a int TRUNCA, ¡no redondea!
n_float = 15.789
n_int = int(n_float)
print(n_int)
