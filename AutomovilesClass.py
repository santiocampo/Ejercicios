class Automoviles:
    def __init__(self, color, personasSentadas, uso):
        self.color = color
        self.personasSentadas = personasSentadas
        self.uso = uso

    def acelerar(self, aceleracion, tiempo):
        velocidad = aceleracion * tiempo
        return velocidad

    def frenar(self, velocidad, desaceleracion):
        tiempo = (-velocidad) * desaceleracion
        return tiempo

ferrari_458 = Automoviles("Rojo", 2, "Deportivo")
mcLaren_720s = Automoviles("Negro", 4, "Deportivo")
autolegal = Automoviles("Blanco", 8, "Publico")

if __name__ == "__main__":
    print(mcLaren_720s.color, mcLaren_720s.personasSentadas, mcLaren_720s.uso)
    mcLaren_720s.personasSentadas = 2
    print(mcLaren_720s.color, mcLaren_720s.personasSentadas, mcLaren_720s.uso)
    print(ferrari_458.acelerar(10,5))
    print(autolegal.frenar(30,-4))