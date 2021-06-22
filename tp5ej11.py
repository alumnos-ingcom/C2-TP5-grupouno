################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# CHECCARELLI Sergio -@checas
# *Agregar datos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Un promedio móvil es una media no ponderada de una cantidad menor al total de un conjunto de valores en una serie de datos. Es una forma de controlar variaciones fuertes en la misma. Esta técnica permite ajustar el nivel de suavizado cambiando la cantidad de valores contiguos de la serie que entran en el calculo.

def promedio_movil(lista,promedio_elegido):
    """Esta funcion calcula el promedio movil solicitado a partir de una lista de numeros enteros"""
    #Mantengo el valor del promedio fijo
    promedio_movil = promedio_elegido
    indice_movil = 0
    #promedio_movil e indice_movil se incrementan para modificar el rango de datos tomados de la lista.
    lista_promediada = []
    largo_lista = len(lista)
    elementos_finales = promedio_elegido - 1
    #elementos_finales limita cuantos elementos puedo obtener de la lista en base al promedio elegido.
    for elemento in lista:
        while elementos_finales < largo_lista:
            lista_elementos = lista[(indice_movil):(promedio_movil)]
            sumados = 0
            #sumados representa la suma de cada promedio
            elementos_finales += 1
            for l in lista_elementos:
                sumados = sumados + l
            promedio = sumados / promedio_elegido
            promedio_movil += 1
            indice_movil += 1
            lista_promediada.append(promedio)
        return lista_promediada

def crear_lista(numeros):
    """Esta funcion crea una lista de cantidad de numeros enteros que se solicite"""
    lista = []
    for i in range(numeros):
        lista.append(i)
    return lista

def prueba():
    #Creo una lista de 100 elementos
    lista = crear_lista(100)
    promedio = promedio_movil(lista, 10)
    print(promedio)
    largo = len(promedio)
    print(largo)


if __name__ == "__main__":
    prueba()
