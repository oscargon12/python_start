def es_primo(num):
    contador = 0 #si este cambia el num no sera primo

    for i in range(1, num + 1): # num + 1 para que alcance a tomar ese numero  no uno anterior
        if i == 1 or i == num:
            continue #Si i==1 o i== num saltese ese i
        if num % i == 0: #si num / i == 0 : contador!= 0
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def run():
    num = int(input('Escribe un numero: '))
    if es_primo(num):
        print('😀 Si es primo')
    else:
        print('🥵 No es primo')


if __name__ == '__main__':
    run()