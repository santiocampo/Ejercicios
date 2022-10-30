"""
Este módulo contiene 3 funciones para convertir la base de un número binario positivo a octal,
decimal y hexadecimal.

Las funciones son:

* binario_octal(numero) ==> Regresa el numero en base 8 (octal)
* binario_decimal(numero) ==> Regresa el numero en base 10 (decimal)
* binario_hexadecimal(numero) ==> Regresa el numero en base 16 (hexadecimal)
"""

def binario_octal(numero):
    numero = int(numero,2)
    binarioOct = oct(numero)
    return binarioOct

def binario_decimal(numero):
    binarioDec = int(numero,2)
    return binarioDec

def binario_hexadecimal(numero):
    numero = int(numero,2)
    binarioHex = hex(numero)
    return binarioHex