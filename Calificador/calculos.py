"""
Este módulo contiene 3 funciones para el cálculo de las notas individuales de los estudiantes por materia
y el cálculo de los promedios por materia.
"""
def calificacionMateria(cantidadEstudiantes, listaNombresEstudiantes, notasEstudiantes, dataPorcentajes,nombreMaterias,cantidadMaterias):
    calificacionMaterias = {}
    for l in range(cantidadEstudiantes):
        calificacionMaterias[listaNombresEstudiantes[l]] = {}
        for m in range(cantidadMaterias):
            calificacionMaterias[listaNombresEstudiantes[l]][nombreMaterias[m]] = ((notasEstudiantes[listaNombresEstudiantes[l]][nombreMaterias[m]][0]) * (dataPorcentajes[nombreMaterias[m]][0])) + ((notasEstudiantes[listaNombresEstudiantes[l]][nombreMaterias[m]][1]) * (dataPorcentajes[nombreMaterias[m]][1])) + ((notasEstudiantes[listaNombresEstudiantes[l]][nombreMaterias[m]][2]) * (dataPorcentajes[nombreMaterias[m]][2])) + ((notasEstudiantes[listaNombresEstudiantes[l]][nombreMaterias[m]][3]) * (dataPorcentajes[nombreMaterias[m]][3]))
    return calificacionMaterias

def almacenajeNotasMateria(notasMateria, nombreMaterias, cantidadMaterias, cantidadEstudiantes):
    notasIndividuales = {}
    listaNotasMateria = []
    contador = 0
    contadorMateria = 0
    keys = notasMateria.keys()
    for j in range(cantidadMaterias):
        for key in keys:
            NotasMaterias = notasMateria[key][nombreMaterias[j]]
            listaNotasMateria.append(NotasMaterias)
    
    for l in range(cantidadEstudiantes):
        listaNotas = []
        for j in range(cantidadMaterias):
            listaNotas.append(listaNotasMateria[j+contador])
            notasIndividuales[nombreMaterias[contadorMateria]] = listaNotas
        contador = contador + cantidadEstudiantes
        contadorMateria = contadorMateria + 1
    return notasIndividuales

def calculoPromedioMaterias(notasMaterias, nombreMaterias, cantidadMaterias, cantidadEstudiantes):
    notasPromediosMaterias = {}    
    for j in range(cantidadMaterias):
        listadoNotas = notasMaterias[nombreMaterias[j]]
        notasPromediosMaterias[nombreMaterias[j]] = (sum(listadoNotas))/cantidadEstudiantes
    return notasPromediosMaterias

def impresionResultados(cantidadMaterias, nombreMaterias, notasEstudiantes, promedioMaterias, cantidadEstudiantes, listaNombresEstudiantes):
    for i in range(cantidadEstudiantes):
        nombre = listaNombresEstudiantes[i]
        notas = notasEstudiantes[listaNombresEstudiantes[i]]
        print("Las notas del estudiante {} son: {}".format(nombre, notas))
    print("\n")
    for j in range(cantidadMaterias):
        key = nombreMaterias[j]
        promedio = promedioMaterias[key]
        print("El promedio de la materia {} es: {}".format(key, promedio))