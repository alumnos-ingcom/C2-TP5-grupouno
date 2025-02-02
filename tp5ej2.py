################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# *Agregar datos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Reemplazar por las funciones del ejercicio

#Fibonacci

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def ingreso_entero_mayor(mensaje, valor_minimo=0):
    """Esta funcion muestra un mensaje y agrega la solicitud de un número entero positivo mayor que 2"""
    ingreso = input(f"{mensaje}: #")
    try:
        entero = int(ingreso)
        if entero > 2:
            return entero 
        if entero <= 2 :
            raise IngresoIncorrecto(f"El número {ingreso}, no es mayor que 2.")
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    
def fibonacci(numero):
    """Esta funcion devuelve el termino n-esimo de la sucusion de fibonacci"""
    lista_fibonacci = []
    sucesiona = 0
    sucesionb = 1
    for i in range(numero):
        sucesiona, sucesionb = sucesionb , sucesiona + sucesionb
        lista_fibonacci.append(sucesiona)
    return lista_fibonacci[-1]

def prueba():
    print("Probando las funciones(TP5EJ2)")

    print("Esta funcion, devuelve el termino que le indique de la sucesion de Fibonacci. \n")
    numero = ingreso_entero_mayor("Ingrese un número entero mayor a 2")
    termino = fibonacci(numero)
    print(f"\n {termino}")
    

if __name__ == "__main__":
    prueba()

