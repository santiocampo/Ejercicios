import estudiante
import materia
import calculos

estudiante.mensajeControl()

while True:
    try:
        cantidadEstudiantes = int(input("Ingrese la cantidad de estudiantes: "))
    except ValueError:
        continue
    if (cantidadEstudiantes <= 0 ):
        print("La cantidad de estudiantes ingresada no es válida")
    else:
        print("\n")
        break

listaNombresEstudiantes = estudiante.nombresEstudiantes(cantidadEstudiantes)

while True:
    try:
        cantidadMaterias = int(input("Ingrese la cantidad de materias a calificar: "))
    except ValueError:
        continue
    if (cantidadMaterias <= 0):
        print("La cantidad de materias ingresada no es válida")
    else:
        print("\n")
        break

cantidadPorcentajes = 4
nombreMaterias = materia.nombresMaterias(cantidadMaterias)
dataPorcentajes = materia.porcentajes(nombreMaterias,cantidadMaterias)
notasEstudiantes = materia.notasEstudiante(cantidadEstudiantes,listaNombresEstudiantes,cantidadMaterias,nombreMaterias)
notasMateria = calculos.calificacionMateria(cantidadEstudiantes, listaNombresEstudiantes, notasEstudiantes, dataPorcentajes,nombreMaterias,cantidadMaterias)
notasMaterias = calculos.almacenajeNotasMateria(notasMateria, nombreMaterias, cantidadMaterias, cantidadEstudiantes)
promedioMaterias = calculos.calculoPromedioMaterias(notasMaterias, nombreMaterias, cantidadMaterias, cantidadEstudiantes)
calculos.impresionResultados(cantidadMaterias, nombreMaterias, notasEstudiantes, promedioMaterias, cantidadEstudiantes, listaNombresEstudiantes)