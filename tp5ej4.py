################
# Sergio Checcarelli - @checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class CustomError(Exception):
    pass

def prueba():
    try:
        numeroPerfecto = input("Ingrese el nùmero para saber si es perfecto")
        divisores = []
        resultado = 0
        for numero in range(int(numeroPerfecto)-1):
            divisorAux = int(numeroPerfecto) % (numero + 1)
            if (divisorAux == 0):
                divisores.append(numero+1)
        for n in divisores:
            resultado = resultado + n
        if(resultado == int(numeroPerfecto)):
            print("El numero es perfecto")
        else:
            print("El nùmero no es perfecto")

    except ValueError as err:
        print("El valor no es un numero")
    pass

if __name__ == "__main__":
    prueba()


