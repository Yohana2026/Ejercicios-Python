print("Planetas del sistema solar")
planets = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
print("Planetas del sistema solar: "+ str(planets))
valor = int(input("Introdizca un número del 1 al 8: "))

if valor >= 1 and valor <= 8:
    print (planets[valor-1])
else:
    print("ERROR: El número introducido no es correcto")

        
