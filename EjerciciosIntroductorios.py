from math import pi
from multiprocessing.dummy import Value

#Ejercicio1
#Dada una cantidad de segundos, realice un algoritmo que los convierta a unidades horas,minutos
#mostrando en pantalla en formato "horas:minutos
print("Ejercicio 1: ")
ts= input('Dame el tiempo en segundos que deseas convertir: ')
ts=float(ts)
tm=ts/60
th=ts/3600
print("El tiempo en minutos es: ",tm)
print("El tiempo en horas es: ",th)
print("")
print("")
print("")

#Ejercicio 2
#¿Qué radio debe tener una esfera, para que su volumen sea el mismo al de un cubo de lado 5 cm?
print("Ejercicio 2: ")
lc=5
r=(((lc**3)*3)/(4*3.1415926))**(1/3)
print("El radio necesario para que ambos volúmenes sean iguales es: ",r," cm")
print("")
print("")
print("")

#Ejercicio 3
#¿Cuantas veces supera, el area de un cubo, al area de una esfera, si el lado del cubo es 10 cm. Y el radio de la esfera 2 cm ? 
print("Ejercicio 3")
Ac=6*(10**2)
Ae=4*pi*(2**2)
e=Ac/Ae
print("La cantidad de veces que el volúmen del cubo sobrepasa al volúmen de la esfera es: ",e)
print("")
print("")
print("")

#Ejercicio 4
#Realice un código, que permita la conversión de millas a km y km a millas
print("Ejercicio 4")
print("1. Conversión de millas a kilométros")
print("2. Conversión de kilométros a millas")
while True:
    try:
        o=input('Qué conversión deseas hacer?: ')
        o=float(o)
    except ValueError:
        print("Debes escribir un número")
    if o<1 or o>2:
        print("La opción que diste es incorrecta")
        continue
    else:
        break

if o==1:
    m=input('Dame la cantidad de millas que deseas convertir: ')
    m=float(m)
    k=m*1.609344
    print(m," millas son ",k," kilométros")

if o==2:
    k=input('Dame la cantidad de kilométros que deseas convertir: ')
    k=float(k)
    m=k/1.609344
    print(k," kilométros son ",m," millas")

print("")
print("")
print("")

#Ejercicio 5
#Dadas las coordenadas P1(5,4,5) y P2(0,10,9). Realice un codigo que determine la distancia entre ambos puntos
print("Ejercicio 5")
P1x= 5
P2x= 0
dx=  P2x-P1x

P1y= 4
P2y= 10
dy=  P2y-P1y

P1z= 5
P2z= 9
dz=  P2z-P1z

d=((dx**2)+(dy**2)+(dz**2))**(1/2)
print("La distancia entre los puntos P1(5,4,5) y P2(0,10,9) es: ",d)
print("")
print("")
print("")

#Ejercicio 6
#La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas, 
#con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 3 calificaciones definidas.
#Realice un algoritmo que calcule la nota necesaria de la última nota para pasar la materia.
print("Ejercicio 6")
while True:
    try:
        n1=input('Dame la primera nota: ')
        n1=float(n1)
    except ValueError:
        print("Debes escribir un número")
        continue
    if n1>5 or n1<0:
        print("La primera nota es incorrecta")
        continue
    else:
        break

nf1=n1*.15

while True:
    try:
        n2=input('Dame la segunda nota: ')
        n2=float(n2)
    except ValueError:
        print("Debes escribir un número")
        continue
    if n2>5 or n2<0:
        print("La segunda nota es incorrecta")
        continue
    else:
        break

nf2=n2*0.25

while True:
    try:
        n3=input('Dame la tercera nota: ')
        n3=float(n3)
    except ValueError:
        print("Debes escribir un número")
        continue

    if n3>5 or n3<0:
        print("La tercera nota es incorrecta")
        continue
    else:
        break

nf3=n3*0.2

nfp=nf1+nf2+nf3
n4=(3-nfp)/0.4
print("La nota que le hace falta para ganar la materia en 3 es: ",n4)
print("")
print("")
print("")

#Ejercicio 7
#La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas,
#con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 2 calificaciones definidas.
#Realice un algoritmo que calcule la nota necesaria de las dos últimas notas para pasar la materia.
print("Ejercicio 7")
while True:
    try:
        n1=input('Dame la primera nota: ')
        n1=float(n1)
    except ValueError:
        print("Debes escribir un número")
        continue
    if n1>5 or n1<0:
        print("La primera nota es incorrecta")
        continue
    else:
        break

nf1=n1*.15

while True:
    try:
        n2=input('Dame la segunda nota: ')
        n2=float(n2)
    except ValueError:
        print("Debes escribir un número")
        continue
    if n2>5 or n2<0:
        print("La segunda nota es incorrecta")
        continue
    else:
        break

nf2=n2*0.25
nfp=nf1+nf2
a=3-nfp
print("La nota acumulada hasta el momento es: ",nfp)
print("Intenta aproximar la nota que deseas sacar: ")

while True:
    try:
        n3=input('Dame la tercera nota: ')
        n3=float(n3)
    except ValueError:
        print("Debes escribir un número")
        continue

    if n3>5 or n3<0:
        print("La tercera nota es incorrecta")
        continue
    else:
        break
n4= (a-(0.2*n3))/0.4
print("Las notas finales necesarias para pasar la materia son: ")
print("La tercera nota necesaria, con un porcentaje de 20/100, es: ",n3)
print("La cuarta nota necesaria, con un porcentaje de 40/100, es: ",n4)
print("")
print("")
print("")

#Ejercicio 8
#Cuatro compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
#El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. El servicio se
#prestará solo de ida.
#Sin embargo, los cuatro no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
#debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
#utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre los cuatro.
#A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:
print("Ejercicio 8")
tf=15000
J=(15000/4)+(15000/3)+15000+(10000/4)
C=(15000/4)+(15000/3)+(10000/4)
Jo=(15000/4)+(15000/2)+(10000/4)
M=(15000/4)+(15000/3)+(15000/2)+(10000/4)

print("EL dinero total que debe pagar Juan es: ",J," $")
print("EL dinero total que debe pagar Camila: ",C," $")
print("EL dinero total que debe pagar José: ",Jo," $")
print("EL dinero total que debe pagar María es",M," $")
print("")
print("")
print("")

#Ejercicio 9
#El salario mensual de un empleado se calcula teniendo en cuenta el numero de seguros vendidos,
#en donde el precio de cada seguro es de $120000. 
#Para los primeros 20 seguros, la comisión es del 20%.
#Para los siguientes 100 seguros las comisión es del 30%. 
#Para los siguientes seguros vendidos. La comisión es de 10%.

print("Ejercicio 9")
print("Punto a")
st=435
c20=120000*20*0.2
c30=120000*100*0.3
cr=(st-120)*120000*0.1
pt=c20+c30+cr
print("El salario total del trabajor para ",st," seguros vendidos es: ",pt," $")
print("")
print("")
print("punto b")
p20=20*120000*0.2
p30=100*0.3*120000
sr=(10000000-(p20+p30))/12000
sr=int(sr)
st=100+20+sr
print("La cantidad total de seguros que debe vender para ganar $10000000 es: ",st)
print("")
print("")
print("punto c")
sr=(15000000-(p20+p30))/12000
sr=int(sr)
st=100+20+sr
pr=st/16
print("El promedio de seguros vendidos por día es: ",pr)
print("")
print("")
print("")

#Ejercicio 10
#El salario de un empleado de una empresa se calcula, utilizando como base el 
#salario minimo, más un apoyo del 10% en transporte, y uno de 5% por gastos varios.
#Además se paga una comisión de acuerdo al numero de ventas de los siguientes productos:
#a) Realice un algoritmo que calcule el salario del empleado teniendo en cuenta el numero de ventas realizadas 
#b) Uno de los directivos, quiere que la comisión de cada uno de los productos no supere los $2000
   #¿Qué productos deben cambiar en su porcentaje de comision?
#c) Otro directivo desea que la comisión de cada producto se fije en $1900, 
   #¿en cuanto se deben fijar las comisiones de los productos

print("Ejercicio 10")
print("Punto a: ")
se=1000000
at=se*0.1
agv=se*0.05

while True:
    try:
        z=input("Dame la cantidad total de zapatos vendidos: ")
        z=int(z)
    except ValueError:
        continue
    if z<0:
        print("La cantidad dada es incorrecta")
        print("Introduce otro valor")
    else:
        break

zt=z*50000*0.05

while True:
    try:
        Te=input("Dame la cantidad total de tenis vendidos: ")
        Te=int(Te)
    except ValueError:
        continue
    if Te<0:
        print("La cantidad dada es incorrecta")
        print("Introduce otro valor")
    else:
        break

Tet=Te*70000*0.04

while True:
    try:
        Ca=input("Dame la cantidad total de camisas vendidas: ")
        Ca=int(Ca)
    except ValueError:
        continue
    if Ca<0:
        print("La cantidad dada es incorrecta")
        print("Introduce otro valor")
    else:
        break

Cat=Ca*40000*0.06

while True:
    try:
        Co=input("Dame la cantidad total de corbatas vendidas: ")
        Co=int(Co)
    except ValueError:
        continue
    if Co<0:
        print("La cantidad dada es incorrecta")
        print("Introduce otro valor")
    else:
        break

Cot=Co*25000*0.07

while True:
    try:
        Pa=input("Dame la cantidad total de pantalones vendidos: ")
        Pa=int(Pa)
    except ValueError:
        continue
    if Pa<0:
        print("La cantidad dada es incorrecta")
        print("Introduce otro valor")
    else:
        break

Pat=Pa*35000*0.05

while True:
    try:
        Bl=input("Dame la cantidad total de blusas vendidas: ")
        Bl=int(Bl)
    except ValueError:
        continue
    if Bl<0:
        print("La cantidad dada es incorrecta")
        print("Introduce otro valor")
    else:
        break

Blt=Bl*80000*0.03

while True:
    try:
        Ve=input("Dame la cantidad total de vestidos vendidos: ")
        Ve=int(Ve)
    except ValueError:
        continue
    if Ve<0:
        print("La cantidad dada es incorrecta")
        print("Introduce otro valor")
    else:
        break

Vet=Ve*95000*0.02

while True:
    try:
        Me=input("Dame la cantidad total de medias vendidas: ")
        Me=int(Me)
    except ValueError:
        continue
    if Me<0:
        print("La cantidad dada es incorrecta")
        print("Introduce otro valor")
    else:
        break

Met=Me*10000*0.08
St=se+at+agv+zt+Tet+Cat+Cot+Pat+Blt+Vet+Met
print("El salario total de la persona es: ",St," $")
print("")
print("")

print("Punto b: ")

cz=int(50000*0.05)
cT=int(70000*0.04)
cCa=int(40000*0.06)
cCo=int(25000*0.07)
cPa=int(35000*0.05)
cBl=int(80000*0.03)
cVe=int(95000*0.02)
cMe=int(10000*0.08)

cp=[cz,cT,cCa,cCo,cPa,cBl,cVe,cMe]

for k in cp:
    if k>2000:
        i=cp.index(k)
        if i==0:
            print("La comisión de los zapatos debe ser rebajada")
        else:
            if i==1:
                print("La comisión de los tenis debe ser rebajada")
            else:
                if i==2:
                    print("La comisición de las camisas debe ser rebajada")
                else:
                    if i==3:
                        print("La comisión de las corbatas debe ser rebajada")
                    else:
                        if i==4:
                            print("La comisión de los pantalones debe ser rebajada")
                        else:
                            if i==5:
                                print("La comisión de las blusas debe ser rebajada")
                            else:
                                if i==6:
                                    print("La comisión de los vestidos debe ser rebajada")
                                else:
                                    if i==7:
                                        print("La comisión de las medias debe ser rebajada")

print("Los elementos anteriores deben ser estudiados para rebajar su comisión")
print("")
print("")

print("Punto c")
cnz=(190000/50000)
cnT=(190000/70000)
cnCa=(190000/40000)
cnCo=(190000/25000)
cnPa=(190000/35000)
cnBl=(190000/80000)
cnVe=(190000/95000)
cnMe=(190000/10000)

print("La comisión de los zapatos debe ser fijada en: ",cnz,"%")
print("La comisión de los tenis debe ser fijada en: ",cnT,"%")
print("La comisión de las camisas debe ser fijada en: ",cnCa,"%")
print("La comisión de las corbatas debe ser fijada en: ",cnCo,"%")
print("La comisión de los pantalones debe ser fijada en: ",cnPa,"%")
print("La comisión de las blusas debe ser fijada en: ",cnBl,"%")
print("La comisión de los vestidos debe ser fijada en: ",cnVe,"%")
print("La comisión de las medias debe ser fijada en: ",cnMe,"%")
