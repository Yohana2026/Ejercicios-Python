print("Precio total de un producto")

nombreProducto = input("Nombre del producto: ")

precioUnidad = float(input("Precio por unidad: "))

cantComprar = float(input("Cantidad a comprar: "))

descuentoPorcentaje = float(input("Descuento (porcentaje): "))

ivaPorcentaje = float(input("IVA (porcentaje): "))


def calculoPorcentaje(porciento, valor):
    return round(porciento/100 * valor,2)

precioTotal = precioUnidad * cantComprar

precioDesc = precioTotal - calculoPorcentaje(descuentoPorcentaje,precioTotal)

total = precioDesc + calculoPorcentaje(ivaPorcentaje,precioDesc)

print("Precio total aplicando descuento e IVA: " + str(total))












