# Crear variables y asignarles los siguientes tipos de datos

#Enteros: 1,2,3,999
#Luego reste sucesivamente del ultimo al primero y almacenelo 
# en una variable llamada resultado1

a=1
b=2
c=3
d=999
resultado1=d-c-b-a
print("EL resultado 1 es: ",resultado1)

#Flotantes: 15.2, 29.5, 18.28
#Luego divida sucesivamente del primero al ultimo
#Y almacenelo en una variable llamada resultado2

a2=15.2
b2=29.5
c2=18.28
resultado2=(a2/b2)/c2
print("EL resultado 2 es: ",resultado2)

#Strings: "123", "Cristian"
#Luego sume ambas variables y determine si la 
# operación es posible, si es así almacenelo en una variable
#de su elección

a3="123"
b3="Cristian"
resultado3=a3+b3
print("La operación si es posible, se genera un string nuevo dado por la unión de los anteriores strings")
print("EL resultado 3 es: ",resultado3)

######## para pensar ###############

#Busque una manera de convertir
#Un entero a un flotante
e1=5
f1=float(e1)
print("El entero ",e1," se ha convertivo en el flotante ",f1)
#Un flotante a un entero
f2=4.5
e2=int(f2)
print("El flotante ",f2," se ha convertivo en el entero ",e2)

#Un string a un entero y flotante
#String a entero
s1="123"
e3=int(s1)
print("El string ",s1," se ha convertivo en el entero ",e3)

#String a flotante

s2="32.425"
f3=float(s2)
print("El string ",s2," se ha convertivo en el flotante ",f3)

#Un numero a un string

n1=32.458
s3=str(n1)
print("EL número flotante ",n1," se ha convertido en la string ",s3)
######################################################################