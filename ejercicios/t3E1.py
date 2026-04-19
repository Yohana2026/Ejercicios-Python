print("Precio total de un producto")

nombreProducto = input("Nombre del producto: ")

precioUnidad = float(input("Precio por unidad: "))

cantComprar = float(input("Cantidad a comprar: "))

descuentoPorcentaje = float(input("Descuento (porcentaje): "))

ivaPorcentaje = float(input("IVA en porcentaje: "))

#precio total antes de descuento
def precioTotal():
    precioPagar = precioUnidad * cantComprar
    return precioPagar

print("El precio total es " + str(precioTotal()))

#descuento del porcentaje
def descPorc ():
    precioDesc = (descuentoPorcentaje / 100) * precioTotal()
    return precioDesc

print("El descuento es " + str(descPorc()))

#precio total con descuento
def totalYDesc():
    total = precioTotal() - descPorc() 
    return total 


print("El total aplicando descuento es " + str(totalYDesc()))
 
def calculoIva():
    iva = ivaPorcentaje / 100
    return iva

def totalDescIva():
    total = (totalYDesc() * calculoIva()) + totalYDesc()
    return total

print ("Usted debe pagar: " + str(totalDescIva()))




