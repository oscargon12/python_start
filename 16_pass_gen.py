import random

def gen_pass():
    #Hago listas de caracteres
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbol = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    all_chars = mayus + minus + nums + symbol #Creo una variable con todos los char

    password = [] #creo unalista vacia

    for i in range(10): #creo un ciclo
        random_char = random.choice (all_chars) #que saque un caracer al azar desde al_chars
        password.append(random_char) #Y lo inserte en el array 'password'
    
    #Se convierte el array de all_chars en string
    password = ''.join(password)

    return password

def run():
    password = gen_pass() #password, igual a lo que retorne la función gen_pass
    print('Your new pass is: ' + password)


if __name__ == '__main__':
    run()