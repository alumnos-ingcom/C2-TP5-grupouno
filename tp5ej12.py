################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# CHECCARELLI Sergio -@checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Escribir una función que determine retornando True si un par de listas
# contienen los mismos elementos que pueden estar ubicados en diferentes posiciones.

def son_listas_iguales(lista1, lista2):
    """
    Devuelve True si las dos listas ingresadas como argumentos son iguales
    
    """
    listas_iguales = False
    
    if len(lista1) != len(lista2):
        listas_iguales = False
        return listas_iguales
    else:
        for elemento in lista1:
            if elemento in lista2:
                listas_iguales = True
                lista2.remove(elemento)  # ¿Cómo hago para que no me modifique la lista que le paso como argumento?     
            else:
                listas_iguales = False
                break
        return listas_iguales      

def prueba():
    listaA = ["gato", 1, 2, 3, 5, 2, "piedra"]
    listaB = [2, "piedra", 1, 5, "gato", 3, 2]
    listaC = [2, 5, 5]
    listaD = [5, 2, 5]
    listaE = [5, 5, 4]
    listaF = [5, 4, 4]
    
    print(f"¿Son las listas \n{listaA} \ny \n{listaB} iguales?")
    print("-", son_listas_iguales(listaA, listaB))
    print(f"\n¿Son las listas \n{listaC} \ny \n{listaA} iguales?")
    print("-", son_listas_iguales(listaC, listaA))
    print(f"\n¿Son las listas \n{listaC} \ny \n{listaD} iguales?")
    print("-", son_listas_iguales(listaC, listaD))
    print(f"\n¿Son las listas \n{listaE} \ny \n{listaF} iguales?")
    print("-", son_listas_iguales(listaE, listaF))
       
if __name__ == "__main__":
        prueba()

            