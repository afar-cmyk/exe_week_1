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

if len(resuStr) == int(4):
    resuStr.insert(1, '.')
    resultado = "".join(resuStr)

elif len(resuStr) == int(5):
    resuStr.insert(2, '.')
    resultado = "".join(resuStr)

elif len(resuStr) == int(6):
    resuStr.insert(3, '.')
    resultado = "".join(resuStr)

elif len(resuStr) == int(7):
    resuStr.insert(1, "'")   
    resuStr.insert(5, '.')
    resultado = "".join(resuStr)

else:
    resultado = "".join(resuStr)

## mensaje final con el resultado de la operación
print (f"El pago para el trabajador es de: {resultado} cop.")
