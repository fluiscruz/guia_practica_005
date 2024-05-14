# Este programa muestra un contador (con avance cada segundo). El tiempo
# de duración del contador estará definido por el usuario y se recibe
# como argumento de entrada desde el code bash.

# Importamos la libreria sys
import sys
import time

# Verificamos que se haya pasado un argumento
if len(sys.argv) != 2:
    print('Error: Debe ingresar un argumento')
    print('Uso: python3 eje5.py <tiempo>')
    print('Donde <tiempo> es un numero entero que representa la cantidad de segundos')
    print('que durará el contador.')
    sys.exit()

# Pedimos el tiempo
tiempo = int(sys.argv[1])

# Imprimimos el contador desde uno hasta el tiempo
for i in range(1, tiempo+1):
    print(i)
    time.sleep(1)
