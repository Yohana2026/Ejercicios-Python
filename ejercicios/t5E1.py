print("Calculadora de nota media")
cantNotas = int(input("¿Cuántas notas desea introducir?: "))

listaNotas = []
for i in range(cantNotas):
   valor = int(input("Ingrese nota: "))
   listaNotas.append(valor)
   media = sum(listaNotas) / cantNotas
print("Media " + str(media))

