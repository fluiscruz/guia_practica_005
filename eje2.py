# Importamos la libreria os
import os

# Listamos todos los directorios dentro del
# directorio /dev/
for file in os.listdir('/dev/'):
    print(file, end='\t')
print()
