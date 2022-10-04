import json
import re

#funcion para cargar el json

def cargar_json(path:str):
    '''
    funcion que recibe un str que representa el path donde esta el archivo

    Devuelve una lista de diccionarios donde cada uno es un heroe
    '''
    with open(path, 'r') as file:
        lista_starwars = json.load(file)
    return lista_starwars['results']

#castear todas las claves numericas
def castear_valores(lista:list)->list:
    '''
    esta funcion sirve para castear todos los valores de los diccionarios que estan en formato string

    retorna la misma lista con los valores casteados
    '''
    nueva_lista = lista.copy()
    for personaje in nueva_lista:
        personaje['height'] = int(personaje['height'])
        personaje['mass'] = int(personaje['mass'])
    return nueva_lista

#buscar minimo maximo para ordenar
def busca_min_max(lista:list, clave:str)->int:
    '''
    esta funcion recibe una lista de diccionarios y una clave para evaluarlos

    retorna el nuemero de indice que corresponde al mayor de ellos
    '''
    lista_resultado = castear_valores(lista)
    indice = 0
    for i in range(len(lista_resultado)):
        if(lista_resultado[i][clave] > lista_resultado[indice][clave]):
            indice = i
    return indice

#funcion para ordenar
def ordenar_personajes(lista:list, clave:str)->list:
    '''
    esta funcion recibe una lista de diccionarios y una clave para ordenarlos

    retorna la misma lista recibida pero ordenada segun la clave
    '''
    lista_resultado = castear_valores(lista)
    for i in range(len(lista_resultado)):
        indice_ref = busca_min_max(lista_resultado[i:], clave) + i
        lista_resultado[i], lista_resultado[indice_ref] = lista_resultado[indice_ref], lista_resultado[i]
    return lista_resultado

#funcion para listar los generos
def listar_generos(lista:list)->list:
    '''
    esta funcion recibe una lista y recorre todos los elementos en la clave genero

    devuelve un set unico con los generos
    '''
    lista_resultados = castear_valores(lista)
    lista_generos = []
    for personaje in lista_resultados:
        lista_generos.append(personaje['gender'])
    lista_generos = set(lista_generos)
    return lista_generos

#funcion para mostrar el personaje mas alto de cada genero
def mostrar_mas_alto_genero(lista:list, clave:str):
    '''
    esta funcion recibe una lista y primero separa en disferentes listas por genero y 
    luego busca el mayor

    retorna un string por cada genero
    '''
    lista_resultado = castear_valores(lista)
    tipos_genero = listar_generos(lista_resultado)
    lista_male = []
    lista_female = []
    lista_na = []
    for personaje in lista_resultado:
        if(personaje['gender'] == 'male'):
            lista_male.append(personaje)
        elif(personaje['gender'] == 'female'):
            lista_female.append(personaje)
        elif(personaje['gender'] == 'n/a'):
            lista_na.append(personaje)
    male_mas_alto = ordenar_personajes(lista_male,clave)
    female_mas_alto = ordenar_personajes(lista_female,clave)
    na_mas_alto = ordenar_personajes(lista_na,clave)
    retorno = '''
            El personaje con genero 'male' mas alto es {0}\n
            El personaje con genero 'female' mas alto es {1}\n
            El personaje con genero 'n/a' mas alto es {2}
            '''.format(male_mas_alto[0]['name'], female_mas_alto[0]['name'], na_mas_alto[0]['name'] )
    return retorno

#funcion para armar un buscador de personajes
def buscador_personajes(lista:list, clave:str, busqueda:str)->list:
    '''
    esta funcion recibe una lista de personajes, una clave para saber donde buscar
    y un valor de busqueda para buscar dentro de esas claves

    retorna un lista con personajes que cumplan esa condicion
    '''
    """ nueva_lista = castear_valores(lista)
    lista_resultados = []
    for personaje in nueva_lista:
        retorno = re.findall('^[\busqueda']$', personaje[clave])    
    return retorno """

#funcion para exportar a csv
def exportar_csv(lista:list, path:str):
    '''
    esta funcion recibe una lista de personajes y un path para guardar el archivo

    retorna un archivo CSV donde cada linea representa un personaje
    '''
    lista_copia = lista.copy()
    with open(path, 'w') as file:
        for personaje in lista_copia:
            file.write("{0},{1},{2},{3}\n".format(personaje['name'],personaje['height'],personaje['mass'],personaje['gender']))
        


