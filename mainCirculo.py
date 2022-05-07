from circulo import Circulo
terminado = False
while not terminado:
    radio = float(input("Introduzca un radio, por favor ([0] para terminar el programa): "))
    if radio == 0.0:
        break
    else:
        correcto = False
        circulo = Circulo(radio)
        while not correcto:
            eleccion = int(input("¿Desearía calcular el área (1) o la longitud (2): "))
            if eleccion == 1:
                print(circulo,circulo.calcularArea())
                correcto = True
            elif eleccion == 2:
                print(circulo,circulo.calcularLongitud())
                correcto = True
            else:
                print("Operador no válido, seleccione de nuevo a continuación por favor.")
print("Fin del programa")
