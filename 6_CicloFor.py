#Recorrer los siguientes iterables
cadena= "HolaMundoCruel"
lista1= [1,2,30,100,50,-20]
tupla=(1,2,3,1,2,3,1,2,3)
lista2= [1,-1,1,-1,1,-1]
rango= range(1,100)

for caracter in cadena:
    print(caracter,end="--")
print("")
print("")
for num in lista1:
    print(num)
print("")
for numt in tupla:
    print(numt,end="-")
print("")
for numl in lista2:
    print(numl,end=" - ")
print("")
for k in rango:
    print(k,end="-")
print("")
print("")
print("")

#Recorrer  los números del 1 al 10 utilizando diferentes iterables (por lo menos 4), sin definirlos en una variable
print("Itarable 1: ")
for k in range(1,11):
    print(k,end=("-"))
print("")
print("")
print("Itarable 2: ")
print("")
for num in [1,2,3,4,5,6,7,8,9,10]:
    print(num,end=" ")
print("")
print("")
print("Itarable 3: ")
print("")
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i,end=" ")
print("")
print("")
print("Itarable 4: ")
print("")
for j in {1,2,3,4,5,6,7,8,9,10}:
    print(j,end=" ")
print("")
print("")

#Imprimir los números pares del 0 al 20
for p in range(0,21,2):
    print(p,end=" ")
print("")
print("")

#Imprimir los números múltiplos del 4 del 5 al 30

for m in range(5,31):
    if m%4 == 0:
        print(m)