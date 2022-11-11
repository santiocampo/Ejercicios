class ProfesoresUnal:
    def __init__(self, nombre, sexo, edad, cualidad):
        self.nombre = nombre 
        self.sexo = sexo
        self.edad = edad
        self.cualidad = cualidad 
    
    def enseñar(self, experiencia, energia):
        if (experiencia == 100) and (energia == "Animado"):
            calidad = 100
        elif (50 <= experiencia < 100) and (energia == "Animado"):
            calidad = 80
        elif (50 <= experiencia < 100) and (energia == "Normal"):
            calidad = 50
        elif (25 <= experiencia < 50) and (energia == "Normal"):
            calidad = 25
        elif (0 < experiencia < 25) and (energia == "Mala"):
            calidad = 10
        elif (experiencia == 0) and (energia == "Terrible"):
            calidad = 0
        elif (experiencia == 100) and (energia == "Mala"):
            calidad = 15
        elif (50 <= experiencia < 100) and (energia == "Mala"):
            calidad = 20
        elif (50 <= experiencia < 100) and (energia == "Terrible"):
            calidad = 10
        return calidad

    def evaluar(self, estadodeAnimo):
        if (estadodeAnimo == "Excelente"):
            dificultadExamen = 0
        elif (estadodeAnimo == "Bien"):
            dificultadExamen = 20
        elif (estadodeAnimo == "Regular"):
            dificultadExamen = 40
        elif (estadodeAnimo == "Malo"):
            dificultadExamen = 75
        elif (estadodeAnimo == "Pesimo"):
            dificultadExamen = 100
        return dificultadExamen

profesor1 = ProfesoresUnal("Elisabeth Restrepo", "F", 30, "Agil") 
profesor2 = ProfesoresUnal("Luis Mulcue", "M", 25, "Reflexivo")
profesor3 = ProfesoresUnal("Cristian Pachon", "M", 41, "Observador")

if __name__ == "__main__":
    print(profesor3.nombre, profesor3.sexo, profesor3.edad, profesor3.cualidad)
    profesor3.edad = 20
    print(profesor1.enseñar(85, "Mala"))
    print(profesor2.evaluar("Bien"))