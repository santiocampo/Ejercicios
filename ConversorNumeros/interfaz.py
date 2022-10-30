"""
Este módulo contiene la parte gráfica del conversor de base y la decision de la conversión del número
"""
import binario
import octal
import dec
import hexadecimal

def textoConversor():
    texto = """
            Bienvenido al conversor de base, por favor ingrese la base del número, 
            el número y la base a la cual desea transformar el número.

            Recuerde que este conversor solo recibe como número de entrada números positivos. 
    """
    return texto


def decision(baseEntrada, baseSalida, numero):
    if (baseEntrada == 2) and (baseSalida == 8):
        resultado = binario.binario_octal(numero)
    if (baseEntrada == 2) and (baseSalida == 10):
        resultado = binario.binario_decimal(numero)
    if (baseEntrada == 2) and (baseSalida == 16):
        resultado = binario.binario_hexadecimal(numero)
    if (baseEntrada == 8) and (baseSalida == 2):
        resultado = octal.octal_binario(numero)
    if (baseEntrada == 8) and (baseSalida == 10):
        resultado = octal.octal_decimal(numero)
    if (baseEntrada == 8) and (baseSalida == 16):
        resultado = octal.octal_hexadecimal(numero)
    if (baseEntrada == 10) and (baseSalida == 2):
        resultado = dec.decimal_binario(numero)
    if (baseEntrada == 10) and (baseSalida == 8):
        resultado = dec.decimal_octal(numero)
    if (baseEntrada == 10) and (baseSalida == 16):
        resultado = dec.decimal_hexadecimal(numero)
    if (baseEntrada == 16) and (baseSalida == 2):
        resultado = hexadecimal.hexadecimal_binario(numero)
    if (baseEntrada == 16) and (baseSalida == 8):
        resultado = hexadecimal.hexadecimal_octal(numero)
    if (baseEntrada == 16) and (baseSalida == 10):
        resultado = hexadecimal.hexadecimal_decimal(numero)
    return resultado

    