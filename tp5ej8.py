################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# CHECCARELLI Sergio -@checas
# *Agregar datos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def codificar(texto, desplazamiento):
    resultado = ""    
    for i in range(len(texto)):
        caracter = texto[i]
        if(ord(caracter)>= 48 and ord(caracter) <= 57):
            resultado += chr((ord(caracter) + int(desplazamiento) - 48) % 10 + 48)
        else:
            if(caracter.isupper()):
                resultado += chr((ord(caracter) + int(desplazamiento) - 65) % 26 + 65)
            else:
                resultado += chr((ord(caracter) + int(desplazamiento) - 97) % 26 + 97)
    return resultado
    

def decodifcar(textoCodificado, desplazamiento):
    resultado = ""    
    for i in range(len(textoCodificado)):
        caracter = textoCodificado[i]
        if(ord(caracter)>= 48 and ord(caracter) <= 57):
            resultado += chr((ord(caracter) - int(desplazamiento) - 48) % 10 + 48)
        else:
            if(caracter.isupper()):
                resultado += chr((ord(caracter) - int(desplazamiento) - 65) % 26 + 65)
            else:
                resultado += chr((ord(caracter) - int(desplazamiento) - 97) % 26 + 97)
    return resultado

def prueba():
    texto = input("Ingrese el texto a codificar: ")
    desplazamiento = input("Ingrese el desplazamiento: ")
    texto_codificado = codificar(texto, desplazamiento)
    print(texto_codificado)
    print("El texto decodificado es: ")
    print(decodifcar(texto_codificado, desplazamiento))
    pass   

if __name__ == "__main__":
    prueba()

