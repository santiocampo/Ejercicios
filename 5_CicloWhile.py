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
contador=1
while contador<101:
    print(contador,end=" - ")
    contador=contador+1
