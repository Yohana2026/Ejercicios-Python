print("Tienda de Ropa")

print("Precio camiseta: 10 euros")

print("Precio sudadera: 20.5 euros")

print("Precio gorra: 5.5 euros")

cantCamiseta = int(input("Cuántas camisetas desea: "))

cantSudadera = int(input("Cuántas sudaderas desea: "))

cantGorra = int(input("Cuántas gorras desea: "))

totalCompra = ((10 * cantCamiseta) + (20.5 * cantSudadera) + (5.5 * cantGorra))

print("Total de la compra antes de IVA: ", totalCompra)

totalIva = (totalCompra * 0.21) + totalCompra 

#SUGERENCIA: Aquí yo mostraría solo el valor del IVA cambiando el textpo a mostrs por 'IVA de la compra' 
#En el próximo print(línea 25) vas a mostrar el valor del iva + precio de compra.
print("Total de compra + IVA: ", totalIva) 

print("Precio final: ", totalIva)

#SUGERENCIA: Intentar validar que el valor que entra el cliente sea un número entero, en caso contrario no incluyo el producto en la compra.

#En general muy bien!