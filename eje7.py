# Este script imprime la hora del sistema, el estado de la memoria
# RAM y el espacio en disco disponible en /.

# Importamos las librerias necesarias
import os
import time

# Imprimimos la hora del sistema
print('La hora del sistema es:')
os.system('date')

# Imprimimos el estado de la memoria RAM
print('\nEl estado de la memoria RAM es:')
os.system('free -h')

# Imprimimos el espacio en disco disponible en /
print('\nEl espacio en disco disponible en / es:')
os.system('df -h /')
