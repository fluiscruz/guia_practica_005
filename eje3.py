# El siguiente code toma dos valores de entrada: sueldo y rango,
# y calcula el sueldo neto de un empleado.
# El rango puede ser 1, 2 o 3.

# Pedimos el sueldo y el rango
sueldo = float(input('Ingrese el sueldo: '))
rango = int(input('Ingrese el rango (1, 2 o 3): '))

# Definimos un diccionario con la formula segun el rango
rangos = {1: 0.83, 2: 1.2, 3: 5.0}

# Calculamos la asignacion segun el rango
asig_final = sueldo * rangos[rango]

# Imprimimos la signacion estimada
print('La asignación que Ud. percibirá es:', '%.2f' % asig_final, 'ARS')
