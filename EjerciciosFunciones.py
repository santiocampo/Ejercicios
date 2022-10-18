#Ejercicio 1

def MayoriadeEdad(Edad):
    if Edad>= 18:
        return True
    else:
        return False

while True:
    try:
        Edad= int(input("Ingresa tu Edad: "))
    except ValueError:
        continue
    if Edad< 0:
        print("La edad ingresada no es válida")
    else:
        break
Resultado= MayoriadeEdad(Edad)
if Resultado == True:
    print("Funcion1\n")
    print("Usted es mayor de edad\n")
else:
    print("Funcion1\n")
    print("Usted es menor de edad\n")


def infoSalario(nombre, salario):
    mensaje= "hola {}, su salario es {}".format(nombre, salario)
    return mensaje

print("Funcion2\n")
nombre= input("Ingresa tu nombre: ")
salario= input("Ingresa tu salario: ")
info= infoSalario(nombre, salario)
print(info,"\n")

def sumaDigitos(numero):
    digitos= list(numero)
    for i in range(len(digitos)):
        digitos[i]= int(digitos[i])
    suma= sum(digitos)
    return suma 

print("Funcion3\n")
numero= input("Ingresa un número: ")
resultadosuma= sumaDigitos(numero)
print(resultadosuma,"\n")

def vocales(mensaje):
    caracteres= list(mensaje)
    contadorvocales= 0
    for i in range(len(caracteres)):
        if (caracteres[i] == "A") or (caracteres[i] == "E") or (caracteres[i] == "I") or (caracteres[i] == "O") or (caracteres[i] == "U") or (caracteres[i] == "a") or (caracteres[i] == "e") or (caracteres[i] == "i") or (caracteres[i] == "o") or (caracteres[i] == "u"):
            contadorvocales= contadorvocales + 1
    if contadorvocales>= 1:
        resultado= True
    else:
        resultado= False
    return resultado

print("Funcion4\n")
mensaje= input("Ingresa un mensaje: ")
resultadoVocales= vocales(mensaje)
if (resultadoVocales== True):
    print("El mensaje contiene vocales\n")
else:
    print("El mensaje no contiene vocales\n")

def divisores(numero):
    div= numero
    divisores= []
    for i in range(numero):
        if (numero % div == 0):
            divisores.append(div)
        div= div-1
    return divisores 

while True:
    try:
        numero= int(input("Ingresa un número: "))
    except ValueError:
        continue
    if numero <=0:
        print("El número ingresado no es válido")
    else: 
        break

print("Funcion5\n")
resultado= divisores(numero)
print("Los divisores de {} son: {}\n".format(numero, resultado))

def primalidad(numero):
    div= numero
    divisores= []
    for i in range(numero):
        if (numero % div == 0):
            divisores.append(div)
        div= div-1
    if (len(divisores)!=2):
        resultado= False
    else:
        resultado= True
    return resultado

print("Funcion6\n")
while True:
    try:
        numero= int(input("Ingresa un número: "))
    except ValueError:
        continue
    if numero <=0:
        print("El número ingresado no es válido")
    else: 
        break    

primo= primalidad(numero)
if (primo == True):
    print("El número {} es primo\n".format(numero))
else:
    print("El número {} no es primo\n".format(numero))


#Ejercicio2

def validezContraseña(contraseña):
    caracteres= list(contraseña)
    largo= len(caracteres)
    contadorMayus= 0
    contadorMinus= 0
    contadorNum= 0
    contadorEspeciales= 0
    contadorCaracteres= 0
    for j in range(largo):
        if (caracteres[j] == "A") or (caracteres[j] == "B") or (caracteres[j] == "C") or (caracteres[j] == "D") or (caracteres[j] == "E") or (caracteres[j] == "F") or (caracteres[j] == "G") or (caracteres[j] == "H") or (caracteres[j] == "I") or (caracteres[j] == "J") or (caracteres[j] == "K") or (caracteres[j] == "L") or(caracteres[j] == "M") or (caracteres[j] == "N") or (caracteres[j] == "O") or (caracteres[j] == "P") or (caracteres[j] == "Q") or (caracteres[j] == "R") or (caracteres[j] == "S") or (caracteres[j] == "T") or (caracteres[j] == "U") or (caracteres[j] == "V") or (caracteres[j] == "W") or (caracteres[j] == "X") or (caracteres[j] == "Y") or (caracteres[j] == "Z"):
            contadorMayus= contadorMayus + 1
        if (caracteres[j] == "a") or (caracteres[j] == "b") or (caracteres[j] == "c") or (caracteres[j] == "d") or (caracteres[j] == "e") or (caracteres[j] == "f") or (caracteres[j] == "g") or (caracteres[j] == "h") or (caracteres[j] == "i") or (caracteres[j] == "j") or (caracteres[j] == "k") or (caracteres[j] == "l") or(caracteres[j] == "m") or (caracteres[j] == "n") or (caracteres[j] == "o") or (caracteres[j] == "p") or (caracteres[j] == "q") or (caracteres[j] == "r") or (caracteres[j] == "s") or (caracteres[j] == "t") or (caracteres[j] == "u") or (caracteres[j] == "v") or (caracteres[j] == "w") or (caracteres[j] == "x") or (caracteres[j] == "y") or (caracteres[j] == "z"):
            contadorMinus= contadorMinus + 1
        if (caracteres[j] == "0") or (caracteres[j] == "1") or (caracteres[j] == "2") or (caracteres[j] == "3") or (caracteres[j] == "4") or (caracteres[j] == "5") or (caracteres[j] == "6") or (caracteres[j] == "7") or (caracteres[j] == "8") or (caracteres[j] == "9"):
            contadorNum= contadorNum + 1        
        if (caracteres[j] == "|") or (caracteres[j] == "°") or (caracteres[j] == "¬") or (caracteres[j] == "!") or (caracteres[j] == "@") or (caracteres[j] == "#") or (caracteres[j] == "$") or (caracteres[j] == "%") or (caracteres[j] == "&") or (caracteres[j] == "/") or (caracteres[j] == "(") or (caracteres[j] == ")") or (caracteres[j] == "=") or (caracteres[j] == "?") or (caracteres[j] == "'") or (caracteres[j] == "¿") or (caracteres[j] == "¡") or (caracteres[j] == "¨") or (caracteres[j] == "+") or (caracteres[j] == "*") or (caracteres[j] == "~") or (caracteres[j] == "}") or (caracteres[j] == "]") or (caracteres[j] == "[") or (caracteres[j] == "{") or (caracteres[j] == "^") or (caracteres[j] == ",") or (caracteres[j] == ";") or (caracteres[j] == ":") or (caracteres[j] == ".") or (caracteres[j] == "-") or (caracteres[j] == "_") or (caracteres[j] == ">") or (caracteres[j] == "<"):
            contadorEspeciales= contadorEspeciales + 1
        if largo>= 8:
            contadorCaracteres= contadorCaracteres + 1
    
    if (contadorMayus >= 1) and (contadorMinus>= 1) and (contadorNum >= 1) and (contadorEspeciales >= 1) and (contadorCaracteres >= 1):
        mensaje= "La contraseña es válida"
    else:
        mensaje= "La contraseña es inválida"
    return mensaje

contraseña= input("Ingresa una contraseña: ")
resultado= validezContraseña(contraseña)
print(resultado,"\n")

#Ejercicio 3

def calculadoraIMC(altura, peso):
    IMC= peso/(altura**2)
    return IMC

while True:
    try:
        altura= float(input("Ingresa tu estatura en metros: "))
        peso= float(input("Ingresa tu peso corporal en kilogramos: "))
    except ValueError:
        continue
    if (altura<= 0):
        print("El valor de altura ingresado es incorrecto")
    elif (peso<= 0):
        print("El valor de peso corporal ingresado es incorrecto")
    else:
        break

resultado= calculadoraIMC(altura, peso)
if (resultado < 30):
    print("Su indice de masa corporal es {}\n".format(resultado))
else:
    print("Su indice de masa corporal es {}".format(resultado))
    print("Usted tiene sobrepeso\n")

#Ejercicio 4

def salarioVendedor(seguros):
    salario= 2000000
    valorseguro= 300000
    ventas= valorseguro * seguros
    if (50 <=seguros< 110):
        salario= salario + (ventas*0.1)
    elif (110 <=seguros< 200):
        salario= salario + (ventas*0.2)
    elif (200 <=seguros< 500):
        salario= salario + (ventas*0.25)
    elif (seguros >= 500):
        salario= salario + (ventas*0.3)
    return salario

while True:
    try:
        seguros= int(input("Ingresa el número de salarios vendidos: "))
    except ValueError:
        continue
    if (seguros < 0):
        print("La cantidad de seguros vendidos es incorrecta")
    else: 
        break

resultado= salarioVendedor(seguros)
print("El salario del vendedor es {}\n".format(resultado))