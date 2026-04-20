print("Precio total de un producto")

nombreProducto = input("Nombre del producto: ")

precioUnidad = float(input("Precio por unidad: "))

cantComprar = float(input("Cantidad a comprar: "))

descuentoPorcentaje = float(input("Descuento (porcentaje): "))

ivaPorcentaje = float(input("IVA (porcentaje): "))

calculoIva = ivaPorcentaje / 100

precioTotal = precioUnidad * cantComprar


precioDesc = (descuentoPorcentaje / 100) * precioTotal
    








