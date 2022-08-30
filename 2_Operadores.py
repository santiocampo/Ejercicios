#Operador de asignación

from pickle import FALSE


a=1
b=3
c=5

#Operadores arítmeticos
#Realice las sigguientes operaciones mentalmente

a1=3+9      #12
a2=3.0+9  #12.0
a3=9**0.5   #3.0
a4=2**32    #4294967296
a5=19//2    #9
a6=19%3     #1
a7=9/3
a8="hola "+"mundo"
a9="hola "*3
a10=["A"]+["1","2","3"]
a11=[]+[]
a12=(1,2,3)+(1,) #El tipo de variable tupla se indica con (n,)

print(a12)

#Operadores lógicos
#Realice las siguientes operaciones

l1= True and True
l2= False and True #and da True si ambos son verdaderos
l3= False and False
l4= not True
l5= not False #not da el Booleano contrario 
l6= True or True
l7= False or True #
l8= 1 and 1
l9= 0 and 1
l10= 1 and 3 #todos los enteros son verdaderos, exceptuando el 0(el cual da falso)
l11= 1 and "hola"
l12= 1 or 3
l13= "hola" or "verdadero"
l14= "" or "hola"
l15= "" or False
print(l15)
print(1 and "verdadero")
print(0 and "falso")  #Todos los string son verdaderos, menos el string "" (el cuál es falso)

