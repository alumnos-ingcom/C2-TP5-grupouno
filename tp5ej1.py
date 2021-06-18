################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# *Agregar datos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Reemplazar por las funciones del ejercicio

#Escribir una función que retorne True cuando un número entero es par y False cuando no lo sea, sin utilizar módulo. (%)

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

def es_par2(numero):
    """
    Se me ocurrio otro metodo y quise probarlo. Utiliza el número ingresado como exponente de -2.
    
    """
    elevado = (-2)**(numero)
    if elevado > 0:
        return True
    else:
        return False
        

def prueba():
    numero1 = es_par(-20)
    print(numero1)
    numero2 = es_par(7)
    print(numero2)
    ##Lineas para es_par2
    numero3 = es_par2(-4)
    print(numero3)
    numero4 = es_par2(51)
    print(numero4)
    
    

if __name__ == "__main__":
    prueba()

