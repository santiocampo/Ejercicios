class Decimal: 
    def __init__(self, valorNumerico) :
        self.valorNumerico = valorNumerico
    
    def convertirBinario(self):
        conversion = bin(self.valorNumerico)
        conversion = conversion[2::]
        return conversion
    
    def convertirOctal(self):
        conversion = oct(self.valorNumerico)
        conversion = conversion[2::]
        return conversion
    
    def conversionHexadecimal(self):
        conversion = hex(self.valorNumerico)
        conversion = conversion[2::]
        return conversion

if __name__ == "__main__":
    decimal1 = Decimal(8)
    decimal2 = Decimal(15)
    print(decimal1.convertirOctal())
    print(decimal2.conversionHexadecimal())
