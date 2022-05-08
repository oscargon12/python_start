#Siempre crear las funciones de primeras por si necesitan llamarlas

def conversor(curr_type, v_dollar):
    pesos = float(input('Cuantos pesos ' + curr_type + ' tienes?: '))
    dolares = pesos / v_dollar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $ ' + dolares + ' dolares' )


menu = """
Bienvenido al conversor de monedas 💰

1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos

Elige una opción:
"""

option = int(input(menu))

if option == 1:
    conversor('Colombianos', 4000)
elif option == 2:
    conversor('Argentinos', 65)
elif option == 3:
    conversor('Mexicanos', 25)
else:
    print('Por favor ungresa una opción correcta')