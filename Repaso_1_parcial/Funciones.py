import json
import re

#funcion para importar el json

def importar_poke(path:str)->list:
    '''
    Esta funcion recibe un string como ruta y devuelve una lista del json extraido
    '''
    with open(path, 'r') as File:
        lista_pokemon = json.load(File)    
    return lista_pokemon['pokemones']

""" print(importar_poke("C:/Users/usuario/Desktop/PROGRAMACION UTN/1 Cuatri/ProgramacionYLaboratorio1/Repaso_1_parcial/pokedex.json")) """

#funcion para listar los ultimos elementos segun lo pida el usuario
def listar_ultimos_poke(lista:list, ultimos:int)->list:
    '''
    esta funcion recibe una lista de diccionarios y un valor para definir los elementos a listar

    retorna una lista con la cantidad seleccionada
    '''
    lista_poke = lista.copy()
    if(len(lista) < ultimos or ultimos == 0):
        retorno = ["Error en los parametros"]
    else:
        top_reverse = len(lista_poke) - ultimos
        retorno = lista_poke[top_reverse:]        
    return retorno

'''
para ordenar hay que buscar el minimo/maximo y retornar el indice de esa lista

declaro el indice en 0 y hago un for i in range(largo de la lista)
si es ascendende el el elemento en i es mayor al elemento en indice o descendente y el elemento en i es menor al indice entonces devuelvo el indice en esa posicion


para ordenar hay que haer un for de i in range(lista)
y adentro hay que declarar el indice del maximo / minimo con la funcion de buscar pero el parametro tiene que ser la lista desde i hasta el final y al final hay que sumarle i

si se encuentra un nuevo minimo hay que swapear



'''

#funcion busca min max
def buscar_min_max(lista:list, clave:str, tipo:str)->int:
    indice = 0
    for i in range(len(lista)):
        if(tipo == 'Asc' and lista[i][clave] < lista[indice][clave]) or (tipo == 'Desc' and lista[i][clave] > lista[indice][clave]):
            indice = i
    return indice

#funcion ordern

def orden(lista:list, clave:str, tipo:str)->list:
    nueva_lista = lista.copy()
    print(type(nueva_lista))
    for i in range(len(nueva_lista)):
        indice_max_min = buscar_min_max(nueva_lista[i:], clave, tipo) + i
        nueva_lista[i], nueva_lista[indice_max_min] = nueva_lista[indice_max_min], nueva_lista[i]
    return nueva_lista

