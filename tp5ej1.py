################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# *Agregar datos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

<<<<<<< HEAD
def es_par(numero):
    """
    Retorna True si el número ingresado es par. Retorna False si el número ingresado es impar
    
    """
    num = abs(numero) # La función abs() permite que se evaluen números negativos ya que toma el número sin signo
    
    while num > 1:
        num -= 2
    
    if num == 0:
        return True
    else:
        return False
=======

# Reemplazar por las funciones del ejercicio
"""Escribir una función que retorne True cuando un número entero es par y False cuando no lo sea, sin utilizar módulo. (%)"""
>>>>>>> b847af57ab13def8aa146ccc75423fdd6dbc9835

def prueba():
    numero1 = es_par(-10)
    print(numero1)
    numero2 = es_par(7)
    print(numero2)
    
    

if __name__ == "__main__":
    prueba()

