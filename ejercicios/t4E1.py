print ("Ruleta de la fortuna de los colores")
print ("De los colores mencionados a continuación, escoge uno: ROJO, VERDE AZUL AMARILLO, MORADO")
colorElegido = input("Escribe el color elegido: ")

def eligeColor(color):
    if colorElegido.lower() == "rojo":
        print ("Rojo: mensaje de pasión y energía.")
    elif colorElegido.lower() == "verde":
        print ("Verde: mensaje de esperanza y crecimiento.")
    elif colorElegido.lower() == "azul":
        print ("Azul: mensaje de calma y serenidad.")
    elif colorElegido.lower() == "amarillo":
        print ("Amarillo: mensaje de felicidad y optimismo.")
    else:
        print("Morado: mensaje de sabiduría y creatividad.")
     
eligeColor(colorElegido)