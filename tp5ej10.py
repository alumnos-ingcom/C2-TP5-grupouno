################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# CHECCARELLI Sergio -@checas
# *Agregar datos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Implementar una funcion que dado un numero entero positivo, retorne una cadena de texto con su representación binaria.
#Implementar una funcion que haga el proceso inverso; dada una cadena de texto, retorne el numero entero.

def decimal_a_binario(numero):
    
    lista_binaria = [] 
    
    while numero > 0: 
        lista_binaria.append(str(numero % 2)) # Los restos de las sucesivas divisiones los almacenamos en una lista
        numero = numero // 2 # Sólo queremos el resultado entero, por eso usamos //
        
    string_binario = "".join(lista_binaria[::-1]) # Damos vuelta la lista para obtener el orden correcto del número binario
    
    return string_binario
    
    
def binario_a_decimal(binario):
    
    numero_en_decimal = 0
    
    for caracter in binario:
        numero_en_decimal = (2 * numero_en_decimal) + int(caracter)
         
    return numero_en_decimal
    
    
def prueba():
    
    print(binario_a_decimal("110"), "en decimal")
    print("es igual a")
    print(decimal_a_binario(6), "en binario.")
    print()
    print(binario_a_decimal("1001001101"), "en decimal")
    print("es igual a")
    print(decimal_a_binario(589), "en binario.")


if __name__ == "__main__":
    prueba()