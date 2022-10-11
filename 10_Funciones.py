#Ejemplo1

def saludarEstudiante(nombre):
    saludo= "Hola {}".format(nombre)
    return saludo

nombre= input("Dame tu nombre: ")
saludoRecibido = saludarEstudiante(nombre)
print(saludoRecibido)
print("\n\n")
#Desarrollar una función que reciba dos números y devuelva la suma de los dos

def sumanumeros(numero1,numero2):
    suma= numero1+numero2
    return suma

numero1= float(input("Ingresa un número: "))
numero2= float(input("Ingresa otro número: "))
resultadoSuma= sumanumeros(numero1,numero2)

print("La suma de ",numero1,"y",numero2,"tiene como resultado: ",resultadoSuma)
print("\n\n")

#Desarrollar una función que reciba dos listas y devuelva una nueva lista que devuelva elemento a elemento

def sumaListas(lista1, lista2,n):
    suma= []
    for  k in range(n):
        suma.append(lista1[k]+lista2[k])
    return suma

n= int(input("Ingresa la longitud de las listas: "))
lista1= []
lista2= []
for i in range(n):
    lista1.append(float(input("Ingresa un número: ")))
print("\n")
for j in range(n):
    lista2.append(float(input("Ingresa un número: ")))

resultado= sumaListas(lista1, lista2,n)
print("El resultado de la suma de las listas es: ",resultado)
print("\n\n")

#Desarrollar una función que no reciba parametros y que no retorne valores, pero que sirva para
# imprimir un mensaje de tres líneas

def Mensaje():
    print("Buenas noches\ndulces sueños\ndescansa")

Mensaje()
print("\n\n")
#Desarrollar una función que reciba un diccionario de calificaciones (Nombre: nota) y retorne el promedio.

def promedio(diccionarioNotas):
    totalNotas= 0
    for key in diccionarioNotas.keys():
        totalNotas= diccionarioNotas[key] + totalNotas
    promedio= totalNotas/ len(list(diccionarioNotas.values()))
    return promedio

diccionarioNotas= {"Santiago": 3.0, 
                   "Daniela": 3.5, 
                   "Sálome": 4.2}
promedionotas= promedio(diccionarioNotas)

print("El promedio de las notas fue: ", promedionotas)
#Desarrollar una función que reciba una cantidad indeterminada de productos y retorne su producto

def multiplicacion(*numeros):
    resultado= 1
    for numero in numeros:
        resultado= resultado * numero
    return resultado

salida1= multiplicacion(1,2,2.5)
salida2= multiplicacion(3,2)
print("El producto de todos los números ingresados es: ", salida1)
print("El producto de todos los números ingresados es: ", salida2)
