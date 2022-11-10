class Octal:
    def __init__(self, valorNumerico):
        self.valorNumerico = valorNumerico
    
    def conversionBinario(self):
        numero = str(self.valorNumerico)
        numero = int(numero, 8)
        conversion = bin(numero)
        conversion = conversion[2::]
        return conversion

    def conversionDecimal(self):
        numero = str(self.valorNumerico)
        conversion = int(numero, 8)
        return conversion

    def conversionHexadecimal(self):
        numero = str(self.valorNumerico)
        numero = int(numero, 8)
        conversion = hex(numero)
        conversion = conversion[2::]
        return conversion

if __name__ == "__main__":
    decimal1 = Octal(10)
    decimal2 = Octal(7)
    print(decimal1.conversionBinario())
    print(decimal2.conversionDecimal())
