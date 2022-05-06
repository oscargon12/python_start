#Variables y condicionales 

#---Pesos a dolar---
# pesos = input('Cuantos pesos tienes?: ')
# pesos = float(pesos) #float transforma en decimal
# v_dolar = 4000

# dolares = pesos / v_dolar
# dolares = round(dolares, 2) #Redondea a (2) decimales
# dolares = str(dolares)
# print('Tienes $ ' + dolares + ' dolares' )

#---Dolares a pesos---
# dollars = float(input('How many dollars do you have?: '))
# v_peso = 4000

# dollar = dollars * v_peso
# dollar = round(dollar, 2)
# dollar = str(dollar)
# print('You have ' + dollar + ' pesos colombianos')

#Menu de conversión
menu = """
Bienvenido al conversor de monedas 💰

1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos

Elige una opción:
"""
#La triple comilla doble me deja ingresar texto con salto de línea

option = int(input(menu))

if option == 1:

    pesos = float(input('Cuantos pesos colombianos tienes?: '))
    v_dolar = 4000

    dolares = pesos / v_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $ ' + dolares + ' dolares' )
elif option == 2:

    pesos = float(input('Cuantos pesos argentinos tienes?: '))
    v_dolar = 65

    dolares = pesos / v_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $ ' + dolares + ' dolares' )
elif option == 3:

    pesos = float(input('Cuantos pesos mexicanos tienes?: '))
    v_dolar = 25

    dolares = pesos / v_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $ ' + dolares + ' dolares' )
else:
    print('Por favor ungresa una opción correcta')

