#!/bin/bash
# Este programa ejecuta tres contadores (con avance cada segundo)
# en python (eje5.1.py, eje5.2.py y eje5.3.py). El tiempo de duración de
# los contadores estará definido por el usuario en este bash.

# Pedimos al usuario que ingrese el tiempo de duración de los contadores
echo "Ingrese el tiempo de duración de los contadores (en segundos):"
read tiempo

echo ""
echo "Iniciando los contadores..."
echo ""

# Ejecutamos los contadores en python
python3 eje5.1.py $tiempo &
python3 eje5.2.py $tiempo &
python3 eje5.3.py $tiempo &

# Identificamos los PID de cada contador
pid1=$(ps -ef | grep "python3 eje5.1.py" | grep -v "grep" | awk '{print $2}')
pid2=$(ps -ef | grep "python3 eje5.2.py" | grep -v "grep" | awk '{print $2}')
pid3=$(ps -ef | grep "python3 eje5.3.py" | grep -v "grep" | awk '{print $2}')

# Esperamos a que los contadores terminen
sleep $tiempo

echo ""
echo "Los contadores se ejecutaron con los siguientes PID:"

# Mostramos los PID de los contadores
echo "PID del contador 1: $pid1"
echo "PID del contador 2: $pid2"
echo "PID del contador 3: $pid3"

echo ""
echo "Los contadores han finalizado."
echo ""
echo "*By: Luis Cruz"
