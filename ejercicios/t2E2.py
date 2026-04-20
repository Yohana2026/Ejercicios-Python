print("Tienda de Ropa")
print("Precio camiseta: 10 euros")
print("Precio sudadera: 20.5 euros")
print("Precio gorra: 5.5 euros")

cantCamiseta = int(input("Cuántas camisetas desea: "))

cantSudadera = int(input("Cuántas sudaderas desea: "))

cantGorra = int(input("Cuántas gorras desea: "))

totalCompra = ((10 * cantCamiseta) + (20.5 * cantSudadera) + (5.5 * cantGorra))

iva = (totalCompra * 0.21) 

totalIva = totalCompra + iva

print("Total de la compra antes de IVA: ", totalCompra)

print("IVA de la compra", iva) 

print("Precio final: ", totalIva)



