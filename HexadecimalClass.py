class Hexadecimal:
    def __init__(self, valorNumerico):
        self.valorNumerico = valorNumerico
    
    def conversionBinario(self):
        numero = str(self.valorNumerico)
        numero = int(numero, 16)
        conversion = bin(numero)
        conversion = conversion[2::]
        return conversion

    def conversionOctal(self):
        numero = str(self.valorNumerico)
        numero = int(numero, 16)
        conversion = oct(numero)
        conversion = conversion[2::]
        return conversion

    def conversionDecimal(self):
        numero = str(self.valorNumerico)
        conversion = int(numero, 16)
        return conversion

if __name__ == "__main__":
    decimal1 = Hexadecimal(8)
    decimal2 = Hexadecimal("a")
    print(decimal1.conversionBinario())
    print(decimal2.conversionDecimal())