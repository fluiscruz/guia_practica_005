# El siguiente code realiza la misma tarea que el anterior, pero en lugar de
# pedir los valores por teclado, los recibe como argumentos con la librería sys

# Importamos la libreria sys
import sys

# Verificamos que se hayan pasado los argumentos
if len(sys.argv) != 3:
    print('Error: Debe ingresar dos argumentos')
    print('Uso: python3 eje4.py <sueldo> <rango>')
    print('Donde <sueldo> es un numero real y <rango> es un numero entero')
    print('que puede ser 1, 2 o 3.')
    sys.exit()

# Pedimos el sueldo y el rango
sueldo = float(sys.argv[1])
rango = int(sys.argv[2])

# Definimos un diccionario con la formula segun el rango
rangos = {1: 0.83, 2: 1.2, 3: 5.0}

# Calculamos la asignacion segun el rango
asig_final = sueldo * rangos[rango]

# Imprimimos la signacion estimada
print('La asignación que Ud. percibirá es:', '%.2f' % asig_final, 'ARS')
