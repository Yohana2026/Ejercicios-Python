print("Meses del año")
listaMeses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

valor = int(input("Introduzca un número del 1 al 12: "))

if valor >= 1 and valor <= 12:
    mes = listaMeses[valor-1]
    print (mes)
    if mes == "Junio":
        print("EL MEJOR MES")
else:
    print("ERROR: El número introducido no es correcto")