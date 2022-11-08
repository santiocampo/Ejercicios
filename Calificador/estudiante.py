"""
Este módulo contiene 2 funciones para el almacenamiento de la información de los estudiantes.
"""
def mensajeControl():
    mensaje = """
            Bienvenido a la herramienta de calificación, por favor ingrese los datos requeridos a continuación:
            - Cantidad de alumnos
            - Nombres de alumnos
            - Cantidad de materias
            - Nombres de materias
            - Porcentajes notas (Todas las materias deben tener 4 porcentajes), recuerden ingresar los porcentajes en un rango de 0 a 1
            - Notas por materia
    """
    print(mensaje)
    input("Ingrese enter para ejecutar la herramienta...")

def nombresEstudiantes(cantidadEstudiantes):
    estudiantes = []
    for i in range(cantidadEstudiantes):
        nombresEstudiante = input("Ingrese el nombre del {} estudiante: ".format(i+1))
        estudiantes.append(nombresEstudiante)
    print("\n")
    return estudiantes