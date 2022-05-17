import random #importo el modulo random

def run():
    rand_num = random.randint(1, 100) #random.randint, crea un num aleatorio entre los parametros
    my_num = int(input('Adivina un numero entre 1 y 100: '))

    while my_num != rand_num: #mientras los numeros sean diferentes...
        if my_num < rand_num: #si el adivinado es menor al random
            print('Es un numero más grande!')
        else:
            print('Es un numero más pequeño!')
        my_num = int(input('Ingresa otro numero: ')) #Se define de nuevo my_num dentro del while
        
    print('Ganaste!') #finaliza el while si los números son iguales


if __name__ == '__main__':
    run()