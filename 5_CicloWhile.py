#Desarrolle un ciclo while infinito
#a=3
#while a!=0:
#    print(a)

#Cómo protegerse de un ciclo infinito
contador=0
while True:
    print("Ciclo ejecutado {} veces".format(contador))
    contador=contador+1
    if contador==100:
        break
print("")
print("")

#Realice un ciclo while con un número secreto, cada vez que se ejecute un ciclo, el programa pide adivinar
#el número, en caso de no ser acertado, se debe mostrar un mensaje diciendo: "Estas atrapado",
# y en caso contrario, terminar el ciclo y avisar que el número es correcto.
import random
a= random.randint(1,10)
while True:
    try:
        ns= int(input("Dame el número secreto: "))
    except ValueError:
        continue
    if ns==a:
        print("El número es correcto")
        break
    else:
        print("Estas atrapado")
        print("Ingresa otro número")
        print("")
#Realice un ciclo while que imprima los números del 10 al 100, separados por guión sin salto de guía 
contador=10
while contador<101:
    print(contador,end="-")
    contador=contador+1
print("")
print("")

#Mostrar en pantalla los números del 200 al 100 utilizando ciclo while

contador= 200
while contador>99:
    print(contador)
    contador= contador-1
print("")
print("")
#Mostrar en pantalla los números del 200 al 100 utilizando ciclo while
#Haga que no haya un salto de línea
contador= 200
while contador>99:
    print(contador,end=" ")
    contador= contador-1
print("")
print("")
#Mostrar en pantalla los números del 200 al 100 utilizando ciclo while
#Haga que el salto de línea se haga cada múltiplo de 10
contador= 200
ciclos= 1

while contador>=100:
    if (str(contador)[-1] in "098765432"):
        print(contador, end=" ")
        contador
    else:
        print(contador,end="\n")
    contador=contador-1
print("")
print("")

#Pida a un usuario que ingrese números, en caso de que así lo desee
#De los números calcule cual es el mayor de los ingresados
#Si el usuario no desea ingresar más números el ciclo debe terminar
#respuesta="Si"
#mayor= -99999999999
#while respuesta=="Si":
#    respuesta= input("Desea ingresar un número?: ")
#    if respuesta== "Si":
#        número=float(input("Ingrese el número: "))
#        if número > mayor:
#            mayor=número
#    else:
#        respuesta=="No"
#
#print("El mayor de los números ingresadoes es: ",mayor)

respuesta="Si"
listan= []
while respuesta=="Si":
    respuesta=input("Desea ingresar un número: ")
    if respuesta == "Si":
        n=float(input("Ingrese un número: "))
        listan.append(n)
    else:
        respuesta=="No"

print(listan)
print("EL mayor de los números ingresados es: ",max(listan))
print("")
print("")
