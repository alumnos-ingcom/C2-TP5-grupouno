################
# MARTIN DARRICADES Sebastián - @sebasamd sebasamd@gmail.com
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# Sergio Checcarelli - @checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Reemplazar por las funciones del ejercicio

#Implementar una función que determine si una cadena con parentesis está balanceada.

def limpiar_cadena(cadena):
    """Esta funcion deja solo los caracteres "{[()]}" de una cadena."""
    i = 0
    validos = ("{[()]}")
    largo = len(cadena)
    filtrada = []
    while i < largo:
        for n in cadena:
            i += 1
            if (n) in validos:
                filtrada.append(n)
        if not filtrada:
            return "["
        return filtrada

#def transformar_tupla(lista):
#    largo = len(lista)
#    i = 0
#    tupla = str()
#    while i < largo:
#        tupla = tupla + str(lista[i]) + ", "
#        i += 1
#    return tupla

def balance_cadena(cadena):
    """Esta funcion determina si una cadena con parentesis está balanceada"""
    i = 0
    while i < len(cadena):
        if cadena[i] in "{[(":
            print("1er paso")
            i += 1
        else:
            if cadena[i - 1] + cadena[i] in "{}" or \
                    cadena[i - 1] + cadena[i] in "[]" or \
                    cadena[i - 1] + cadena[i] in "()":
                    cadena = cadena[:i - 1] + cadena[i + 1:]
                    i -= 1
                    return 1
            else:
                return 0

def prueba():
    print("Probando las funciones(TP5EJ6)")

    print("Ingrese una cadena para verificar si se encuentra balanceada: \n")
    cadena = input("Ingrese su cadena: ")
    filtrada = limpiar_cadena(cadena)
    print(type(filtrada))
    print(filtrada)
    
#    tupla = transformar_tupla(filtrada)
#    print(f"\n tupla {tupla}")
#    print(type(tupla))

#    verificar = balance_cadena(tupla)
#    print(verificar)
    
    print("\n string")
    verificar2 = balance_cadena(filtrada)
    print(verificar2)
    
if __name__ == "__main__":
    prueba()

