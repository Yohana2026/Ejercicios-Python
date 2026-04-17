print("Precio camiseta: 10 euros")

print("Precio sudadera: 20.5 euros")

print("Precio gorra: 5.5 euros")

cant_camiseta = int(input("Cuántas camisetas desea: "))

cant_sudadera = int(input("Cuántas sudaderas desea: "))

cant_gorra = int(input("Cuántas gorras desea: "))

total_compra = ((10 * cant_camiseta) + (20.5 * cant_sudadera) + (5.5 * cant_gorra))

print("Total de la compra antes de IVA: ", total_compra)

total_iva = (total_compra * 0.21) + total_compra 

print("Total de compra + IVA: ", total_iva)

print("Precio final: ", total_iva)