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