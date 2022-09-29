import json

#funcion para cargar el json
def traer_data_json(path:str)->list:
    '''
    Esta funcion recibe un string que indica la ruta del json.

    retorna la lista de heroes contenida dentro de la clave 'heroes' del json
    '''
    with open(path, "r") as file:
        lista_heroes = json.load(file)
    return lista_heroes['heroes']


#funcion para hacer el top N
def mostrar_heroes(lista:list, top:int)->list:
    '''
    Esta funcion recibe una lista que contiene diccionarios donde cada uno representa un heroe
    Tambien recibe un top que es un entero y representa la cantidad de elementos a mostrar

    Retorna una lista con la cantidad de elementos elegida
    '''
    if(len(lista) == 0 or top > len(lista)):
        retorno = "Error en la llamda a la funcion. Reintentar con otro valor top"
    else:
        nueva_lista = lista.copy()
        retorno = nueva_lista[:top]    
    return retorno

#funcion para formatear las listas
def formato_lindo(heroe:dict):
    '''
    Recibe un diccionario que representa un heroe

    Retorna el heroe con un formato mas prolijo
    '''
    if(type(heroe) != dict):
        retorno = "Error en el tipo de datos"
    else:
        retorno = '\nNombre: {0} -- Altura: {1} -- Peso: {2} -- Fuerza: {3}'.format(heroe['nombre'], heroe['altura'], heroe['peso'], heroe['fuerza'] )    
    return retorno

#funcion para buscar minimo o maximo
def busca_min_max(lista:list, clave:str='altura', tipo_orden:str="asc"):
    '''
    Recibe una lista de diccionarios, una clave para saber que campo debe ser ordenado y un tipo de orden (asc/desc)

    Retorna el indice del heroe minimo o maximo
    '''
    nueva_lista = lista.copy()
    indice = 0
    for i in range(len(nueva_lista)):
        if(tipo_orden == "asc" and nueva_lista[i][clave] < nueva_lista[indice][clave]) or (tipo_orden == "desc" and nueva_lista[i][clave] > nueva_lista[indice][clave]):
            indice = i
    return indice

#funcion para ordenar
def ordenar_lista(lista:list, clave:str='altura', tipo_orden:str="asc"):
    '''
    Recibe una lista de diccionarios, una clave para saber que campo debe ser ordenado y un tipo de orden (asc/desc)

    Retorna una lista ordenada por la clave y por el orden. 
    '''
    nueva_lista = lista.copy()
    for i in range(len(nueva_lista)):
        indice_min_max = busca_min_max(nueva_lista[i:], clave, tipo_orden) + i
        nueva_lista[i], nueva_lista[indice_min_max] = nueva_lista[indice_min_max], nueva_lista[i]
    return nueva_lista

""" check = ordenar_lista(traer_data_json("C:/Users/usuario/Desktop/PROGRAMACION UTN/1 Cuatri/ProgramacionYLaboratorio1/CLASE_10/data_stark.json"), 'altura', 'asc') 

for heroe in check:
    print(formato_lindo(heroe))
 """
""" print(busca_min_max(traer_data_json("C:/Users/usuario/Desktop/PROGRAMACION UTN/1 Cuatri/ProgramacionYLaboratorio1/CLASE_10/data_stark.json"), 'altura', 'asc')) """

#funcion para obtener el promedio
def calcula_promedio(lista:list, clave:str):
    '''
    Recibe una lista de diccionarios que representan un heroe y una clave que debe ser numerica para obtener el promedio.

    Retorna el promedio calculado de acuerdo a la clave 
    '''
    contador_clave = 0
    acumulador_clave = 0
    for elemento in lista:
        if(type(elemento[clave]) == float or type(elemento[clave]) == int):
            contador_clave += 1
            acumulador_clave += elemento[clave]
    promedio_clave = acumulador_clave / contador_clave

    return promedio_clave

#funcion para filtrar en base al promedio
def filtro_promedio(lista:list, clave:str, tipo_filtro:str):
    '''
    Recibe una lista, la clave para calcular el promedio y el tipo de filtro (mayor o menor al promedio)

    Retorna una lista filtrada en base a las condiciones  
    '''
    nueva_lista = lista.copy()
    promedio = calcula_promedio(nueva_lista, clave)
    lista_filtrada = []
    for elemento in nueva_lista:
        if(tipo_filtro == "mayor" and elemento[clave] > promedio) or (tipo_filtro == "menor" and elemento[clave] < promedio):
            lista_filtrada.append(elemento)
    return lista_filtrada


""" print(filtro_promedio(traer_data_json("C:/Users/usuario/Desktop/PROGRAMACION UTN/1 Cuatri/ProgramacionYLaboratorio1/CLASE_10/data_stark.json"), 'peso', 'menor')) """

#funcion para buscar heroes por inteligencia
def buscar_inteligencia(lista:list,busqueda:str):
    '''
    recibe una lista de diccionarios y termino para la busqueda dentro de la clave inteligencia de esos diccionarios

    retorna una lista de heroes que cumplan con esa busqueda
    '''
    if(busqueda != "high" and busqueda != "average" and busqueda != 'good'):
        retorno = ["No  hay elementos compatibles con esa busqueda"]
    else:
        nueva_lista = lista.copy()
        lista_final = []
        for elemento in nueva_lista:
            if(elemento['inteligencia'] == busqueda):
                lista_final.append(elemento)
        retorno = lista_final
    
    return retorno


#funcion para exportar CSV
def exportar_csv(lista:list, path:str):
    '''
    recibe una lista de diccionarios y un path donde guardar el CSV

    devuelve un CSV donde cada linea es un diccionario en el que cada clave esta separada por comas
    '''
    with open(path,"w") as file:
        for elemento in lista:
            file.write("{0},{1},{2},{3},{4},{5}\n".format(elemento['nombre'],elemento['identidad'], elemento['altura'], elemento['peso'], elemento['fuerza'], elemento['inteligencia']))