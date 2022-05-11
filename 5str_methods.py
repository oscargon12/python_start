nombre = input('cual es tu nombre?: ')
#cual es tu nombre?: Oscar 
nombre.upper() #string en mayúsculas
#'OSCAR '
nombre.capitalize() #string con letra capital
#'Oscar '
nombre = nombre.capitalize()
nombre #'Oscar '
nombre = nombre.strip() #Elimina la basura (espacios) antes y despues del string
nombre #'Oscar '

nombre = nombre.lower()
nombre #'oscar'
nombre = nombre.replace('o', 'a') #Reemplaza la 1ra letra que pongo como argumento, por la 2da
nombre #'ascar'
nombre[0]
'O' #Primera letra de la cadena 'Oscar'
letra = nombre[0]
letra #'O'
len('Hola mundo')
10 #numero de caracteres en 'Hola mundo'

#** Slice (Rebanadas)**
nombre = 'Oscar'
nombre[0:2] #desde el primer elemento hasta antes del tercero:
'Os'
nombre[0:3] #desde el primer elemento hasta antes del cuarto:
'Osc'
nombre[:3] #desde el primer elemento hasta antes del cuarto:
'Osc'
nombre[3:] #desde el tercer elemento hasta el ultimo:
'ar'
nombre[1:4] #desde el 2do hasta antes del 5:
'sca'
nombre[0:6:2] #desde el primer elemento hasta antes del sexto, (: de dos en dos):
'Ocr'
nombre[0::2] #desde el primero hasta el ultimo (: de dos en dos):
'Ocr'
nombre[::-1] #desde el ultimo hasta el primero (:-1 en orden inverso):
'racsO'
