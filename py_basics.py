#Variables

from operator import truediv
from wsgiref.validate import validator


num = 3
print(num)

num1 = 5
num2 = 6

final_num = num1 + num2
print(final_num)

# Tipos de datos
# Enteros
# numeros Flotantes
# Strings
# Booleans

#Strings
name = 'Oscar'
last_name = 'Gonzalez'

full_name = name + ' ' + last_name
print(full_name)

lot_names = name * 4
print(lot_names)

#Float
dec_num = 3.4
print(dec_num)

# boolean
is_user = True
vip_user = False
print(is_user)

#input
num1 = input('Escribe un numero: ')
# Escribe un numero: 4
print(num1) #4 as a text

num1 = int(num1) #int transforma el numero string en numero

num_dec = 4.5
int(4.5) #convierte los decimales en nteros
#4

# *** Operadores de logicos ***
# And
#Si todas las variables son verdaderas

is_student = True
work = False
is_student and work #False

# Or
#Alguno de los dos se cumple
is_student or work #True

# not
# Invierte el valor
not work # True, porque work era false

# *** Operadores de comparación ***
num1 = 5
num2 = 5
num1 == num2 # True

num3 = 7
num1 == num3 #False
num1!= num3 #True
num1 > num3 #False
num1 < num3 #True
num1 >= num3 #False
num1 >= num2 #True
num1 <= num3 #True




