################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# CHECCARELLI Sergio -@checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Implementar una funcion que retorne una lista con todos los factoriones menores a 1.499.999

def encontrar_factoriales(numero):
    """
    Esta función devuelve el factorial de un número del 0 al 9 solicitado en el argumento.
    
    El factorial de un número entero positivo se define como el producto de todos
    los números naturales anteriores o iguales a él.
    
    """
    
    lista_factoriales = [1,]
    resultado = 1
    
    for i in range (9):
        resultado = resultado * (i + 1)
        lista_factoriales.append(resultado)
    
    # print(lista_factoriales)
    
    return lista_factoriales[numero]


def encontrar_factoriones():
    """
    Devuelve una lista con con todos los factoriones menores a 1.499.999
    
    """
    # Si quieren una prueba de escritorio de la función, des-comenten los prints de ésta función. Pero bajen el número de
    # el lazo while para que no se haga eterno!!!
    
    busqueda = 0
    lista_factoriones = []
    
    while busqueda < 1500000:
                # print()
                resultado_total = 0
                for caracter in str(busqueda):
                    resultado_parcial = encontrar_factoriales(int(caracter))
                    # print(f"El factorial de {caracter} es {resultado_parcial}")
                    resultado_total += resultado_parcial
                    
                # print(f"El resultado total de {busqueda} es {resultado_total}")
                if busqueda == resultado_total:
                    lista_factoriones.append(busqueda)
                busqueda += 1

    return lista_factoriones


def prueba():
    
    print(encontrar_factoriones())
    
    
if __name__ == "__main__":
    prueba()

