#Ejercicio 1
#a) Pedir al usuario que ingrese su edad, luego imprimir en pantalla si es mayor o menor de edad
#b) Pedir al usuario que ingrese su salario, luego imprimir si su salario es alto o bajo, (salario alto > $ 5000000)
#c) Pedir al usuario que ingrese 3 notas, luego avisar si aprueba o reprueba la materia
print("Ejercicio 1: ")
print("Punto a: ")
print("")
edad= int(input("Dame tu edad: "))
print((edad>=18 and "Es mayor de edad") or "Es menor de edad")
print("")
print("")

print("Punto b: ")
salario= float(input("Dame tu salario mensual en pesos: "))
print((salario>5000000 and "Su salario es alto") or "Su salario es bajo")
print("")
print("")

print("Punto c: ")
while True:
    try:
        nota1= float(input("Dame la primera nota: "))
    except ValueError:
        continue
    if nota1<0 or nota1>5:
        print("El valor ingresado es incorrecto")
        print("Ingresa otro valor")
        print("")
    else:
        break

while True:
    try:
        nota2= float(input("Dame la segunda nota: "))
    except ValueError:
        continue
    if nota2<0 or nota2>5:
        print("El valor ingresado es incorrecto")
        print("Ingresa otro valor")
        print("")
    else:
        break

while True:
    try:
        nota3= float(input("Dame la tercera nota: "))
    except ValueError:
        continue
    if nota3<0 or nota3>5:
        print("El valor ingresado es incorrecto")
        print("Ingresa otro valor")
        print("")
    else:
        break

prom=(nota1+nota2+nota3)/3
print((prom>=3 and ("Ha ganado la materia en: ",prom)) or ("Ha perdido la materia en: ",prom))
print("")
print("")

#Ejercicio 2
#a) Determine el numero de metodos que tienen los strings, enteros, flotantes, listas, diccionarios,
#b) Determine el tipo de variable resultado de las siguientes operaciones:
print("Ejercicio 2: ")
print("")
print("Punto a: ")

print("Los métodos para strings son: ",dir(str))
print("")
print("Los métodos para enteros son: ",dir(int))
print("")
print("Los métodos para flotantes son: ",dir(float))
print("")
print("Los métodos para listas son: ",dir(list))
print("")
print("Los métodos para diccionarios son: ",dir(dict))
print("")
print("")

print("Punto b: ")
print("El tipo de la operación []+[] es: ",str(type([]+[])))
print("El tipo de la operación [1]+[1,2,3] es: ",str(type([1]+[1,2,3])))
print("El tipo de la operación (1,)+(1,2,3) es: ",str(type((1,)+(1,2,3))))
print("El tipo de la operación (1,2,3)+(1,) es: ",str(type((1,2,3)+(1,))))
print("EL tipo de la operación {'a','b'} | {'c'} es: ",str(type({"a","b"} | {"c"})))
print("EL tipo de la operación {'a','b'} & {'a','c'} es: ",str(type({"a","b"} & {"a","c"})))
print("EL tipo de la operación False and 2 es: ",str(type(False and 2)))
print("EL tipo de la operación True and 5 es: ",str(type(True and 5)))
print("EL tipo de la operación False or 0 es: ",str(type(False or 0)))
print("EL tipo de la operación True or 5 es: ",str(type(True or 5)))
print("EL tipo de la operación 1 and True es: ",str(type(1 and True)))
print("")
print("")

#Ejercicio 3
#Redondear los siguientes flotantes teniendo en cuenta cifras significativas.
print("Ejercicio 3: ")
print("")
print("La cifra 2.572 redondeada con 0 cifras decimales es: ",round(2.572,0))
print("La cifra 3.789 redondeada con 2 cifras decimales es: ",round(3.789,2))
print("La cifra 0.392 redondeada con 1 cifras decimales es: ",round(0.392,1))
print("La cifra 10.123913 redondeada con 4 cifras decimales es: ",round(10.123913,4))
print("La cifra 14.2293 redondeada con 2 cifras decimales es: ",round(14.2293,2))
print("La cifra 78.2569 redondeada con 1 cifras decimales es: ",round(78.2569,1))
print("")

#Ejercicio 4
#Realizar las siguientes conversiones:
print("Punto a: ")
dec1,dec2,dec3= 512,8,128
print("EL número ",dec1," convertido a binario, octal y hexadecimal es: ",bin(dec1)," ",oct(dec1)," ",hex(dec1))
print("EL número ",dec2," convertido a binario, octal y hexadecimal es: ",bin(dec2)," ",oct(dec2)," ",hex(dec2))
print("EL número ",dec3," convertido a binario, octal y hexadecimal es: ",bin(dec3)," ",oct(dec3)," ",hex(dec3))
print("")
print("")
print("Punto b: ")
bin1,bin2,bin3= "1000","10","101"
print("EL número binario ",bin1," convertido a decimal es: ",int(bin1,2))
print("EL número binario ",bin2," convertido a decimal es: ",int(bin2,2))
print("EL número binario ",bin3," convertido a decimal es: ",int(bin3,2))
print("")
print("")
print("Punto c: ")
oct1,oct2,oct3= "563","7","64"
print("EL número octal ",oct1," como decimal es: ",int(oct1,8))
print("EL número octal ",oct2," como decimal es: ",int(oct2,8))
print("EL número octal ",oct3," como decimal es: ",int(oct3,8))
print("")
print("")
print("Punto d: ")
hex1,hex2,hex3= "0xABC","0x10A2","0x9FF"
print("EL número hexadecimal ",hex1,"en forma decimal es: ",int(hex1,16))
print("EL número hexadecimal ",hex2,"en forma decimal es: ",int(hex2,16))
print("EL número hexadecimal ",hex3,"en forma decimal es: ",int(hex3,16))