#Crear piedra papel o tijeras.
import random 
opciones = ["Piedra", "Papel", "Tijeras"]

#Eleccion del usuario
jugador = int(input("Eliga\n'0' para Piedra\n'1' para Papel\n'2' para Tijeras\n"))

#Eleccion de la PC
pc = random.choice([0,1,2])

print("Jugador uso:", opciones[jugador])
print("PC uso:", opciones[pc])

if 0 <= jugador <= 2:
    if jugador == pc:
     print("Empate")
    elif jugador - pc in [-1,2]:
        print("PC Gana, Jugador Pierde")
    else:
        print("Jugador Gana, PC pierde")

