print ("Conversor de monedas")

print ("Dólares (1 euro = 1.1 dólares)")
print("Libras (1 euro = 0.87 libras)")

cantEuro = float(input("Por favor, introduzca el monto total de euros : "))

def converDolar():
    dolar = cantEuro * 1.1
    return dolar

def converLibra():
    libra = cantEuro * 0.87
    return libra

print (" Euros = " + str(cantEuro) + " / Dólares = " + str(converDolar()))
print (" Euros = " + str(cantEuro) + " / Libras = " + str(converLibra()))

