################
# MARTIN DARRICADES Sebastián - @sebasamd sebasamd@gmail.com
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# Sergio Checcarelli - @checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Reemplazar por las funciones del ejercicio

def factorial(numero):
    """Factorial"""
    producto = numero
    for i in range(2, numero):
        producto *= i
        print(producto)
    return producto

def prueba():
    print("Probando las funciones(TP5EJ6)")

    print("Ingrese una cadena para verificar si se encuentra balanceada: \n")
    cadena = input("Ingrese su cadena: ")
    entero = int(cadena)
    verificar = factorial(entero)
    print(verificar)
    
if __name__ == "__main__":
    prueba()

