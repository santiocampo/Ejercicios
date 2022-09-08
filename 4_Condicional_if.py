#06/09/2022

#Pida al usuario su nombre y su edad. Determine si es mayor de edad, y muestre un mensaje
# en pantalla diciendo: <Nombre>, usted es mayor,menor de edad.

nombre= input("Ingresa tu nombre: ")
while True:
    try:
        edad= int(input("Ingresa tu edad: "))
    except ValueError:
        continue
    if edad<=0:
        print("EL valor ingresado es incorrecto.")
        print("Ingresa otro valor.")
        print("")
    else:
        break

if edad>= 18:
    print("{}, usted es mayor de edad.".format(nombre))
else: 
    print("{}, usted es menor de edad.".format(nombre))
print("")
print("")

#Realice un programa que calcule el mayor de tres números
a= float(input("Ingresa el primer número: "))
b= float(input("Ingresa el segundo número: "))
c= float(input("Ingresa el tercer número: "))

if a>b and a>c:
    print("EL mayor de los tres números es: {}".format(a))
elif b>a and b>c:
    print("EL mayor de los tres números es: {}".format(b))
elif c>a and c>b:
    print("EL mayor de los tres números es: {}".format(c))
print("")
print("")

 #Salario base: 1000000. Realice un programa que calcule el salario de un vendedor,
 #teniendo en cuenta las siguientes condiciones: 
 # ventas: entre [5,20] seguros, aumento del 20% sobre la base.
 # ventas: entre [21,50] seguros, aumento del 30% sobre la base.
 # ventas: entre [51,infinito] seguros, aumento del 35% sobre la base

sb= 1000000
while True:
    try:
        seguros= int(input("Dame la cantidad total de seguros vendidos: "))
    except ValueError:
        continue
    if seguros <=0:
        print("El valor ingresado es incorrecto.")
        print("Ingresa otro valor")
    else:
        break

if 1<=seguros<5:
    print("El salario total es: {}".format(sb))
elif 5<=seguros<=20:
    print("El salario total es: {}".format(sb*1.2))
elif 21<=seguros<=50:
    print("El salario total es: {}".format(sb*1.3))
elif seguros>=51:
    print("El salario total es: {}".format(sb*1.35))

#Una contraseña debe incluir: 
# Mayúsculas
# Mínusculas
# Contenga números
# Caracteres especiales
# Por los menos 8 caracteres en total
# Determine si al ingresar una contraseña, esta cumple todas las condiciones

contraseña= input("Ingresa una contraseña: ")
contraseña= list(contraseña)
numcar= len(contraseña)
contM=0
contmin=0
contnum=0
contce=0

for i in range(0,numcar):
    for M in "ABCDEFGHIJKLMNOPQRSTUUVWXYZ":
        if M in contraseña:
            contM= contM+1

for i in range(0,numcar):
    for m in "abcdefghijklmnopqrstuvwxyz":
        if m in contraseña:
            contmin= contmin+1

for i in range(0,numcar):
    for num in "0123456789":
        if num in contraseña:
            contnum= contnum+1

for i in range(0,numcar):
    for ce in "|°¬!$%&/=¿?¡+~*}]`{[^-_":
        if ce in contraseña:
            contce= contce+1

condicion1= (contM>0)
condicion2= (contmin>0)
condicion3= (contnum>0)
condicion4= (contce>0)
condicion5= (numcar>=8)
contraseña= "".join(contraseña)
if condicion1 and condicion2 and condicion3 and condicion4 and condicion5:
    print("La contraseña ",contraseña," es completa")
else:
    print("La contraseña ",contraseña," es incompleta")

