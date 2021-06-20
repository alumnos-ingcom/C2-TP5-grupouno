################
# Sergio Checcarelli - @checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class CustomError(Exception):
    pass

def prueba():
    try:
        indice = input("Ingrese el n-nesimo elemento de la serie Fibonacci: ")
        if int(indice) <= 2:
            raise CustomError("El nùmero debe ser mayor que 2")
        valor1 = 0
        valor2 = 1
        for number in range(int(indice)-2):
            valorAux = valor2
            valor2 = valor1 + valor2
            valor1 = valorAux
        print("El n-nesimo valor de la serie es: " + valor2)
    except ValueError as err:
        print("El valor no es un numero")
    pass

if __name__ == "__main__":
    prueba()


