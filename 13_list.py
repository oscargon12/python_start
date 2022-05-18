#listas en python son Arrays
nums = [5, 7, 34, 23, 88]
print (nums)

#accediendo a los elementos
objects = ['hola', 3, 4.5, True]
objects[0] #'hola' #accedo a los elementos con los indices
objects[1] #3
objects[3] #True

#insertando/eliminando elementos de la lista
#Agregaar
objects.append(False)
print(objects) #['hola', 3, 4.5, True, False]

objects.append('mundo')
print(objects) #['hola', 3, 4.5, True, False, 'mundo']

#eliminar: Elimina según el parametro index que se le de
objects.pop(1)
print(objects)#['hola', 4.5, True, False, 'mundo']

#Recorriendo la lista (Igual que con un string)
for element in objects: 
    print(element)
#'hola'
#4.5
#True
#False
#mundo

#Metodos de slice e invert
invert = objects[::-1] #desde el ultimo hasta el primero (:-1 en orden inverso):
print(invert) #['mundo', False, True, 4.5, 'hola']

bit = objects[1:3] #desde el 2do hasta antes del 4
print(bit) #[4.5, True]

#operaciones con listas
nums1 = [1,2,3,4]
nums2 = [5,6,7,8]

total_sum = nums1 + nums2
print(total_sum) #[1, 2, 3, 4, 5, 6, 7, 8]

total_mult = nums1 * 5
print(total_mult) #[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]