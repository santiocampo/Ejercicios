# Métodos de las listas
# Métodos inplace (Métodos que afectan implicitamente las variables, y pueden o no devolver un resultado)
lista= [1, "a", 2, 3, "b"]
lista.append("1000")
lista.append(10)
lista.pop(1)
lista.pop(4)
lista.insert(2, "Santiago")
lista.insert(3, "Ocampo")
print(lista)

for i in [2,2,3]:
    if (type(lista[i])== str):
        lista.pop((i))
s= sum(lista)
print(s,"\n\n")

#Sumar los elementos de la lista sin afectar lista3 

lista3= [1, 2, 100, 3, "b", "Pachon", 10, "holamundo", 5]

lista3Copia=lista3.copy()

for j in [4,4,5]:
    if (type(lista3Copia[j])== str):
        lista3Copia.pop(j)

s1= sum(lista3Copia)
print(s1)


#Organice los elementos de la lista3 con el método sort. Es inplace?

lista3Copia.sort(reverse= True)
print(lista3Copia)

#Indexado listas

listaNueva= [1,2,3,4,5,"hola", "cruel", "mundo", 100]

#Extraer el primer elemento de dos maneras
print(listaNueva[0], listaNueva[-9])
#Extraer el último elemento de dos maneras.
print(listaNueva[8], listaNueva[-1])
#Extraer el elemento de la mitad de dos maneras
print(listaNueva[4], listaNueva[-5])

#Slicing
#Extraer cada elemento de dos en dos
print(listaNueva[0:9:2])
#Extraer hasta la mitad de la cadena 
print(listaNueva[0:5])
#Extraer desde la mitad de la cadena en adelante
print(listaNueva[5::])
#Extraer los elementos que son strings
print(listaNueva[5:8])
#Extraer los elementos que son enteros
print(listaNueva[0:5] + [listaNueva[-1]])
