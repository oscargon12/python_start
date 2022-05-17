#listas en python son como arrays
nums = [5, 7, 34, 23, 88]
print (nums)

#accediendo a los elementos
objects = ['hola', 3, 4.5, True]
objects[0]
objects[1]
objects[3]

#insertando/eliminando elementos de la lista
#Agregaar
objects.append(False)
print(objects)

objects.append('mundo')
print(objects)

#eliminar: Elimina según el parametro index que se le de
objects.pop(1)
print(objects)