################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# CHECCARELLI Sergio -@checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Escribir una función que determine si un numero entero positivo es capicúa.

def es_capicua(numero):
    """
    Determina si un número ingresado como argumento es capicúa. Funciona para números negativos!
    
    """
    absoluto = abs(int(numero)) 
    string_num = str(absoluto)
    inverso_num = string_num[::-1]
    
    if string_num == inverso_num:
        return True
    else:
        return False
  
def prueba():
    print("Ingrese un número")
    numero = input()
    print(f"¿Es {numero} capicúa?")
    print(es_capicua(numero))
    
if __name__ == "__main__":
        prueba()


 

