import random
import sys

#opciones de ingreso de datos
opciones = ["piedra", "papel", "tijera"]

#datos que ingresa el usuario en terminal
usuario = sys.argv[1]

#verificacion de datos validos
if usuario not in opciones:
        print("Argumento inválido. Debes elegir entre: piedra, papel o tijera.")
        sys.exit(1)

#seleccion ramdom del pc
pc = random.choice(opciones)

#mensaje que muestra la seleccion de opciones
print (f"Tu jugaste {usuario} - El PC jugó {pc}")

#logica del juego
if usuario == pc:
    print("Empate!!")
elif ((usuario == "piedra" and pc == "papel") or
    (usuario == "papel" and pc == "tijera") or
    (usuario == "tijera" and pc == "piedra")):
    print("Perdiste!!")
else:
    print("Ganaste!!")
    
