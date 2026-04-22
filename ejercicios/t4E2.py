print("Adivina el número")
introNum = int(input("Por favor, introduzca un número del 1 al 10: "))

def numGanador(numero):
    if numero == 4:
        print("Haz acertado al número ganador")
    else:
        print("El número introducido no ha resultado ser el ganador")

numGanador(introNum)