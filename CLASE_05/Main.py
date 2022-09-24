from tkinter import Menu
from data_stark import lista_personajes

#punto 0
def stark_normalizar_datos(lista_heroes:list)->list:
    '''
    La funcion recorre la lista recibida y convierte las keys al tipo de dato correcto (si corresponde)
    Imprime un mensaje si hubo al menos 1 jey modificada

    Recibe como parametro lista_heroes que debe ser una lista que contenga diccionarios como elementos.

    Retorna una lista parecida a la recibida pero con los datos modificados si corresponde
    '''
    if(type(lista_heroes) != list or len(lista_heroes) == 0):
        print("Error: Lista de héroes vacía")
    else:
        contador_modificaciones = 0
        for heroe in lista_heroes:
            if(type(heroe['altura']) != float):
                heroe['altura'] = float(heroe['altura'])
                contador_modificaciones += 1
            if(type(heroe['peso']) != float):
                heroe['peso'] = float(heroe['peso'])
                contador_modificaciones += 1
            if(type(heroe['fuerza']) != int):
                heroe['fuerza'] = int(heroe['fuerza'])
                contador_modificaciones += 1
        if(contador_modificaciones > 0):
            print("Datos normalizados")
        return lista_heroes

def obtener_nombre(heroe:dict)->str:
    '''
    La funcion modifica la clave 'nombre' y modifica el formato del mismo

    Recibe el parametro heroe que es un diccionario.

    Retorna un string formateado de este estilo 'Nombre: Howard the Duck'
    '''

    if(type(heroe) != dict or heroe.keys == False):
        print("Error en el tipo de datos")
    else:
        nuevo_nombre = 'Nombre: {0}'.format(heroe['nombre'])
    
    return nuevo_nombre

def imprimir_dato(dato:str):
    '''
    La funcion imprime un string en consola

    Recibe el parametro 'dato' que debe ser del tipo string

    No retorna ningun valor pero imprime en pantalla el string recibido
    '''
    if(type(dato) != str):
        print("Error en el tipo de dato recibido")
    else:
        print(dato)

def stark_imprimir_nombres_heroes(lista:list):
    '''
    La funcion imprime en consola los nombres de los heroes

    Recibe el parametro 'lista' que debe ser una lista que contenga diccionarios

    Retorna -1 si la lista recibida esta vacia
    '''
    if(len(lista) == 0):
        return -1
    else:
        for heroe in lista:
            imprimir_dato(obtener_nombre(heroe))    
        return 1

#----------------------Ejercicio 2-----------------
def obtener_nombre_y_dato(heroe:dict,clave:str)->str:
    '''
    La funcion devuelve un string con nombre y clave (cualquiera sea) elegida a imprimir

    Recibe los parametros 'heroe' que debe ser un diccionario y 'clave' que debe ser un str 
    que represente alguna clave dentro de ese diccionario.

    Retorna un string formateado de este estilo 'Nombre: Venom | fuerza: 500'
    '''
    if(type(heroe) != dict or type(clave) != str):
        print("Error en los parametros recibidos")
    else:
        resultado_formateado = 'Nombre: {0} | {1}: {2}'.format(heroe['nombre'], clave, heroe[clave])

        return resultado_formateado

#----------------------Ejercicio 3-----------------
def stark_imprimir_nombres_alturas(lista:list):
    '''
    La funcion imprime nombre y altura utilizando la funcion obtener_nombre_y_dato()

    Recibe como parametro a 'lista' que debe ser una lista que contenga 
    diccionarios como elementos

    Retorna -1 si la lista esta vacia o imprime lo solicitado en consola
    ''' 

    if(len(lista) == 0):
        return -1
    else:
        for heroe in lista:
            print(obtener_nombre_y_dato(heroe, 'altura'))
        return 1

#----------------------Ejercicio 4-----------------
def calcular_max(lista:list, clave:str)->dict:
    '''
    La funcion devuelve un diccionario que representa el maximo segun
    la clave que reciba

    Recibe como parametro a 'lista' que es una lista que contiene diccionarios y
    'clave' que es un string para acceder a alguna key de esos diccionarios.
    Las claves deben ser peso, altura o fuerza.

    Retorna un diccionario con el objeto maximo. 
    '''
    if(type(lista) != list or len(lista) == 0 or type(clave) != str):
        print("Error en los tipos de datos recibidos")
    elif(clave != 'altura' and clave != 'peso' and clave != 'fuerza'):
        print("Error en la clave recibida")
    else:
        lista = stark_normalizar_datos(lista)
        heroe_max = lista[0]
        for heroe in lista:
            if(heroe[clave] > heroe_max[clave]):
                heroe_max = heroe
        return heroe_max

def calcular_min(lista:list, clave:str)->dict:
    '''
    La funcion devuelve un diccionario que representa el minimo segun
    la clave que reciba

    Recibe como parametro a 'lista' que es una lista que contiene diccionarios y
    'clave' que es un string para acceder a alguna key de esos diccionarios.
    Las claves deben ser peso, altura o fuerza.

    Retorna un diccionario con el objeto minimo. 
    '''
    if(type(lista) != list or len(lista) == 0 or type(clave) != str):
        print("Error en los tipos de datos recibidos")
    elif(clave != 'altura' and clave != 'peso' and clave != 'fuerza'):
        print("Error en la clave recibida")
    else:
        lista = stark_normalizar_datos(lista)
        heroe_min = lista[0]
        for heroe in lista:
            if(heroe[clave] < heroe_min[clave]):
                heroe_min = heroe
        return heroe_min

def calcular_max_min_dato(lista:list, tipo_calculo:str ,clave:str)->dict:
    '''
    La funcion devuelve un diccionario que representa el maximo o minimo segun
    la clave y el tipo de calculo que reciba

    Recibe como parametro a 'lista' que es una lista que contiene diccionarios.
    'clave' que es un string para acceder a alguna key de esos diccionarios.
    Las claves deben ser peso, altura o fuerza.
    'tipo_calculo' que es un string que representa el tipo de calculo
    a realizar ('maximo' o 'minimo')

    Retorna un diccionario con el objeto minimo o maximo. 
    '''
    if(type(lista) != list or len(lista) == 0 or type(clave) != str or type(tipo_calculo) != str):
        print("Error en los tipos de datos recibidos")
    elif(clave != 'altura' and clave != 'peso' and clave != 'fuerza'):
        print("Error en la clave recibida")
    else:
        if(tipo_calculo == 'maximo'):
            resultado = calcular_max(lista, clave)
        elif(tipo_calculo == 'minimo'):
            resultado = calcular_min(lista, clave)
        
        return resultado
    
def stark_calcular_imprimir_heroe(lista:list, tipo_calculo:str, clave:str):
    '''
    La funcion devuelve un mensaje personalzado que representa el maximo o minimo segun
    la clave y el tipo de calculo que reciba

    Recibe como parametro a 'lista' que es una lista que contiene diccionarios.
    'clave' que es un string para acceder a alguna key de esos diccionarios.
    Las claves deben ser peso, altura o fuerza.
    'tipo_calculo' que es un string que representa el tipo de calculo
    a realizar ('maximo' o 'minimo')

    Retorna -1 si la lista esta vacia o imprime el mensaje de este estilo
    'Mayor altura: Nombre: Howard the Duck | altura: 79.34'
    '''
    if(len(lista) == 0):
        return -1
    else:
        if(tipo_calculo == 'maximo'):
            resultado = calcular_max(lista, clave)
            print("Mayor {0}: {1}".format(clave, obtener_nombre_y_dato(resultado, clave)))
        elif(tipo_calculo == 'minimo'):
            resultado = calcular_min(lista, clave)
            print("Menor {0}: {1}".format(clave, obtener_nombre_y_dato(resultado, clave)))

#----------------------Ejercicio 5-----------------
def sumar_dato_heroe(lista:list, clave:str):
    '''
    La funcion devuelve el resultado de la suma segun la clave ingresada

    Recibe 'lista' que debe ser una lista que contenga diccionarios y 'clave'
    que representa una key dentro de esos diccionarios.

    Retorna un entero o un flotante como resultado de la suma.
    '''
    if(type(lista) != list or type(clave) != str):
        print("Error en los datos recibidos")
    else:
        sumatoria = 0
        for heroe in lista:
            sumatoria += heroe[clave]
        
        return sumatoria

def dividir(dividendo:float, divisor:float):
    '''
    me falta la doc
    '''
    if(divisor == 0):
        return 0
    else:
        division = dividendo / divisor
        
        return division

def calcular_promedio(lista:list,clave:str):
    '''
    me falta la doc
    '''
    if(type(lista) != list or type(clave) != str):
        print("Error en los datos recibidos")
    else:
        totales = sumar_dato_heroe(lista, clave)
        contador_heroes = 0
        for heroe in lista:
            if(heroe[clave] != ""):
                contador_heroes += 1
        promedio = dividir(totales, contador_heroes)

        return promedio

def stark_calcular_imprimir_promedio_altura(lista:list):
    '''
    falta la doc
    '''
    if(type(lista) != list):
        return -1
    else:
        promedio_alturas = calcular_promedio(lista, 'altura')

        print("El promedio de alturas es {0}".format(promedio_alturas))

#----------------------Ejercicio 6-----------------

def imprimir_menu():
    '''
    falta doc
    '''
    menu_stark = input("\nSeleccione una opcion del menu:\n'1 - Imprimir nombres Heroes '\n'2 - Imprimir nombre y dato especifico'\n'3 - Imprimir alturas y sus nombres'\n'4 - Calcular Maximo o Minimo entre los heroes'\n'5 - Imprimir el promedio de alturas'\n'6 - Salir'\n\n>")

    imprimir_dato(menu_stark)



    

 