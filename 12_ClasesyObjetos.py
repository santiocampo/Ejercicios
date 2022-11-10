#08/11/2022

"""
Crear una clase llamada ComidaColombiana.
Atributos: componente1, componente2, componente3
Métodos: Nutrir y Provocar
"""

class ComidaColombiana: 
    #Para crear los atributos
    def __init__(self, ingrediente1, ingrediente2, ingrediente3):
        self.ingrediente1 = ingrediente1
        self.ingrediente2 = ingrediente2
        self.ingrediente3 = ingrediente3
    #Para crear los métodos (Funciones)
    def provocar(self, opcion):
        if opcion in ["Huele bien", "Se ve bien", "Tengo hambre"]:
            return "Este alimento provoca"
        else:
            return "Este alimento no provoca"
    
    def nutrir(self, opcion ):
        if opcion in ["Estoy enfermo", "Tengo nauseas", "El doctor me prohibió"]:
            return "Este alimento no me puede nutrir"
        else:
            return "Este alimento me nutre" 

#Como crear un objeto

bandejaPaisa = ComidaColombiana("chorizo", "arepa", "chicharron") 
SancochoGallina = ComidaColombiana("Gallina", "Papa", "Caldo")
ajiacoSantafereno = ComidaColombiana("Papa", "Pollo", "Aguacate")

#Como acceder a los atributos de un objeto

atributo1BandejaPaisa = bandejaPaisa.ingrediente1
atributo2SancochoGallina = SancochoGallina.ingrediente2
atributo1Ajiaco = ajiacoSantafereno.ingrediente1

#print(atributo1BandejaPaisa)
#print(atributo2SancochoGallina)
#print(atributo1Ajiaco)

#Como acceder a los métodos de un objeto

#print(bandejaPaisa.provocar("Tengo hambre"))

#Ejercicio

"""
1)  Crear una clase llamada Profesores
    Atributos: Nombre, edad, salario
    Métodos: Enseñar, Calificar

2)  Crear una clase llamada Decimal
    Atributos: valorNumerico
    Métodos: convertirBinario, convertirOctal, convertirHexadecimal

"""