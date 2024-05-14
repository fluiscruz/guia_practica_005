# El siguiente script simula una calculadora simple que recibe dos valores
# y un operador como argumentos de entrada. El operador puede ser +, -, * o /.

# Importamos la libreria sys
import sys

# Verificamos que se hayan pasado los argumentos
if len(sys.argv) != 4:
    print('Error: Debe ingresar tres argumentos válidos')
    print('Uso: python3 eje6.py <v1> <op> <v2>')
    print('Donde <v1> y <v2> son numeros reales y <op> es un caracter')
    print('que puede ser +, -, x o /.')
    sys.exit()

# Pedimos los valores y el operador
v1 = float(sys.argv[1])
op = sys.argv[2]
v2 = float(sys.argv[3])

# Definimos un diccionario con las operaciones
operaciones = {'+': v1 + v2,
               '-': v1 - v2,
               'x': v1 * v2,
               '/': v1 / v2}

# Calculamos el resultado segun el operador
resultado = operaciones[op]

# Imprimimos el resultado
print('El resultado de la operación es:', resultado)
