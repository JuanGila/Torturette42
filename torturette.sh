#!/bin/bash
clear
# NUMEROS VERDES CAYENDO
for i in {1..10}
do
    printf "\033[32m"
    for j in {1..210}
    do
        printf "%c" $((RANDOM % 94 + 33))
    done
    echo
    sleep 0.01
done
# # FIN NUMEROS VERDES CAYENDO
clear
# BUCLE DE FRAMES
# Comprobar que existen archivos .ansi
if ! compgen -G "assets/ansi/*.ansi" > /dev/null; then
    echo "Se ha modificado la estructura del tester. Reinstalar torturette."
    exit 1
fi
# Iteramos por los archivos .ansi
for f in assets/ansi/*.ansi
do
    printf '\033[H%s' "$(<"$f")"
done
# # FIN BUCLE DE FRAMES
: <<'COMMENT'
Esto es un comentario multilinea
que Bash va a ignorar completamente
porque está dentro de un string no ejecutado
progress=0
while (( progress < 100 )); do
    # Salto aleatorio entre 10 y 15. Cada frame avanza siempre entre 10% y 15% respecto al anterior. EVALUAR SI DEBE SER 12%-18%.
    step=$(( RANDOM % 6 + 10 ))
    # Obtenemos el frame correspondiente a progress mediante RANDOM.
    progress=$(( progress + step ))
    # "Si progress es mayor que 100, entonces pon progress a 100" porque el operador && en Bash significa: ejecuta lo de la derecha solo si lo de la izquierda es verdadero.
    (( progress > 100 )) && progress=100
    # Guardamos en la variable f el path del frame correspondiente a progress
    printf -v f 'assets/ansi/frame%03d.ansi' "$progress"
    printf '\033[H%s' "$(<"$f")"
done
COMMENT