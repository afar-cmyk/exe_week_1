#   Ejercicio #1 - Calculadora de pagos
#
#   Programa que sirve para calcular el pago en pesos 
#   colombianos a un trabajador conforme a sus horas trabajadas

## Ingreso de datos a las variables del programa
numHoras = int(input("Ingrese el numero de horas trabajadas: "))
costoHoras = int(input("Ingrese el costo por hora del trabajador: "))

## calculo de los datos ingresados
resuInt = numHoras * costoHoras

## conversion del resultado a string para agregar el punto decimal y el apostrofe de millón
resuStr = list(str(resuInt))