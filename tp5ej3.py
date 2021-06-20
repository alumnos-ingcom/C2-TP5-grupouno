################
# Sergio Checcarelli - @checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class CustomError(Exception):
    pass

def prueba():
    try:
        indice = input("Ingrese el n-nesimo elemento de la serie Fibonacci: ")
        if int(indice) <= 3:
            raise CustomError("El nùmero debe ser un entero mayor que 3")
        valor1 = 1
        valor2 = 1
        valor3 = 1
        for number in range(int(indice)-3):
            valorAux = valor2
            valorAux2 = valor3
            valor3 = valor1 + valor2 + valor3
            valor1 = valorAux
            valor2 = valorAux2
        print("El n-nesimo valor de la serie es: " + str(valor3))
    except ValueError as err:
        print("El valor no es un numero")
    pass

if __name__ == "__main__":
    prueba()


