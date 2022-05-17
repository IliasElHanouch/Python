from fecha import Fecha
dia = int(input("Introduzca el día: "))
mes = input("Introduzca el mes: ")
anio = int(input("Introduzca el año: "))
fecha = Fecha(dia,mes,anio)
print(fecha)
