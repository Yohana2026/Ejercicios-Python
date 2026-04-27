print("Calculadora de nota media")
cantNotas = int(input("¿Cuántas notas desea introducir?: "))

suma = 0
for i in range(cantNotas):
   valor = int(input("Ingrese nota: "))
   suma = suma + valor
   media = suma/cantNotas
print("Media " + str(media))

