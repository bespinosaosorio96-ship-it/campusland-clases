import os

import random

x=random.randint(1,10)
print(x)

isActive=True

while isActive:

    os.system("clear")
    print("Bienvenida al minijuego de adivinar un numero entre 1 y 10")

    numero=int(input("Ingrese el numero de cree es el aleatorio: "))


    if numero==x:
        print("\nFelicidades, adivinaste el numero")
        isActive:False
        input()
    else:
        print("\nLo sinto, intenta de nuevo")
        input()
        

