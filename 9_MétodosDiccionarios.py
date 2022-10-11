# 04/10/2022

# Diccionarios y sus métodos
# Son elementos compuestos pro clave: valor

import operator

diccionario= {"Cristian Pachon": 3.0, "Daniel Quintero": 4.0, "Esteban Chavez": 5.0, "Margarita María": 3.0}

#Acceder a elementos del diccionario

print(diccionario["Cristian Pachon"])
print(diccionario["Daniel Quintero"])
print(diccionario["Esteban Chavez"])
print(diccionario["Margarita María"])
print(diccionario.get(("Juan David Gonzales"), "No existe esta clave"))

try: 
    print(diccionario["Juan David Gonzales"])
    1/0
except: 
    print("Esto es un error, el programa continua")
print("--------------\n\n")

#Extraer todas las claves del diccionario
print(diccionario.keys())

#Extraer todos los valores del diccionario

print(diccionario.values())

#Ejercicio: imprimir utilizando un ciclo for todas las claves del diccionario

listaclaves= list(diccionario.keys())

for i in range(len(listaclaves)):
    print("La",i+1,"clave del diccionario es: ",listaclaves[i])

print("\n")
listavalores= list(diccionario.values())

for j in range(len(listavalores)):
    print("El",j+1,"valor del diccionario es: ",listavalores[j])

print("\n")

print(diccionario.items())

#Imprimir las parejas utilizando el método items

for pareja in list(diccionario.items()):
    print(pareja[0] +"-"+ str(pareja[1]))

for key, value in list(diccionario.items()): #Desempaquetado 
    print(key + "-" + str(value))
print("\n")

#Cómo cambiar los valores del diccionario

diccionario["Cristian Pachon"] = 5.0
print(diccionario)
print("\n")

#Ejercicio: Cambiar todos los valores del diccionario a 0.0
for k in list(diccionario.keys()):
    diccionario[k]= 0.0

print(diccionario)


#Ejercicio: Cambiar los valores del diccionario de la siguiente manera:
#           Si es mujer 5.0 y si es hombre 0.0

for nombre in diccionario.keys():
    if nombre[-1] == "a":
        diccionario[nombre] = 5.0
    else:
        diccionario[nombre] = 0.0

print(diccionario)

#No es posible hacer copas de diccionarios en Python
#Hacer una copia del diccionario y cambiar las notas a 5
diccionarioCopia= diccionario
diccionarioCopia= diccionario.copy()
for m in diccionarioCopia.keys():
    diccionarioCopia[m]= 5.0

print(diccionario)
print(diccionarioCopia)

print("\n")

#Eliminar una clave del diccionario

#del diccionario["Cristian Pachon"]
#print(diccionario)
#print(diccionario)

#Ejercicio: Con lo visto anteriormente, como cambiar la clave Margarita Maria a Margarita Rosa
vce= diccionario["Margarita María"]
del diccionario["Margarita María"]

diccionario["Margarita Rosa"]= vce
print(diccionario)
print("\n")

#Almacenelos de tal manera que sea posible acceder a la calificacion con nombre y materia 
#Nombre                         Materias
#                    Cuantica Etica Deportes Lenguas
#Juan Gutierrez        2.0     5.0     1.3     3.2
#Maria Snowden         3.1     4.9     2.2     1.1
#Pedro Gonzalez        5.0     3.8     3.1     4.1
#Angelica Lozano       2.1     2.7     4.1     3.2
#Pablo Iglesias        3.2     1.6     5.0     1.2
#Mariana Pajon         2.2     2.5     4.9     3.3
#Esteban Loaiza        2.1     3.4     3.8     4.3
#Daniela Pineda        5.0     4.3     2.7     1.2
#Esteban Vazco         3.1     5.0     1.6     3.2
#Enilse Lopez          5.0     2.2     2.5     5.0
#Cristian Playonero    0.5     1.1     3.4     3.2
#A pedal:
diccionarionotas= {
    "Juan Gutierrez":{"Cuantica": 2.0, "Etica": 5.0, "Deportes": 1.3, "Lenguas": 3.2}, 
    "Maria Snowden": {"Cuantica": 3.1, "Etica": 4.9, "Deportes": 2.2, "Lenguas": 1.1}, 
    "Pedro Gonzales": {"Cuantica": 5.0, "Etica": 3.8, "Deportes": 3.1, "Lenguas": 4.1},
    "Angelica Lozano": {"Cuantica": 2.1, "Etica": 2.7, "Deportes": 4.1, "Lenguas": 3.2}, 
    "Pablo Iglesias": {"Cuantica": 3.2, "Etica": 1.6, "Deportes": 5.0, "Lenguas": 1.2}, 
    "Mariana Pajon": {"Cuantica": 2.2, "Etica": 2.5, "Deportes": 4.9, "Lenguas": 3.3}, 
    "Esteban Loaiza": {"Cuantica": 2.1, "Etica": 3.4, "Deportes": 3.8, "Lenguas": 4.3}, 
    "Daniela Pineda": {"Cuantica": 5.0, "Etica": 4.3, "Deportes": 2.7, "Lenguas": 1.2}, 
    "Esteban Vazco": {"Cuantica": 3.1, "Etica": 5.0, "Deportes": 1.6, "Lenguas": 3.2}, 
    "Enilse Lopez": {"Cuantica": 5.0, "Etica": 2.2, "Deportes": 2.5, "Lenguas": 5.0}, 
    "Cristian Plamoyero": {"Cuantica": 0.5, "Etica": 1.1, "Deportes": 3.4, "Lenguas": 3.2}
    }

#nombre= input("Dame el nombre de la persona: ") 
#materia= input("Dame el nombre de la materia: ")
#print("La nota de ",nombre,"en la materia",materia,"es: ",diccionarionotas[nombre][materia],"\n\n")

#Método optimizado
data= [
    ["Juan Gutierrez",     2.0,  5.0,  1.3,  3.2], 
    ["Maria Snowden",      3.1,  4.9,  2.2,  1.1], 
    ["Pedro Gonzales",     5.0,  3.8,  3.1,  4.1],
    ["Angelica Lozano",    2.1,  2.7,  4.1,  3.2], 
    ["Pablo Iglesias",     3.2,  1.6,  5.0,  1.2], 
    ["Mariana Pajon",      2.2,  2.5,  4.9,  3.3], 
    ["Esteban Loaiza",     2.1,  3.4,  3.8,  4.3], 
    ["Daniela Pineda",     5.0,  4.3,  2.7,  1.2], 
    ["Esteban Vazco",      3.1,  5.0,  1.6,  3.2], 
    ["Enilse Lopez",       5.0,  2.2,  2.5,  5.0], 
    ["Cristian Plamoyero", 0.5,  1.1,  3.4,  3.2]
    ]

diccionarioCalificaciones= {}

for estudiante in data:
    diccionarioCalificaciones[estudiante[0]]= {"Cuantica": estudiante [1], "Etica": estudiante[2],
                                               "Deportes": estudiante[3], "Lenguas": estudiante[4]}

print(diccionarioCalificaciones,"\n\n")

# Calcular el promedio de calificaciones de cada estudiante usando diccionarioCalificaciones
# Determinar los 3 estudiantes con mejor y peor promedio
# Calcular el promedio de las 4 materias
# Promedios Estudiantes

diccionarioPromedios= {}
keys= diccionarioCalificaciones.keys()

for key in keys:
    diccionarioPromedios[key]= (diccionarioCalificaciones[key]["Cuantica"]+diccionarioCalificaciones[key]["Etica"]+diccionarioCalificaciones[key]["Deportes"]+diccionarioCalificaciones[key]["Lenguas"])/4

for Prom in diccionarioPromedios:
    print("El promedio de notas de",Prom,"fue: ",diccionarioPromedios[Prom])
print("\n\n")

# Mejores y peores promedios

sort_Promediosp= sorted(diccionarioPromedios.items(), key= operator.itemgetter(1))
print("Los peores promedios son: ")
for i in range(3):
    print(str(sort_Promediosp[i][0]),":",str(sort_Promediosp[i][1]))
print("\n\n")

sort_Promediosm= sorted(diccionarioPromedios.items(), key= operator.itemgetter(1), reverse= True)
print("Los mejores promedios son: ")
for j in range(3):
    print(str(sort_Promediosm[j][0]),":",str(sort_Promediosm[j][1]))

print("\n\n")

# Promedios Materias
diccionarionotasCuantica= {}
diccionarionotasEtica= {}
diccionarionotasDeportes= {}
diccionarionotasLenguas= {}

for key in keys:
    diccionarionotasCuantica[key]= (diccionarioCalificaciones[key]["Cuantica"])
for key in keys:
    diccionarionotasEtica[key]= (diccionarioCalificaciones[key]["Etica"])
for key in keys:
    diccionarionotasDeportes[key]= (diccionarioCalificaciones[key]["Deportes"])
for key in keys:
    diccionarionotasLenguas[key]= (diccionarioCalificaciones[key]["Lenguas"])

notasCuantica= list(diccionarionotasCuantica.values())
notasEtica=  list(diccionarionotasEtica.values())
notasDeportes= list(diccionarionotasDeportes.values())
notasLenguas=  list(diccionarionotasLenguas.values())

promCuantica= (sum(notasCuantica))/len(notasCuantica)
promEtica= (sum(notasEtica))/len(notasEtica)
promDeportes= (sum(notasDeportes))/len(notasDeportes)
promLenguas= (sum(notasLenguas))/len(notasLenguas)

print("El promedio de Cuantica es: ",promCuantica)
print("El promedio de Etica es: ",promEtica)
print("El promedio de Deportes es: ",promDeportes)
print("El promedio de Lenguas es: ",promLenguas)
print("\n\n")

