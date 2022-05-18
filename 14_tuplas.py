#Tuplas
#Similares a las listas o arrays, pero no permiten agregar o eliminar elementos, son inmutables
#Las tuplas consumen menos memoria que las listas, son mucho mas rapidas

mi_tupla = (1,2,3,4,5) #se hacen con parentesis
#mi_tupla.append(6) #Error
#mi_tupla.pop(1) #Error

#las tuplas si se pueden recorrer
for num in mi_tupla:
    print(num)

tupla2 = ('hola', 3, 4.5, True) #Permito distintos tipos de dato
print(tupla2) 
