#################### Funciones entradas / salida #########################

nombre= input("Ingrese su nombre: ") #Interrumpe la ejecución del código hasta que se almacene un valor
print("Su nombre es: ",nombre)
print("")
print("")

#Solicite una edad y muestre por pantalla si es mayor de edad o no
Edad=input("Ingrese su edad actual: ")
Edad=int(Edad)
#forma operadores lógicos
print((Edad >=18 and "Es mayor de edad") or "no es mayor de edad")

#forma if
if Edad>=18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")
print("")
print("")

#Solicite una clave y muestre por pantalla si es correcta o incorrecta

clave_original= 9876
clave_entrada= int(input("Ingrese la clave: "))
#forma operadores lógicos
print((clave_original==clave_entrada and "La clave ingresada es correcta") or "La clave ingresada es incorrecta")

#forma if
if clave_original == clave_entrada:
    print("La clave ingresada es correcta.")
else:
    print("La clave ingresada es incorrecta.")

# ---------------------------- función format ----------------------
#Formato notación científica
número= 192.5678
formato_científico= format(número,"e")
print("El número ",número," en formato científico es: ",formato_científico)
formato_científico2= format(número,".2e")
print("El número ",número," en formato científico con dos décimales es: ",formato_científico2)
formato_científico0= format(número,".0e")
print("El número ",número," en formato científico con cero décimales es: ",formato_científico0)
print("")
print("")

#Formato coma flotante 
#Aproxima correctamente según la cantidad de decimales mostrados por pantalla
numero= 12.90339001
formato_flotante= format(numero,".2f")
print("El número ",numero," en formato flotante con 2 décimales es: ",formato_flotante)
formato_flotante0= format(numero,".0f")
print("El número ",numero," en formato flotante con 0 décimales es: ",formato_flotante0)

numero1= 0.52941
n1e= format(numero1,".0f")
n1f2= format(numero1,".2f")
n1f5= format(numero1,".5f")
n1e1= format(numero1,".1e")
n1e2= format(numero1,".2e")
print("El número ",numero1," como entero es: ",n1e)
print("El número ",numero1," como flotante con dos decimales es: ",n1f2)
print("El número ",numero1," como flotante con cinco decimales es: ",n1f5)
print("El número ",numero1," como notación científica con 1 decimal es: ",n1e1)
print("El número ",numero1," como notación científica con 2 decimal es: ",n1e2)
print("")
print("")


#Formatos strings
string= "Hola mundo"
formato_centrado= format(string,"^50")
formato_derecha= format(string,">50")
formato_izquierda= format(string,"<50")
print("La cadena alineada al centro es: ",formato_centrado)
print("La cadena alineada a la derecha es: ",formato_derecha)
print("La cadena alineada a la izquierda es: ",formato_izquierda)
print("")
print("")

#Funciones de conversión
#Convertir a binario, octal y hexadecimal

decimal= 9
conversion_binario= bin(decimal)
conversion_octal= oct(decimal)
conversion_hexadecimal= hex(decimal)

print("El número ",decimal," como binario es: ",conversion_binario)
print("El número ",decimal," como octal es: ",conversion_octal)
print("El número ",decimal," como hexadecimal es: ",conversion_hexadecimal)

#Conversión a decimal
bin,oct,hex= "1001","11","9"

print("El número ",bin," binario a decimal es: ",int(bin,2))
print("El número ",oct," octal a decimal es: ",int(oct,8))
print("El número ",hex," hexadecimal a decimal es: ",int(hex,16))
print("")
print("")

#Funciones de ayuda
#dir
#permite conocer las funciones para un tipo de dato

cadena= "Hola mundo"
lista=[1,2,3]
entero=10

print("\n Funcionalidades para cadena: \n\n",dir(cadena))
print("\n Funcionalidades para lista: \n\n",dir(lista))
print("\n Funcionalidades para entero: \n\n",dir(entero))
print("")
print("")

#Funcines para Secuencias

print("\n\n Funciones para secuencias: ")
secuencia= range(1,11) #No es necesario poner el salto si es 1
print(list(secuencia))
print("")

secuencia1= range(20,30)
print(list(secuencia1))
print("")

#Números del -10 al 10 con salto 2
secuencia2= range(-10,11, 2)
print(list(secuencia2))
print("")
print("")

#números multiplos del 3 desde -10 hasta 5
secuencia3= range(-9,6, 3)
print(list(secuencia3))
print("")
print("")

#Números del 10 al 0
secuencia4= range(10,-1, -1)
print(list(secuencia4))
print("")
print("")

#Números múltiplos del 3 y 5 del 1 al 1000. al revés
secuencia51= range(990,14,-15)
print(list(secuencia51))
print("")
print("")

#Funciones operaciones secuencias
#Tamaño: len()
#Suma: sum()
#Elemento mínimo: min()
#Elemento máximo: max()
#Invertir orden: reversed()
secuencia= range(1,2000,5)
lista= [3,4,5,6,7,8,9,10,15,20]

print("El tamaño de la secuencia es: ",len(secuencia))
print("El tamaño de la lista es: ", len(lista))
print("El mínimo de la secuencia es: ",min(secuencia))
print("El mínimo de la lista es: ", min(lista))
print("El inverso de la secuencia es: ",list(reversed(secuencia)))
print("El inverso de la lista es: ", list(reversed(lista)))

#Repetir ejercicio anterior usando reversed
secuencia= range(1,11) #No es necesario poner el salto si es 1
print(list(reversed(secuencia)))
print("")

secuencia1= range(20,30)
print(list(reversed(secuencia1)))
print("")

#Números del -10 al 10 con salto 2
secuencia2= range(-10,11, 2)
print(list(reversed(secuencia2)))
print("")
print("")

#números multiplos del 3 desde -10 hasta 5
secuencia3= range(-9,6, 3)
print(list(reversed(secuencia3)))
print("")
print("")

#Números del 10 al 0
secuencia4= range(10,-1, -1)
print(list(reversed(secuencia4)))
print("")
print("")

#Números múltiplos del 3 y 5 del 1 al 1000. al revés
secuencia51= range(990,14,-15)
print(list(reversed(secuencia51)))
print("")
print("")