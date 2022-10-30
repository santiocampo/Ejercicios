"""
Este módulo contiene 3 funciones para convertir la base de un número octal positivo a binario,
decimal y hexadecimal.

Las funciones son:

* octal_binario(numero) ==> Regresa el numero en base 2 (binario)
* octal_decimal(numero) ==> Regresa el numero en base 10 (decimal)
* octal_hexadecimal(numero) ==> Regresa el numero en base 16 (hexadecimal)
"""
def octal_binario(numero):
    numero = int(numero,8)
    octalBin = bin(numero)
    return octalBin

def octal_decimal(numero):
    octalDec = int(numero,8)
    return octalDec

def octal_hexadecimal(numero):
    numero = int(numero,8)
    octalHex = hex(numero)
    return octalHex 