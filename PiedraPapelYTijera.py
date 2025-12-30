import random as rd 

min_val = 1
max_val = 3
turnoDeLaCompu = str()
def cpu_pick():
    juego = rd.randint(min_val, max_val)
    match juego:
        case 1:
            return "tijera"
        case 2:
            return "piedra"
        case _ :
            return "papel"

def resultado(var1, cpu):
    usuario = var1.strip().lower()
    match (usuario, cpu):
        case (u, c) if u == c:
            return "Empate!, intenta de nuevo."
        case ("tijera", "papel") | ("piedra", "tijera") | ("papel","piedra"):
            return "Ganaste!"
        case _ :
            return "Perdiste!, intenta de nuevo."
var1 = input(str("Introduce tu jugada (Piedra, Papel o Tijera): "))
cpu = cpu_pick()
print("CPU:", cpu)
print(resultado(var1, cpu))
