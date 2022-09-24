from curses.ascii import isalpha
from xml.etree.ElementTree import tostring
from data_stark import lista_personajes

def extraer_iniciales(nombre_heroe:str):
    '''
    recibe nombre_heroe que es un string.

    retorna un nuevo string con las iniciales del nombre y un punto.
    '''
    if(nombre_heroe == ""):
        return "N/A"
    else:
        if(nombre_heroe.count('the') > 0):
            nombre_heroe = nombre_heroe.replace('the', '')
        if(nombre_heroe.count('-') > 0):
            nombre_heroe = nombre_heroe.replace('-', '')
        lista_nombres = nombre_heroe.split(' ')
        nueva_lista = []
        for nombre in lista_nombres:
            nombre = nombre.strip()
            nombre = nombre[0:1]
            nombre = nombre.upper()
            if(nombre != ''):
                nueva_lista.append(nombre)                

        iniciales = '.'
        iniciales = iniciales.join(nueva_lista)
        iniciales = iniciales + "." 

        return iniciales

""" for heroe in lista_personajes:
    extraer_iniciales(heroe['nombre']) """

def definir_iniciales_nombre(heroe:dict):
    '''
    Recibe 'heroe' como parametro que es un diccionario.

    Modifica el mismo diccionario con un clave nueva agregada llamada 'iniciales' 
    y retorna True si salio todo bien
    '''
    if(type(heroe) != dict or heroe.get('nombre', "no existe") == "no existe"):
        return False
    else:
        heroe['iniciales'] = extraer_iniciales(heroe['nombre'])
        return True

""" for heroe in lista_personajes:
    print(definir_iniciales_nombre(heroe)) """

def agregar_iniciales_nombre(lista_heroes:list):
    '''
    recibe 'lista_heroes' como parametro que es una lista de diccionarios

    Modifica el mismo diccionario con un clave nueva agregada llamada 'iniciales' 
    y retorna True si salio todo bien
    ''' 
    if(type(lista_heroes) != list or len(lista_heroes) == 0):
        print("Error en los tipos de datos - funcion 1.3")
        return False 
    else:
        for i in range(len(lista_heroes)):
            if(not definir_iniciales_nombre(lista_heroes[i])):
                print('El origen de datos no contiene el formato correcto')
                return False
            else:
                retorno = definir_iniciales_nombre(lista_heroes[i])
        return retorno
            

def stark_imprimir_nombres_con_iniciales(lista_heroes:list[dict]):
    '''
    recibe 'lista_heroes' como parametro que es una lista de diccionarios

    Imprime el nombre de cada heroe con este formato
    * Howard the Duck (H.D.)    
    '''
    if(len(lista_heroes) == 0):
        print("Error en los tipos de datos")
    else:
        agregar_iniciales_nombre(lista_heroes)
        for heroe in lista_heroes:
            print('* {0} ({1})'.format(heroe['nombre'], heroe['iniciales']))


""" for heroe in lista_personajes:
    print(definir_iniciales_nombre(heroe)) """

""" stark_imprimir_nombres_con_iniciales(lista_personajes) """

def generar_codigo_heroe(id_heroe:int,genero_heroe:str)->str:
    '''
    Recibe 'id_heroe' como parametro que es un entero y un string
    'genero_heroe' que recibe 'F' 'M' o 'NB'

    Retorna un string con el siguiente formato 'GENERO-000…000ID'
    '''
    if(type(id_heroe) != int or (genero_heroe != "F" and genero_heroe != "M" and 
                                                            genero_heroe != "NB")):
        return "N/A"
    else:
        id_heroe = str(id_heroe)
        codigo_gen = genero_heroe + "-"
        codigo_final = codigo_gen + id_heroe.zfill(10 - len(codigo_gen))
        return codigo_final

def agregar_codigo_heroe(heroe:dict, id_heroe:int)->bool:
    '''
    Recibe 'heroe' como parametro. Es un Diccionario con datos de heroes
            'id_heroe' Es un entero que representa el codigo del heroe

    Retorna True y al mismo tiempo modifica el diccionario recibido y agrega una key
        llamada 'codigo_heroe' 
    '''
    if(bool(heroe) == False):
        return False
    else:
        heroe['codigo_heroe'] = generar_codigo_heroe(id_heroe, heroe['genero'])
        return True

def stark_generar_codigos_heroes(lista_heroes:list):
    '''
    Recibe una lista de heroes que contiene diccionarios. Uno por cada heroe

    Imprime una lista con el siguiente formato.
    Se asignaron ## códigos 

*   El código del primer héroe es: 		M-00000001
    '''
    contador_codigos = 0
    generador_id = 1
    for heroe in lista_heroes:
        agregar_codigo_heroe(heroe, generador_id)
        if(generador_id == 1):
            primer_codigo = heroe['codigo_heroe']
        ultimo_codigo = heroe['codigo_heroe']
        contador_codigos += 1
        generador_id += 1

    print("Se asignaron {0} códigos\n* El código del primer héroe es: {1}\n* El código del ultimo héroe es: {2}".format(contador_codigos,
    primer_codigo, ultimo_codigo))

""" stark_generar_codigos_heroes(lista_personajes) """

def sanitizar_entero(numero_str:str):
    '''
    
    '''
  


