"""
Este módulo contiene 3 funciones para convertir la base de un número octal positivo a binario,
decimal y hexadecimal.

Las funciones son:

* hexadecimal_binario(numero) ==> Regresa el numero en base 2 (binario)
* hexadecimal_octal(numero) ==> Regresa el numero en base 8 (octal)
* hexadecimal_decimal(numero) ==> Regresa el numero en base 10 (decimal)
"""
def hexadecimal_binario(numero):
    numero = int(numero,16)
    hexaBin = bin(numero)
    return hexaBin

def hexadecimal_octal(numero):
    numero = int(numero,16)
    hexaOct = oct(numero)
    return hexaOct

def hexadecimal_decimal(numero):
    hexaDec = int(numero,16)
    return hexaDec