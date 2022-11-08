"""
Este módulo contiene 3 funciones para el almacenamiento de la información acádemica de los estudiantes.
"""
def notasEstudiante(cantidadEstudiantes,listaNombresEstudiantes,cantidadMaterias,nombreMaterias):
    calificacionesEstudiantes = {}
    for l in range(cantidadEstudiantes):
        calificacionesEstudiantes[listaNombresEstudiantes[l]] = {}
        for m in range(cantidadMaterias):
            calificacionesEstudiantes[listaNombresEstudiantes[l]][nombreMaterias[m]] = [float(input("Ingrese la primera nota: ")), float(input("Ingrese la segunda nota: ")),float(input("Ingrese la tercera nota: ")), float(input("Ingrese la cuarta nota: "))]
            print("\n")
    return calificacionesEstudiantes

def nombresMaterias(cantidadMaterias):
    materias = []
    for h in range(cantidadMaterias):
        nombreMateria = input("Ingrese el nombre de la {} materia: ".format(h+1))
        materias.append(nombreMateria)
    print("\n")
    return materias

def porcentajes(nombreMaterias,cantidadMaterias):
    porcentajesMateria = {}
    for m in range(cantidadMaterias):
        porcentajesMateria[nombreMaterias[m]] = [float(input("Ingrese el primer porcentaje de la materia: ")), float(input("Ingrese el segundo porcentaje de la materia: ")), float(input("Ingrese el tercer porcentaje de la materia: ")), float(input("Ingrese el cuarto porcentaje de la materia: ")) ]
        print("\n")
    return porcentajesMateria