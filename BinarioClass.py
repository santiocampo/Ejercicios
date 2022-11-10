class Binario:
    def __init__(self, valorNumerico) :
        self.valorNumerico = valorNumerico

    def conversionOctal(self):
        numero = str(self.valorNumerico)
        numero = int(numero,2)
        conversion = oct(numero)
        conversion = conversion[2::]
        return conversion

    def conversionDecimal(self):
        numero = str(self.valorNumerico)
        conversion = int(numero,2)
        return conversion

    def conversionHexadecimal(self):
        numero = str(self.valorNumerico)
        numero = int(numero,2)
        conversion = hex(numero)
        conversion = conversion[2::]
        return conversion

if __name__ == "__main__":
    decimal1 = Binario(1000)
    decimal2 = Binario(1010)
    print(decimal1.conversionDecimal())
    print(decimal2.conversionHexadecimal())