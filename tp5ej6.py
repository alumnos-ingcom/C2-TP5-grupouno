################
# MARTIN DARRICADES Sebastián - @sebasamd sebasamd@gmail.com
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# Sergio Checcarelli - @checas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Reemplazar por las funciones del ejercicio

#Implementar una función que determine si una cadena con parentesis está balanceada.

def filtrar_cadena(cadena):
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
        return filtrada

def balance_cadena(cadena):
    """Esta funcion determina si una cadena se encuentra balanceada, devuelve valor 0 si no y 1 si lo esta."""
    i = 0
    largo = len(cadena) 
    if largo == 0:
        return 0
    while i < largo:
        if cadena[i] in "{[(":
            i += 1
        else:
            if cadena[i - 1] + cadena[i] in "{}" or \
                    cadena[i - 1] + cadena[i] in "[]" or \
                    cadena[i - 1] + cadena[i] in "()":
                    cadena = cadena[:i - 1] + cadena[i + 1:]
                    i -= 1
                    return 1

def prueba():
    print("Probando las funciones(TP5EJ6)")

    print("Ingrese una cadena para verificar si se encuentra balanceada: \n")
    cadena = input("Ingrese su cadena: ")
    filtrada = filtrar_cadena(cadena)
    verificar = balance_cadena(filtrada)
    print(verificar)
    
if __name__ == "__main__":
    prueba()

