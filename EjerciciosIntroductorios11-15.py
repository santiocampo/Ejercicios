#Ejercicio 11
#Un auto acelera de manera uniforme 0.5 km/s², 
#a) ¿cuantas horas deben pasar para alcanzar la velocidad de la luz?
#b) ¿qué distancia se habrá recorrido? (suponga que es posible alcanzar la velocidad de la luz)

a=0.5
v0=0
v=299792.48
ts=v/a
th=ts/3600
print("EL tiempo en horas que demora para llegar hasta ",v,"  m/ses: ",th," h")
print("")
print("")

x=(0.5*a*(ts**2))/1000
print("La distancia recorrida total será: ",x," km")
print("")
print("")

#Ejercicio 12
#Un proyectil es lanzado verticalmente hacia arriba, calcule la velocidad inicial que debe tener para 
#alcanzar una altura dada.
y0= input("Dame la altura inicial del proyectil en metros: ")
y0= float(y0)

y= input("Dame la altura final del cuerpo en metros: ")
y= float(y)

g=9.8
v0= (2*g*(y-y0))**(1/2)
print("")
print("")
print("La velocidad inicial que necesita el cuerpo para llegar a ",y," metros partiendo de ",y0," metros es: ",v0," m/s")
print("")
print("")

#Ejercicio 13
#Un proyectil es lanzado siguiendo una trayectoria parabólica, calcule el ángulo y la velocidad inicial
#que debe tener para alcanzar una distancia horizontal y vertical dada.
from math import asin, pi
Xmax= float(input("Dame la distancia horizontal total que se desea alcanzar en metros: "))
Ymax= float(input("Dame la altura máxima que se desea alcanzar en metros: "))
Y0= float(input("Dame la altura inicial del cuerpo: ")) 
t= float(input("Dame el tiempo de vuelo del proyectil: "))

g=9.8
Vox=Xmax/t
Voy=0.5*g*(t**2)

Vo=((Vox**2)+(Voy**2))**(1/2)
ang= asin(Voy/Vo)
ang= ang*(180/pi)
print("")
print("")

print("La velocidad inicial necesaria es: ",Vo," m/s")
print("El ángulo de lanzamiento necesario es: ",ang," grados")

#Ejercicio 14
#Un atleta inicia su entrenamiento, desde el punto de partida de una pista, a una velocidad constante de 3m/s. 
#Diez segundos después otro atleta empieza su recorrido a una velocidad constante de 5m/s. ¿Cuánto tiempo 
#habrá pasado para que el segundo atleta alcance al primero?
v1=3
v2=5
xo1=30
t=xo1/(v2-v1)
print("El tiempo necesario para que ambos se encuentren es: ",t+10," segundos")

#Ejercicio 15
#Dos automoviles realizan una carrera. El primero de ellos acelera a razón constante de 3m/s², el segundo 
#a razón de 5m/s². Si el segundo de ellos empieza su recorrido 10 segundos después que el primero ha empezado.
#¿Cuanto tiempo habrá transcurrido cuando ambos se encuentran?
a1= 3
a2= 5

xo1=0.5*a1*(10**2)
t=(30+((900+(4*150)))**(1/2))/2
print("EL tiempo transcurrido hasta que se encuentran es: ",t+10," segundos")