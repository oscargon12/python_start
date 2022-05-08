#Funciones
# def print_msg():
#     print('Mensaje especial')
#     print('Estoy usando funciones')

# print_msg()
# print_msg()
# print_msg()

#Excercise

from unittest import result


def conversation(msg):
    print('Hola')
    print('Como estas')
    print(msg) #Parametro de la función
    print('Adios')

option = int(input('Elije una opcion (1, 2, 3): '))
if option == 1:
    conversation('Elegiste la opcion 1')  #Envio argumento a la funcion
elif option == 2:
    conversation('Elegiste la opcion 2')
elif option == 3:
    conversation('Elegiste la opcion 3')
else:
    print('Elige una opcion correcta')

def suma(a, b):
    print('Se suman dos numeros: ')
    result = a + b
    return result

sumatoria = suma(1, 4) #sumatoria es una variable que contiene el return de la funcion
print('El resultado es ' + sumatoria)