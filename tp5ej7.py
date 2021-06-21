################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# CHECCARELLI Sergio - @checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Escriba una funcion que determine la distancia entre dos números sin usar valor absoluto.

def distancia_entre_dos_numeros(numero1, numero2):
    """
    Devuelve la distancia entre dos números ingresados
    
    """
    
    if numero1 < 0 and numero2 > 0: # Si uno es positivo y el otro negativo, se calcula la distancia al 0 de cada uno y se suman
        distancia = (0 - numero1) + (0 + numero2)    
    elif numero1 > 0 and numero2 < 0:
        distancia = (0 + numero1) + (0 - numero2)
        
    if numero1 > 0 and numero2 > 0 or numero1 < 0 and numero2 < 0:
        distancia = numero1 - numero2 # Si los dos números son positivos o los dos son negativos, se restan los números
      
        
    if numero1 == 0: # Si alguno de los números es 0, la distancia es el otro número
        distancia = numero2
    elif numero2 == 0:
        distancia = numero1
    
    if distancia < 0: # Si la distancia es negativa, la pasa a positiva
        distancia *= -1 
         
    return distancia 


def prueba():
    distancia = distancia_entre_dos_numeros(-8, -5)
    print(distancia)
    
    distancia = distancia_entre_dos_numeros(8, 5)
    print(distancia)
    
    distancia = distancia_entre_dos_numeros(-8.5, 5)
    print(distancia)
    
    distancia = distancia_entre_dos_numeros(8.5, -5)
    print(distancia)
    
    distancia = distancia_entre_dos_numeros(0, 5)
    print(distancia)
    
    distancia = distancia_entre_dos_numeros(-5, 0)
    print(distancia)
    
    distancia = distancia_entre_dos_numeros(0, 0)
    print(distancia)

    
if __name__ == "__main__":
    prueba()