import re


def palindromo(palabra):
    palabra = palabra.replace(' ', '') #se quitan los espacios
    palabra = palabra.lower() #se pone toda en lowercase
    palabra_invertida = palabra[::-1] #Se invierte el orden con el splice -1
    if palabra == palabra_invertida: #si la invertida es igual a la original...
        return True #retorna True
    else:
        return False

#Función principal
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('SI Es palíndromo 😁')
    else:
        print('NO es palindromo 🥵')


if __name__ == '__main__': #Entry point (punto de entrada) de todos los programas de python
    run()