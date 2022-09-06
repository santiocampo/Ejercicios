#Ejercicio 1
#a) Pedir al usuario que ingrese su edad, luego imprimir en pantalla si es mayor o menor de edad
#b) Pedir al usuario que ingrese su salario, luego imprimir si su salario es alto o bajo, (salario alto > $ 5000000)
#c) Pedir al usuario que ingrese 3 notas, luego avisar si aprueba o reprueba la materia
from operator import truediv


print("Ejercicio 1: ")
print("Punto a: ")
print("")
while True:
    try:
        edad=int(input("Dame tu edad: "))
    except ValueError:
        continue
    if edad<=0:
        print("El valor ingresado es incorrecto")
        print("Ingresa otro valor.")
        print("")
    else:
        break

print((edad>=18 and "Es mayor de edad") or "Es menor de edad")
print("")
print("")

print("Punto b: ")
while True:
    try:
        salario= float(input("Dame tu salario mensual en pesos: "))
    except ValueError:
        continue
    if salario<=0:
        print("El valor ingresado es incorrecto")
        print("Ingresa otro valor.")
        print("")
    else:
        break

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
print("Ejericicio 4: ")
print("")
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
print("")
print("")

#Ejercicio 5
#Formatear (format(<numero>, <regla>)) los siguientes elementos:
print("Ejercicio 5: ")
print("")
print("Punto a: ")
a= 0.52941
b= 2.389
c= 3.5
d= 200000
print("El número ",a," como entero es: ", format(a,".0f"))
print("El número ",a," como flotante con dos deciamles es: ", format(a,".2f"))
print("El número ",a," como flotante con 5 decimales es: ", format(a,".5f"))
print("El número ",a," como notacipon científica con 1 decimal es: ", format(a,".1e"))
print("El número ",a," como notación científica con 2 decimales es: ", format(a,".2e"))

print("El número ",b," como entero es: ", format(b,".0f"))
print("El número ",b," como flotante con dos deciamles es: ", format(b,".2f"))
print("El número ",b," como flotante con 5 decimales es: ", format(b,".5f"))
print("El número ",b," como notacipon científica con 1 decimal es: ", format(b,".1e"))
print("El número ",b," como notación científica con 2 decimales es: ", format(b,".2e"))

print("El número ",c," como entero es: ", format(c,".0f"))
print("El número ",c," como flotante con dos deciamles es: ", format(c,".2f"))
print("El número ",c," como flotante con 5 decimales es: ", format(c,".5f"))
print("El número ",c," como notacipon científica con 1 decimal es: ", format(c,".1e"))
print("El número ",c," como notación científica con 2 decimales es: ", format(c,".2e"))

print("El número ",d," como entero es: ", format(d,".0f"))
print("El número ",d," como flotante con dos deciamles es: ", format(d,".2f"))
print("El número ",d," como flotante con 5 decimales es: ", format(d,".5f"))
print("El número ",d," como notacipon científica con 1 decimal es: ", format(d,".1e"))
print("El número ",d," como notación científica con 2 decimales es: ", format(d,".2e"))
print("")
print("")

print("Punto b: ")
st= "INFORMATICA 3"
print("La string ",st," alineada al centro es: ", format(st,"^20"))
print("La string ",st," alineada a la derecha es: ", format(st,">20"))
print("La string ",st," alineada a la izquierda es: ", format(st,"<20"))
print("")
print("")

print("Punto c: ")
print("")
a= 128
b= 64 
c= 226
print("El número ",a," como binario es: ", bin(a))
print("El número ",a," como octal es: ", oct(a))
print("El número ",a," como hexadecimal es: ", hex(a))
print("")
print("El número ",b," como binario es: ", bin(b))
print("El número ",b," como octal es: ", oct(b))
print("El número ",b," como hexadecimal es: ", hex(b))
print("")
print("El número ",c," como binario es: ", bin(c))
print("El número ",c," como octal es: ", oct(c))
print("El número ",c," como hexadecimal es: ", hex(c))
print("")
print("")

#Ejercicio 6
#Crear las siguientes secuencias:
s1= range(1,501)
s2= range(2,202,2)
s3= range(100,-1,-1)
s4= range(-100,105,5)
print("La secuencia 1 es: ", list(s1))
print("")
print("La secuencia 2 es: ", list(s2))
print("")
print("La secuencia 3 es: ", list(s3))
print("")
print("La secuencia 4 es: ", list(s4))
print("")

#Ejercicio 7
#Cree secuencias enumeradas utilizando las anteriores secuencias
print("Ejercicio 7: ")
print("")
print("La secuencia 1 numerada es: ", list(enumerate(s1)))
print("")
print("La secuencia 2 numerada es: ", list(enumerate(s2)))
print("")
print("La secuencia 3 numerada es: ", list(enumerate(s3)))
print("")
print("La secuencia 4 numerada es: ", list(enumerate(s4)))
print("")

#Ejercicio 8
#A los siguientes iterables,calcule,  el tamaño, la suma de elementos, valor mínimo y máximo
print("Ejercicio 8")
print("")

i1= [200,300,1,2,3,4,231,21,54,6,76, 4, 32, 432, 654, 8, 435, 432]
i2= list(range(2,10002,2))
i3= list(range(302,10001,3))
i4= 'abcdefghijklmnopqrstuvwxyz'

print("EL tamaño del primer iterable es: ",len(i1))
print("La suma de elementos del primer iterable es: ",sum(i1))
print("El valor máximo del primer iterable es: ", max(i1))
print("El valor mínimo del primer iterable es: ", min(i1))
print("")
print("EL tamaño del segundo iterable es: ",len(i2))
print("La suma de elementos del segundo iterable es: ",sum(i2))
print("El valor máximo del segundo iterable es: ", max(i2))
print("El valor mínimo del segundo iterable es: ", min(i2))
print("")
print("EL tamaño del tercer iterable es: ",len(i3))
print("La suma de elementos del tercer iterable es: ",sum(i3))
print("El valor máximo del tercer iterable es: ", max(i3))
print("El valor mínimo del tercer iterable es: ", min(i3))
print("")
print("EL tamaño del cuarto iterable es: ",len(i4))
print("El valor máximo del cuarto iterable es: ", max(i4))
print("El valor mínimo del cuarto iterable es: ", min(i4))