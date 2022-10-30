"""
Este módulo contiene 3 funciones para convertir la base de un número decimal positivo a binario,
octal y hexadecimal.

Las funciones son:

* decimal_binario(numero) ==> Regresa el numero en base 2 (binario)
* decimal_octal(numero) ==> Regresa el numero en base 8 (octal)
* decimal_hexadecimal(numero) ==> Regresa el numero en base 16 (hexadecimal)
"""
def decimal_binario(numero): 
    numeroBin = bin(numero)
    return numeroBin

def decimal_octal(numero):
    numeroOct = oct(numero)
    return numeroOct

def decimal_hexadecimal(numero):
    numeroHex = hex(numero)
    return numeroHex