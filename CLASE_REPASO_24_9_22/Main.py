from Funciones import *
'''
otra forma de import es 

import Funciones -> (se llama a la biblioteca)

y luego para usarlas es Funciones.cargar_json() -> ()
'''

#crear el menu
def paulina_app():
    lista_videos = cargar_json("path")
    while(True):
        print(
            '''
            1 - Listar TOP N videos
            2 - Ordenar videos por duracion (UP/DOWN)
            3 - Ordenar videos por cantidad de views (UP/DOWN)
            4 - Buscar videos por titulos
            5 - Exportar lista de videos a CSV
            6 - Salir
            '''
        )
        respuesta = input()
        if(respuesta == "1"):
            top = int(input("\nCantidad de elementos a mostrar?: "))
            #crear una funcion para validar todo

            mostrar(lista_videos[:top])
        elif(respuesta == "2"):
            pass
        elif(respuesta == "3"):
            pass
        elif(respuesta == "4"):
            pass
        elif(respuesta == "5"):
            pass
        else:
            break

def buscar_minimo(lista:list)->int:
    '''
    buscar un minimo de una lista de diccionarios con claves especificas

    '''
                                                                                                                                                                            

#sort functions
def nahuel_sort(lista:list):
    lista_ordenar = lista.copy() # lista[:]

