'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones

def starwars_app():
    lista_personajes = funciones.cargar_json("PP_STARWARS/data.json")
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            lista_resultado = funciones.ordenar_personajes(lista_personajes,'height')
            print(lista_resultado)
        elif(respuesta=="2"):
            print(funciones.mostrar_mas_alto_genero(lista_personajes,'height'))
        elif(respuesta=="3"):
            lista_resultado = funciones.ordenar_personajes(lista_personajes,'mass')
            print(lista_resultado)
        elif(respuesta=="4"):
            clave = input('\nEn que categoria desea buscar?\n')
            busqueda = input('\nIngrese un string para iniciar la busqueda\n')
            """ lista_resultado = funciones.buscador_personajes(lista_personajes,clave, busqueda) """
            print("no funciona")
        elif(respuesta=="5"):
            funciones.exportar_csv(lista_resultado,"PP_STARWARS/export.csv")
        elif(respuesta=="6"):
            break


starwars_app()

