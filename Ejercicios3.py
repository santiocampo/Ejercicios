#Ejercicio 3
# a) Programa que calcule los primeros 100 terminos de la serie de fibonacci
while True:
    try:
        n= int(input("Dame el último término de la serie de Fibonacci que deseas calcular: "))
    except ValueError:
        continue
    if n<=0:
        print("El número introducido es incorrecto\ningresa otro número")
    else:
        break

f1= 1
f2= 1
lf= [1,1]

for i in range(3,n+1):
    f3=f1+f2
    lf.append(f3)
    f1= f2
    f2= f3

print(lf)
print("\n\n")

# b) Programa que determine todos los divisores de un numero n
while True:
    try:
        x= int(input("Dame el número que deseas analizar: "))
    except ValueError:
        continue
    if x<=0:
        print("El número introducido es incorrecto\ningresa otro número")
    else:
        break

cd= 0
div= []
for k in range (1,x+1):
    if (x%k) ==0: 
        div.append(k)
        cd= cd+1

print("El número ", x," tiene ",cd," divisores")
print("Los divisores del número ",x, " son: ")
print(div,"\n\n")

# c) Programa que determine si un número n es primo

while True:
    try:
        p= int(input("Dame un número: "))
    except ValueError:
        continue
    if p<=0:
        print("El número introducido es incorrecto\ningresa otro número")
    else:
        break

cdiv= 0

for d in range(1,p+1):
    if (p%d) ==0: 
        cdiv= cdiv+1

if p== 1:
    print("El número ",p," no puede ser clasificado como primo o no primo")
else:
    if cdiv == 2:
        print("El número ", p," es primo\n\n")
    else: 
        print("El número ", p," no es primo\n\n")

# d) Programa que sume los digitos de un numero cualquiera. Ejemplo: numero=> 8791, rta=> 25 

while True:
    try:
        a= int(input("Ingresa un número: "))
    except ValueError:
        continue
    if a<0:
        print("El número ingresado es incorrecto\n\ningresa otro número")
    else:
        break

a= str(a)
a= list(a)
a= [int(n) for n in a]
s= sum(a)
a= [str(n) for n in a]
a= "".join(a)
a= int(a)
print("La suma de los dígitos del número ",a," es: ",s,"\n\n")

# e) Programa que sume los digitos pares de un numero cualquiera

while True:
    try:
        o= int(input("Ingresa un número: "))
    except ValueError:
        continue
    if a<0:
        print("El número ingresado es incorrecto\n\ningresa otro número")
    else:
        break

o1= str(o)
o1= list(o1)
o1= [int(n) for n in o1]

def numpar(o1k):
    if o1k % 2 == 0:
        return True

    return False

pariter= filter(numpar,o1)
pares= list(pariter)
spar= sum(pares)

if spar>0:
    print("La suma de los dígitos pares del número ",o," es: ",spar,"\n\n")
else:
    print("El número ingresado no tiene dígitos pares\n\n")

#Ejercicio 4
print("Ejercicio 4: ")

Rendimiento= ["B", "B", "B", "C", "B", "A", "C", "B", "A", "C", "B", "B", "B", "B", "A", "B", "A", "A", "C", "B","B", "B", "B", "C", "A", "C"]

def empdes(emp):
    if emp == "C":
        return True
    return False

despiter= filter(empdes, Rendimiento)
desp= list(despiter)
numdesp= len(desp)

def empaum(empa):
    if empa == "A":
        return True
    return False

aumiter= filter(empaum,Rendimiento)
aum= list(aumiter)
numaum= len(aum)

print(numaum,"empleados pueden pedir un aumento de salario")
print(numdesp,"empleados podrán ser despedidos\n\n")

#Ejercicio 5
print("Ejercicio 5: ")
Rendimientodepor= ["A","B","C","B","B","B","C","B","A","C","B","A","C","B","B","B","B","A","B","A","A","C","B","B","B","B","C"]
Edades= [42, 60, 18, 20, 35, 25, 60, 30, 19, 42, 21, 17, 39, 30, 28, 34, 27, 23, 23, 20, 25, 40, 31, 32, 45, 26, 17]

def atlalto(atl):
    if atl== "A":
        return True
    return False

altoiter= filter(atlalto, Rendimientodepor)
altoatl= list(altoiter)
numalto= len(altoatl)

def atlacep(alt):
    if alt =="B":
        return True
    return False

acepiter= filter(atlacep, Rendimientodepor)
acepalt= list(acepiter)
numacep= len(acepalt)

def atlinsu (atlet):
    if atlet== "C":
        return True
    return False

insuiter= filter(atlinsu, Rendimientodepor)
insuatl= list(insuiter)
numinsu= len(insuatl)

numalto40= 0 
numbajo25= 0
depor3040acep= 0
alto30= 0
insu35= 0
for k in range (0,len(Edades)):
    if (Rendimientodepor[k]== "A") and (Edades[k]> 40):
        numalto40= numalto40 +1
    if (Rendimientodepor[k]== "C") and (Edades[k]< 25):
        numbajo25= numbajo25+1
    if (Rendimientodepor[k]== "B") and (30<Edades[k]<40):
        depor3040acep= depor3040acep+1
    if (Rendimientodepor[k]== "A") and (Edades[k]< 30):
        alto30= alto30 + 1
    if (Rendimientodepor[k]== "C") and (Edades[k]> 35):
        insu35= insu35+1

print("El número de deportistas con un rendimiento alto es: ",numalto)
print("El número de deportistas con un rendimiento aceptable es: ", numacep)
print("El número de deportistas con un rendimiento insuficiente es: ",numinsu)
print("El número de deportistas mayores de 40 con un rendimiento alto es: ",numalto40)
print("El número de deportistas menores de 25 con un rendimiento bajo es: ",numbajo25)
print("El número de deportistas entre 30 y 40 con rendimiento aceptable es: ",depor3040acep)
print("El número de deportistas menores de 30 con rendimiento alto es: ", alto30)
print("El número de deportistas mayores de 35 con rendimiento insuficiente es: ", insu35)
print("\n\n")

#Ejercicio 6

niño2dlv= 5000
niño3dlv= 8000
niño2dsd= 7000
niño3dsd= 9000
adulto2dlv= 8000
adulto3dlv= 12000
adulto2dsd= 9000
adulto3dsd= 15000
c2dns= 0
c3dns= 0
c2dnf= 0
c3dnf= 0
c2das= 0
c3das= 0
c2daf= 0
c3daf= 0

v1= ["3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"]
v2= ["2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"]
v3= ["2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"]
v4= ["2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"]
v5= ["3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"]
v6= ["2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"]
v7= ["2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"]
v8= ["2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"]
v9= ["3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"]
v10= ["3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"]
v11= ["2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"]
v12= ["2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"]
v13= ["3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"]
v14= ["3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIEROLES"]
v15= ["3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"]
v16= ["2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"]
v17= ["2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"]
v18= ["2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"]
v19= ["3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"]
v20= ["3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"]
v21= ["3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"]
v22= ["3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"]
v23= ["2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"]
v24= ["2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"]
v25= ["2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"]
v26= ["3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"]
v27= ["3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"]
v28= ["2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"]
v29= ["2D_1NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"]
v30= ["2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"]
v31= ["3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"]
v32= ["2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"]
v33= ["2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"]
v34= ["3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"]
v35= ["3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"]
v36= ["2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"]
v37= ["2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"]
v38= ["2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"]
v39= ["2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"]
v40= ["2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"]
v41= ["3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"]
v42= ["3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"]
v43= ["2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"]
v44= ["2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"]
v45= ["3D_1NIÑOS_SABADO", "3D_1ADULTOS_SABADO"]
v46= ["2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"]
v47= ["3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"]
v48= ["3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"]
v49= ["3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"]
v50= ["3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"]
v51= ["2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"]
v52= ["2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"]
v53= ["3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"]

V= [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40, v41, v42, v43, v44, v45, v46, v47, v48, v49, v50, v51, v52, v53]

for m in range(len(V)):
    if (V[m][0] == "2D_1NIÑOS_MARTES") or (V[m][0] == "2D_1NIÑOS_MIERCOLES") or (V[m][0] == "2D_1NIÑOS_JUEVES") or (V[m][0] == "2D_1NIÑOS_VIERNES"):
        c2dns= c2dns +1
    if (V[m][0] == "3D_1NIÑOS_MARTES") or (V[m][0] == "3D_1NIÑOS_MIERCOLES") or (V[m][0] == "3D_1NIÑOS_JUEVES") or (V[m][0] == "3D_1NIÑOS_VIERNES"):
        c3dns= c3dns +1
    if (V[m][0] == "2D_1NIÑOS_SABADO") or (V[m][0] == "2D_1NIÑOS_DOMINGO"):
        c2dnf= c2dnf +1
    if (V[m][0] == "3D_1NIÑOS_SABADO") or (V[m][0] == "3D_1NIÑOS_DOMINGO"):
        c3dnf= c3dnf +1
    if (V[m][0] == "2D_2NIÑOS_MARTES") or (V[m][0] == "2D_2NIÑOS_MIERCOLES") or (V[m][0] == "2D_2NIÑOS_JUEVES") or (V[m][0] == "2D_2NIÑOS_VIERNES"):
        c2dns= c2dns +2
    if (V[m][0] == "3D_2NIÑOS_MARTES") or (V[m][0] == "3D_2NIÑOS_MIERCOLES") or (V[m][0] == "3D_2NIÑOS_JUEVES") or (V[m][0] == "3D_2NIÑOS_VIERNES"):
        c3dns= c3dns +2
    if (V[m][0] == "2D_2NIÑOS_SABADO") or (V[m][0] == "2D_2NIÑOS_DOMINGO"):
        c2dnf= c2dnf +2
    if (V[m][0] == "3D_2NIÑOS_SABADO") or (V[m][0] == "3D_2NIÑOS_DOMINGO"):
        c3dnf= c3dnf +2
    if (V[m][0] == "2D_3NIÑOS_MARTES") or (V[m][0] == "2D_3NIÑOS_MIERCOLES") or (V[m][0] == "2D_3NIÑOS_JUEVES") or (V[m][0] == "2D_3NIÑOS_VIERNES"):
        c2dns= c2dns +3
    if (V[m][0] == "3D_3NIÑOS_MARTES") or (V[m][0] == "3D_3NIÑOS_MIERCOLES") or (V[m][0] == "3D_3NIÑOS_JUEVES") or (V[m][0] == "3D_3NIÑOS_VIERNES"):
        c3dns= c3dns +3
    if (V[m][0] == "2D_3NIÑOS_SABADO") or (V[m][0] == "2D_3NIÑOS_DOMINGO"):
        c2dnf= c2dnf +3
    if (V[m][0] == "3D_3NIÑOS_SABADO") or (V[m][0] == "3D_3NIÑOS_DOMINGO"):
        c3dnf= c3dnf +3
    if (V[m][1] == "2D_1ADULTOS_MARTES") or (V[m][1] == "2D_1ADULTOS_MIERCOLES") or (V[m][1] == "2D_1ADULTOS_JUEVES") or (V[m][1] == "2D_1ADULTOS_VIERNES"):
        c2das= c2das +1
    if (V[m][1] == "3D_1ADULTOS_MARTES") or (V[m][1] == "3D_1ADULTOS_MIERCOLES") or (V[m][1] == "3D_1ADULTOS_JUEVES") or (V[m][1] == "3D_1ADULTOS_VIERNES"):
        c3das= c3das +1
    if (V[m][1] == "2D_1ADULTOS_SABADO") or (V[m][1] == "2D_1ADULTOS_DOMINGO"):
        c2daf= c2daf +1
    if (V[m][1] == "3D_1ADULTOS_SABADO") or (V[m][1] == "3D_1ADULTOS_DOMINGO"):
        c3daf= c3daf +1
    if (V[m][1] == "2D_2ADULTOS_MARTES") or (V[m][1] == "2D_2ADULTOS_MIERCOLES") or (V[m][1] == "2D_2ADULTOS_JUEVES") or (V[m][1] == "2D_2ADULTOS_VIERNES"):
        c2das= c2das +2
    if (V[m][1] == "3D_2ADULTOS_MARTES") or (V[m][1] == "3D_2ADULTOS_MIERCOLES") or (V[m][1] == "3D_2ADULTOS_JUEVES") or (V[m][1] == "3D_2ADULTOS_VIERNES"):
        c3das= c3das +2
    if (V[m][1] == "2D_2ADULTOS_SABADO") or (V[m][1] == "2D_2ADULTOS_DOMINGO"):
        c2daf= c2daf +2
    if (V[m][1] == "3D_2ADULTOS_SABADO") or (V[m][1] == "3D_2ADULTOS_DOMINGO"):
        c3daf= c3daf +2
    if (V[m][1] == "2D_3ADULTOS_MARTES") or (V[m][1] == "2D_3ADULTOS_MIERCOLES") or (V[m][1] == "2D_3ADULTOS_JUEVES") or (V[m][1] == "2D_3ADULTOS_VIERNES"):
        c2das= c2das +3
    if (V[m][1] == "3D_3ADULTOS_MARTES") or (V[m][1] == "3D_3ADULTOS_MIERCOLES") or (V[m][1] == "3D_3ADULTOS_JUEVES") or (V[m][1] == "3D_3ADULTOS_VIERNES"):
        c3das= c3das +3
    if (V[m][1] == "2D_3ADULTOS_SABADO") or (V[m][1] == "2D_3ADULTOS_DOMINGO"):
        c2daf= c2daf +3
    if (V[m][1] == "3D_3ADULTOS_SABADO") or (V[m][1] == "3D_3ADULTOS_DOMINGO"):
        c3daf= c3daf +3
    if (V[m][1] == "2D_4ADULTOS_MARTES") or (V[m][1] == "2D_4ADULTOS_MIERCOLES") or (V[m][1] == "2D_4ADULTOS_JUEVES") or (V[m][1] == "2D_4ADULTOS_VIERNES"):
        c2das= c2das +4
    if (V[m][1] == "3D_4ADULTOS_MARTES") or (V[m][1] == "3D_4ADULTOS_MIERCOLES") or (V[m][1] == "3D_4ADULTOS_JUEVES") or (V[m][1] == "3D_4ADULTOS_VIERNES"):
        c3das= c3das +4
    if (V[m][1] == "2D_4ADULTOS_SABADO") or (V[m][1] == "2D_4ADULTOS_DOMINGO"):
        c2daf= c2daf +4
    if (V[m][1] == "3D_4ADULTOS_SABADO") or (V[m][1] == "3D_4ADULTOS_DOMINGO"):
        c3daf= c3daf +4
    if (V[m][1] == "2D_5ADULTOS_MARTES") or (V[m][1] == "2D_5ADULTOS_MIERCOLES") or (V[m][1] == "2D_5ADULTOS_JUEVES") or (V[m][1] == "2D_5ADULTOS_VIERNES"):
        c2das= c2das +5
    if (V[m][1] == "3D_5ADULTOS_MARTES") or (V[m][1] == "3D_5ADULTOS_MIERCOLES") or (V[m][1] == "3D_5ADULTOS_JUEVES") or (V[m][1] == "3D_5ADULTOS_VIERNES"):
        c3das= c3das +5
    if (V[m][1] == "2D_5ADULTOS_SABADO") or (V[m][1] == "2D_5ADULTOS_DOMINGO"):
        c2daf= c2daf +5
    if (V[m][1] == "3D_5ADULTOS_SABADO") or (V[m][1] == "3D_5ADULTOS_DOMINGO"):
        c3daf= c3daf +5

btns= c2dns+c3dns
dta3df= c3daf * adulto3dsd
bvt = c2dns + c2dnf + c3dns + c3dnf + c2das +c2daf + c3das + c3daf
dvt= (c2dns*niño2dlv) + (c2dnf*niño2dsd) + (c3dns*niño3dlv) + (c3dnf*niño3dsd) + (c2das*adulto2dlv) + (c2daf*adulto2dsd) + (c3das*adulto3dlv) + (c3daf*adulto3dsd)

print("El número total de boletas vendidas para niños entre semana es: ", btns)
print("Las ventas de las boletas 3D para adultos el fin de semana es: ", dta3df)
print("El número total de boletas vendidas fue: ", bvt)
print("LAs vntas totales fueron: ", dvt)