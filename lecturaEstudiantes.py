"""
Leer el archivo data.json y luego calcular la media de los valores
"""
import json

archivo = "data.json"
opcion = "r"

with open(archivo, opcion) as file:
    data = json.load(file)
    length = len(data)
    total = sum(data)
    prom = total/length
    print("El promedio de los datos es: {}".format(prom))

"""
Leer el archivo estudiantes.json, y luego calcular el promedio de cada uno de los estudiantes.
"""

archivo2 = "estudiantes.json"

with open(archivo2, opcion) as file:
    data2 = json.load(file)
    keys = list(data2.keys())
    len = len(data2)
    promedios = {}
    for i in range(len):
        notas = data2[keys[i]]
        lenNotas = 3
        prom = sum(notas)/lenNotas
        promedios[keys[i]] = prom
    print(promedios)