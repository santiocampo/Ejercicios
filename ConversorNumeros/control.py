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

salida = interfaz.decision(baseEntrada, baseSalida, numero)

print("El número {} en base {} es: {}".format(numero, baseSalida, salida))