import random 

min_val = 1
dificultad = input("Elige la dificultad(F, M, D): ")

if dificultad == "F":
    max_val = 10
elif dificultad == "M":
    max_val = 50
elif dificultad == "D":
    max_val = 100
elif dificultad not in "FMD":
    print("ERROR, DIFICULTAD NO ENCONTRADA")
    max_val = 10 

numero_al_azar = random.randint(min_val,max_val)
print(numero_al_azar)



while True:
    numero_probar = int(input("Escribi un numero:"))
    if numero_probar < numero_al_azar:
        print("Te quedaste corto compañero, el numero es mas grande que " + str(numero_probar))
    elif numero_probar > numero_al_azar:
        print("Te pasaste compañero, el numero es mas chico que " + str(numero_probar))
    elif numero_probar == numero_al_azar:
        print("Correcto, Ganaste!")
        break
    else:
        print("Error, vuelve a intentarlo")
        
        