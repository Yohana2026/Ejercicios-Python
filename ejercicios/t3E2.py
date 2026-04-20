print ("Conversor de monedas")

print ("Dólares (1 euro = 1.1 dólares)")
print("Libras (1 euro = 0.87 libras)")

cantEuro = float(input("Por favor, introduzca el monto total de euros : "))

def convertir(tipoCambio):
    return round(cantEuro * tipoCambio,2)


print (" Euros = " + str(cantEuro) + " / Dólares = " + str(convertir(1.1)))
print (" Euros = " + str(cantEuro) + " / Libras = " + str(convertir(0.87)))

