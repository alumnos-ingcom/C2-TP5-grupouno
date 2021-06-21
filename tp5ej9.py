################
# MARTIN DARRICADES Sebastián - @sebasamd sebasamd@gmail.com
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# Sergio Checcarelli - @checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Reemplazar por las funciones del ejercicio

def factorial(numero):
    """Factorial"""
    producto = int(numero)
    for i in range(2, numero):
        producto *= i
        print(producto)
    return producto

def separar(numero):
    lista = []
    i = 0
    for i in str(numero):
        lista.append(i)
    return lista
    
def factorizar(lista):
    for i in lista:
        factorizar = factorial(i)
        print(factorizar)


def prueba():
    print("Probando las funciones(TP5EJ6)")

    print("Ingrese una cadena para verificar si se encuentra balanceada: \n")
    cadena = input("Ingrese su cadena: ")
    entero = int(cadena)
    separado = separar(entero)
    fact = factorizar(separado)
    print(factorizar)
    print(type(separado))
    print(separado)
    #verificar = factorial(entero)
    #print(verificar)
    
    
    
if __name__ == "__main__":
    prueba()

