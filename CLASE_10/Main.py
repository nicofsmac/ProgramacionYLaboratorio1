from Funciones import *

#Crear el menu

def menu_stark():
    lista_heroes = traer_data_json("C:/Users/usuario/Desktop/PROGRAMACION UTN/1 Cuatri/ProgramacionYLaboratorio1/CLASE_10/data_stark.json")
    while(True):
        print(
            '''
            1 - Listar TOP N heroes
            2 - Ordenar y listar heroes por altura. ('asc'/'desc')
            3 - Ordenar y listar heroes por fuerza('asc'/'desc')
            4 - Calcular promedio de cualquier key numerica. ('mayor'/'menor')
            5 - Buscar y listar heroes por inteligencia (good/average/high)
            6 - Exportar a CSV las listas ordenadas
            7 - Salir
            '''
        )
        respuesta = input()
        lista_resultado = lista_heroes.copy()
        if(respuesta == "1"):
            top = int(input("\nCantidad de heroes a mostrar?: "))
            lista_resultado = mostrar_heroes(lista_heroes, top)
            """ for heroe in lista_resultado:
                heroe = formato_lindo(heroe)
                print(heroe) """
        elif(respuesta == "2"):
            tipo_orden = input("\nEn que orden desea ordenar los datos? 'asc' o 'desc'\n")
            lista_resultado = ordenar_lista(lista_heroes,'altura',tipo_orden)
            """ for heroe in lista_resultado:
                heroe = formato_lindo(heroe)
                print(heroe) """
        elif(respuesta == "3"):
            tipo_orden = input("\nEn que orden desea ordenar los datos? 'asc' o 'desc'\n")
            lista_resultado = ordenar_lista(lista_heroes,'fuerza',tipo_orden)
            """ for heroe in lista_resultado:
                heroe = formato_lindo(heroe)
                print(heroe) """
        elif(respuesta == "4"):
            clave = input("\nque clave desea filtrar? 'peso' 'fuerza' o 'altura'\n")
            tipo_filtro = input("\nQue elementos desea filtrar en base al promedio? 'mayor' o 'menor'\n")
            lista_resultado = filtro_promedio(lista_heroes,clave,tipo_filtro)
            """ for heroe in lista_resultado:
                heroe = formato_lindo(heroe)
                print(heroe)
            print(calcula_promedio(lista_heroes, clave)) """
        elif(respuesta == "5"):
            busqueda = input("\nQue tipo de inteligencia desea buscar? 'good' 'average' o 'high'")
            buscar_inteligencia(lista_heroes, busqueda)
        elif(respuesta == "6"):
            exportar_csv(lista_resultado,"./CLASE_10/heroes.csv")
        else:
            break

menu_stark()