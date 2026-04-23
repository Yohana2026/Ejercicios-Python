print("Adivina el número")
introNum = int(input("Por favor, introduzca un número del 1 al 10: "))

def numGanador(numero):
    if numero < 1 or numero > 10:
     print("El número introducido no se encuentra entre el 1 y el 10 ")
    else:
     if numero == 4:
        print("Haz acertado al número ganador")
     else:
        print("El número introducido no ha resultado ser el ganador")

numGanador(introNum)

