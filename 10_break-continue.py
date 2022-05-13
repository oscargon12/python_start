#El continue hace que segun una condición se salte a la otra iteracion

def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue #Si el múdulo es distinto de cero, debe saltarlo (solo imprime pares)
    #     print(contador)

#El break hace que la iteracion se pare, segun una condicion 
    # for i in range(10000):
    #     print(i)
    #     if i == 548:
    #         break

    texto = input('Ingresa una palabra: ')
    for l in texto:
        if l == 'o':
            break
        print(l)

if __name__ == '__main__':
    run()