#Ejercicio 1 
#Realice las siguientes operaciones mentalmente. Intente determinar la respuesta,
#luego verifique en python

a= 1+3-5
print(a)
b= 13/2
print(b)
c= 19//6
print(c)
d= 31%3
print(d)
e= 2**5
print(e)
f= 16**(0.5)
print(f)
g= "Cristian"+"unal"
print(g)
h= "Unal"*5
print(h)
i= [1,2,3]+[4,5,6]
print(i)
j=  [1,2]*4
print(j)
k= (1,2,3)+(4,5,6)
print(k)
l= (1,2)*4
print(l)
m= True and False
print(m)
n= 1 and 2
print(n)
o= 5 and True
print(o)
p= False and 5
print(p)
q= [] and "resultado"
print(q)
r= True and (2,3,4)
print(r)
s= False or True
print(s)
t= 0 or 5
print(t)
u= True or 5
print(u)
v= "resultado" or False
print(v)
w= 5>3
print(w)
x= 2!=2
print(x)
y= 3 =="3"
print(y)
z1= 5> True
print(z1)
a1= True<0
print(a1)
b1= True != False
print(b1)
c1= "abc"<"bcd"
print(c1)
d1= 1 in [1,2,3]
print(d1)
e1= "A" in ("A","B","C")
print(e1)
f1= 1 not in ["A","B","C"]
print(f1)
g1= "A" in {"A","B","C"}
print(g1)

#Ejercicio 2
#¿Qué operaciones puede realizar con los anteriores operadores?
#¿Qué tipos de datos se pueden utilizar con cada uno de los operadores?
print("Operador de asignación: permite asignar valores a una variable")
print("ES posible usarlo con cualquier tipo de dato")
print("")
print("")

print("Operadores arítmeticos: Permiten realizar las operaciones arítmeticas básicas,")
print("tales como suma, resta, multiplicación, división, división entera, potenciación, residuo")
print("Se pueden utilizar con datos númericos y strings")
print("")
print("")

print("Operadores lógicos: permiten realizar operaciones lógicas o comparativas con valores booleanos")
print("Se puede utilizar con cualquier tipo de dato")
print("")
print("")

print("Operadores de comparación: permiten reconocer si una variable es mayor o menor a otra en magnitud")
print("Es posible usarlo con cualquier tipo de dato")
print("")
print("")


print("Operadores de pertenencia: permiten comparar si un dato existe o no dentro de un grupo de datos")
print("Se puede usar con cualquier dato que pueda estar contenido en un grupo de datos")
print("")
print("")

#Ejercicio 3
#De los operadores *, /, +. ¿Cual tiene mayor prioridad?
oa1=3/2*5
oa11=3*2/5
print(oa1)
print(oa11)
print("Tiene primacía el operador / sobre *")
print("")
print("")

oa2=3/2+5
oa22=3+2/5
print(oa2)
print(oa22)
print("Tiene primacía el operador / sobre +")
print("")
print("")

oa3=3*2+5
oa33=3+2*5
print(oa3)
print(oa33)
print("Tiene primacía el operador * sobre +")
print("")
print("")

#Ejercicio 4
#De los operadores *, **. ¿Cual tiene mayor prioridad?

o1=3*2**5
o11=3**2*5
print(o1)
print(o11)
print("En casos donde estén presentes los operadores * y **, siempre tiene primacia el operador **")
print("")
print("")

o2=2*2**3
o22=2**2*3
print(o2)
print(o22)
print("En casos donde estén presentes los operadores * y **, siempre tiene primacia el operador **")
print("")
print("")

o3=2**2**3
print(o3)
print("En casos donde se repite el operador **, el primer número se eleva a las potencias siguientes")
print("")
print("")

#Ejercicio 5
#De los operadores *, /, //, % ¿cual tiene mayor prioridad?:

oe1= 13//6*2
oe11= 27//6*2
print(oe1)
print(oe11)
print("En el caso de estar presente los operadores // y *, tiene primacía el operador //")
print("")
print("")

oe2= 13/6//2
oe22= 13//6/2
print(oe2)
print(oe22)
print("En el caso de estar presente los operadores // y /, tiene primacía el operador //")
print("")
print("")

oe3= 13*6%2
oe33= 13%6*2
print(oe3)
print(oe33)
print("En el caso de estar presente los operadores * y %, tiene primacía el operador %")
print("")
print("")

#Ejercicio 6
#Realice las siguientes operaciones, y determine:
#¿Cuál es el orden de prioridades de los operadores not, and, or?

ol1= not True and False
print(ol1)
print("Cuando se encuentren en una misma operación los operadores not y and, se ejecutara primero el comando not")
print("")
print("")

ol2= True and not False
print(ol2)
print("Cuando se encuentren en una misma operación los operadores not y and, se ejecutara primero el comando not")
print("")
print("")

ol3= True and False or False
print(ol3)
print("Cuando se encuentren en una misma operación los operadores or y and, se ejecutara primero el comando and")
print("")
print("")

ol4= True or False and False
print("Cuando se encuentren en una misma operación los operadores or y and, se ejecutara primero el comando and")
print(ol4)
print("")
print("")

#Ejercicio 7
#Intente determinar mentalmente la salida de las siguientes operaciones
om1= 1 and 2 and 3
print("3")
om2= 1 and 0 and 3
print("0")
om3= 0 and 2 and 3
print("0")
om4= 1 or 2 or 3
print("1")
om5= 1 or 0 or 3
print("1")
om6= 0 or 1 or 2
print("1")
