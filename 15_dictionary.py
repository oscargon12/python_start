#Diccionario == objetos

def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }

    print(mi_diccionario['llave1']) #1
    print(mi_diccionario['llave2']) #2
    print(mi_diccionario['llave3']) #3

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    print(poblacion_paises['Colombia']) #imprime 50372424

#Recorriendo diccionarios
    for pais in poblacion_paises.keys(): #imprime solo las llaves
        print(pais)
        #Argentina
        #Brasil
        #Colombia

    for habitantes in poblacion_paises.values(): #imprime solo los valores
        print(habitantes)
        #imprime 44938712
        #imprime 210147125
        #imprime 50372424

#Recorriendo keys y values
    for pais, poblacion in poblacion_paises.items(): #pais y habitantes son parametros
        print(pais + ' tiene ' + str(poblacion) + ' habitantes ')
        #Argentina tiene 44938712 habitantes
        #Brasil tiene 210147125 habitantes
        #Colombia tiene 50372424 habitantes

if __name__ == '__main__':
    run()