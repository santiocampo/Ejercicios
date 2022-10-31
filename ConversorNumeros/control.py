import binario
import octal
import dec
import hexadecimal
import interfaz

textoEntrada = interfaz.textoConversor()
print(textoEntrada)

while True:
    try:
        baseEntrada = int(input("Ingrese, como número, la base actual del número: "))
    except ValueError:
        continue
    if baseEntrada not in [2, 8, 10, 16]:
        print("Ingrese de nuevo la base que desea")
    else:
        break

while True:
    try:
        if (baseEntrada == 2):
            numero = input("Ingrese el número: ")
        if (baseEntrada == 8):
            numero = input("Ingrese el número: ")
        if (baseEntrada == 10):
            numero = int(input("Ingrese el número: "))
        if (baseEntrada == 16):
            numero = input("Ingrese el número: ")
    except ValueError:
        continue
    if numero != None:
        break
    else:
        print("El número ingresado es incorrecto")  

while True:
    try:
        baseSalida = int(input("Ingrese, como número, la base a la cual desea transformar el número: "))
    except ValueError:
        continue
    if (baseSalida not in [2, 8, 10, 16]) or (baseEntrada == baseSalida):
        print("Ingrese de nuevo la base que desea")
    else:
        break

def decision(baseEntrada, baseSalida, numero):
    if (baseEntrada == 2) and (baseSalida == 8):
        resultado = binario.binario_octal(numero)
    if (baseEntrada == 2) and (baseSalida == 10):
        resultado = binario.binario_decimal(numero)
    if (baseEntrada == 2) and (baseSalida == 16):
        resultado = binario.binario_hexadecimal(numero)
    if (baseEntrada == 8) and (baseSalida == 2):
        resultado = octal.octal_binario(numero)
    if (baseEntrada == 8) and (baseSalida == 10):
        resultado = octal.octal_decimal(numero)
    if (baseEntrada == 8) and (baseSalida == 16):
        resultado = octal.octal_hexadecimal(numero)
    if (baseEntrada == 10) and (baseSalida == 2):
        resultado = dec.decimal_binario(numero)
    if (baseEntrada == 10) and (baseSalida == 8):
        resultado = dec.decimal_octal(numero)
    if (baseEntrada == 10) and (baseSalida == 16):
        resultado = dec.decimal_hexadecimal(numero)
    if (baseEntrada == 16) and (baseSalida == 2):
        resultado = hexadecimal.hexadecimal_binario(numero)
    if (baseEntrada == 16) and (baseSalida == 8):
        resultado = hexadecimal.hexadecimal_octal(numero)
    if (baseEntrada == 16) and (baseSalida == 10):
        resultado = hexadecimal.hexadecimal_decimal(numero)
    return resultado

salida = decision(baseEntrada, baseSalida, numero)

print("El número {} en base {} es: {}".format(numero, baseSalida, salida))