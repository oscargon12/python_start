#main function
def run():
    LIMITE = 1000 #las variables (constantes) sedefinen en mayuscula
    base = 2

    contador = 0 #estado inicial antes de entrar al ciclo
    potencia_2 = base**contador #estado inicial antes de entrar al ciclo
    while potencia_2 < LIMITE:
        print('2 elevado a la ' + str(contador) + ' es ' + str(potencia_2))
        contador = contador + 1 #iteraciones
        potencia_2 = base**contador #iteraciones

if __name__ == '__main__':
    run()