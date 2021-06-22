
################
# MARTIN DARRICADES Sebastián - @sebasamd
# BOCCHIGLIERE Andrés - @AndresBochi - elmaildeandresbochi@gmail.com
# CHECCARELLI Sergio -@checas
# *Agregar datos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class Error_texto_no_encontrado(Exception):
    pass

def buscarString(textoBase, textoBuscar):
    try:
        resultado = textoBase.find(textoBuscar)
        if(resultado != -1 ):
            return resultado
        else: 
            resultado = ""
            raise Error_texto_no_encontrado
    except Error_texto_no_encontrado:
        print("La palabra no fue encontrada")
def prueba():
    textoBase = input("Ingrese el texto: ")
    textoBuscar = input("Ingrese la palabra a buscar: ")
    respuesta = buscarString(textoBase, textoBuscar)
    if(respuesta != None):
        print(respuesta)
    pass

if __name__ == "__main__":
    prueba()