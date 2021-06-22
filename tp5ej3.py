################
# Sergio Checcarelli - @checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class ValorMenor(Exception):
    pass

def prueba():
    try:
        indice = input("Ingrese el n-nesimo elemento de la serie Fibonacci: ")
        if int(indice) <= 3:
            raise ValorMenor
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
    except ValorMenor:
        print("El valor tiene que ser mayor que 3")
    pass

if __name__ == "__main__":
    prueba()


