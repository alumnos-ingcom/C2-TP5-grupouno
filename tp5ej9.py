################
# MARTIN DARRICADES Sebastián - @sebasamd sebasamd@gmail.com
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# Sergio Checcarelli - @checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Reemplazar por las funciones del ejercicio

def factorial(num):
    """Factorial"""
    product = num
    for i in range(2, num):
        product *= i
    return product

def prueba():
    print("Probando las funciones(TP5EJ6)")

    print("Ingrese una cadena para verificar si se encuentra balanceada: \n")
    cadena = input("Ingrese su cadena: ")
    filtrada = filtrar_cadena(cadena)
    verificar = balance_cadena(filtrada)
    print(verificar)
    
if __name__ == "__main__":
    prueba()

