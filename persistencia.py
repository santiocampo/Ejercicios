import json
data = list(range(1, 1000, 2))

nombreArchivo = "data.json"
ruta =  nombreArchivo
opcion = "w"
with open(ruta, opcion) as file:
    json.dump(data, file)