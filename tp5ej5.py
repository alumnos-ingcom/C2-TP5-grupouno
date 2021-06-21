################
# Sergio Checcarelli - @checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class CustomError(Exception):
    pass

def prueba():
    textoIn = input("Ingrese el texto a modificar: ")
    print(textoIn.swapcase())
    pass
if __name__ == "__main__":
    prueba()
