#Convierte cualquier palabra en una lista de letras únicas ordenadas alfabéticamente

def deconstruir_palabra(palabra):
    palabra = list(set(list(palabra)))
    palabra.sort()
    return palabra
    


print(deconstruir_palabra(input('Introduzca una palabra: ')))