from Funciones import *

def pokemon_menu():
    '''
    Esta funcion devuelve un menu por consola que permite acceder a distintas funciones
    '''

    lista_poke = importar_poke("C:/Users/usuario/Desktop/PROGRAMACION UTN/1 Cuatri/ProgramacionYLaboratorio1/Repaso_1_parcial/pokedex.json")
    while(True):
        print('''
        1 - Listar los ultimos N Pokemon de la lista. Ingresar el numero deseado.
        2 - Ordenar y listar pokemon por poder. 'Asc' o 'Desc'
        3 - Ordenar y listar pokemon por ID. 'Asc' o 'Desc'
        4 - Promedio cantidad promedio de: 'evoluciones' 'fortalezas' 'debilidades' 'tipos'
        5 - Buscar pokemon por tipo. Elegir un tipo para la busqueda.
        6 - Exportar a CSV la opcion elegida.
        7 - Salir
        ''')
        respuesta = input()
        lista_resultado = lista_poke
        if(respuesta == "1"):
            valor = int(input("\Ingrese el valor de elementos a filtrar empezando desde el final de la lista\n"))
            lista_resultado = listar_ultimos_poke(lista_poke,2)
            print(lista_resultado)
        elif(respuesta == "2"):
            lista_resultado = orden(lista_poke, 'poder', 'Asc')
            print(lista_resultado)
        elif(respuesta == "3"):
            pass
        elif(respuesta == "4"):
            pass
        elif(respuesta == "5"):
            pass
        elif(respuesta == "6"):
            pass
        elif(respuesta == "7"):
            break

pokemon_menu()