from data_stark import lista_personajes

#punto A

def imprimir_nombre_personaje_m(lista:list):
    for personaje in lista:
        if(personaje['genero'] == "M"):
            print(personaje['nombre'])

#punto B
def imprimir_nombre_personaje_f(lista:list):
    for personaje in lista:
        if(personaje['genero'] == "F"):
            print(personaje['nombre'])

#punto C
def calcular_heroe_m_alto(lista:list):
    flag = 0
    personaje_alto_masc = ""
    for personaje in lista:
        if(personaje['genero'] == "M"):
            altura_personaje = float(personaje['altura'])
            if(flag == 0 or altura_personaje > max_alto_masc):
                max_alto_masc = altura_personaje
                personaje_alto_masc = personaje['nombre']
                flag = 1
                
    return personaje_alto_masc

#punto D
def calcular_heroe_f_alto(lista:list):
    flag = 0
    personaje_alto_fem = ""
    for personaje in lista:
        if(personaje['genero'] == "F"):
            altura_personaje = float(personaje['altura'])
            if(flag == 0 or altura_personaje > max_alto_fem):
                max_alto_fem = altura_personaje
                personaje_alto_fem = personaje['nombre']
                flag = 1
                
    return personaje_alto_fem

#punto F
def calcular_heroe_f_bajo(lista:list):
    flag = 0
    personaje_bajo_fem = ""
    for personaje in lista:
        if(personaje['genero'] == "F"):
            altura_personaje = float(personaje['altura'])
            if(flag == 0 or altura_personaje < min_bajo_fem):
                min_bajo_fem = altura_personaje
                personaje_bajo_fem = personaje['nombre']
                flag = 1
                
    return personaje_bajo_fem

#punto E

def primer_personaje_masc():
    personaje_masc = {}
    for personaje in lista_personajes:
        if(personaje['genero'] == "M"):
            personaje_masc = personaje
            break
    return personaje_masc

def calcular_heroe_m_bajo(lista:list):
    nombre_personaje_bajo_masc = ""
    personaje_bajo_masc = primer_personaje_masc()
    altura_baja = float(personaje_bajo_masc['altura'])
    for personaje in lista:
        if(personaje['genero'] == 'M'):        
            altura = float(personaje['altura'])
            if(altura < altura_baja):
                altura_baja = altura
                nombre_personaje_bajo_masc = personaje['nombre']
            else:
                nombre_personaje_bajo_masc = personaje_bajo_masc['nombre']

    return nombre_personaje_bajo_masc

#punto G
def calcular_promedio_heroe_m(lista:list):
    acumulador_alturas = 0
    contador_personajes_masc = 0

    for personaje in lista:
        if(personaje['genero'] == 'M'):        
            acumulador_alturas += float(personaje['altura'])
            contador_personajes_masc += 1

    promedio_alturas_masc = acumulador_alturas/contador_personajes_masc

    return promedio_alturas_masc

#punto H
def calcular_promedio_heroe_f(lista:list):
    acumulador_alturas = 0
    contador_personajes_fem = 0

    for personaje in lista:
        if(personaje['genero'] == 'F'):        
            acumulador_alturas += float(personaje['altura'])
            contador_personajes_fem += 1

    promedio_alturas_masc = acumulador_alturas/contador_personajes_fem

    return promedio_alturas_masc

#punto J
def imprimir_heroes_color_ojos(lista:list):
    #lista unica (con set) de colores posibles
    lista_color_ojos = []
    for personaje in lista:
        lista_color_ojos.append(personaje['color_ojos'])
        set_color_ojos = set(lista_color_ojos)

    #recorro cada color, hago su contador, lo guardo y luego muestro el resultado
    lista_completa_ojos = []
    dict_color_contador = {}
    for color in set_color_ojos:
        contador_color = 0
        for personaje in lista:
            if(color == personaje['color_ojos']):
                contador_color += 1   
        dict_color_contador = {'Color' : color, 'Total' : contador_color}
        lista_completa_ojos.append(dict_color_contador)

    for item in lista_completa_ojos:
        print(item)

#punto K
#lista unica (con set) de colores posibles
def imprimir_heroes_color_pelo(lista:list):
    lista_color_pelo = []
    for personaje in lista:
        lista_color_pelo.append(personaje['color_pelo'])
        set_color_pelo = set(lista_color_pelo)

    #recorro cada color, hago su contador, lo guardo y luego muestro el resultado
    lista_completa_pelos = []
    dict_color_contador = {}
    for color in set_color_pelo:
        contador_color = 0
        for personaje in lista:
            if(color == personaje['color_pelo']):
                contador_color += 1   
        dict_color_contador = {'Color' : color, 'Total' : contador_color}
        lista_completa_pelos.append(dict_color_contador)
    
    for item in lista_completa_pelos:
        print(item)

#punto L
def imprimir_heroes_inteligencia(lista:list):
    lista_inteligencia = []
    for personaje in lista:
        lista_inteligencia.append(personaje['inteligencia'])
        set_color_int = set(lista_inteligencia)

    #recorro cada color, hago su contador, lo guardo y luego muestro el resultado
    lista_completa_inteligencia = []
    dict_inteligencia_contador = {}
    for int in set_color_int:
        contador_int = 0
        for personaje in lista:
            if(int == personaje['inteligencia']):
                contador_int += 1   
        if(int == ""):
            int = "No Tiene"
        else:
            int = int
        dict_inteligencia_contador = {'Inteligencia' : int, 'Total' : contador_int}
        lista_completa_inteligencia.append(dict_inteligencia_contador)

    for item in lista_completa_inteligencia:
        print(item)

#punto M
def imprimir_lista_heroes_color_ojos(lista:list):
    lista_color_ojos = []
    for personaje in lista_personajes:
        lista_color_ojos.append(personaje['color_ojos'])
        set_color_ojos = set(lista_color_ojos)


    lista_completa_ojos = []
    dict_color_contador = {}
    for color in set_color_ojos:
        lista_heroes_ojos = []
        for personaje in lista_personajes:
            if(color == personaje['color_ojos']):
                lista_heroes_ojos.append(personaje['nombre'])
        dict_color_contador = {'Color' : color, 'Heroes' : lista_heroes_ojos}
        lista_completa_ojos.append(dict_color_contador)

    for item in lista_completa_ojos:
        print(item)

#punto N
def imprimir_lista_heroes_color_pelo(lista:list):
    lista_color_pelo = []
    for personaje in lista:
        lista_color_pelo.append(personaje['color_pelo'])
        set_color_pelo = set(lista_color_pelo)

    lista_completa_pelos = []
    dict_color_contador = {}
    for color in set_color_pelo:
        lista_heroes_pelo = []
        for personaje in lista:
            if(color == personaje['color_pelo']):
                lista_heroes_pelo.append(personaje['nombre']) 
        dict_color_contador = {'Color' : color, 'Heroes' : lista_heroes_pelo}
        lista_completa_pelos.append(dict_color_contador)

    for item in lista_completa_pelos:
        print(item)

#punto O
def imprimir_lista_heroes_inteligencia(lista:list):
    lista_inteligencia = []
    for personaje in lista:
        lista_inteligencia.append(personaje['inteligencia'])
        set_color_int = set(lista_inteligencia)

    lista_completa_inteligencia = []
    dict_inteligencia_contador = {}
    for int in set_color_int:
        lista_heroes_int = []
        for personaje in lista:
            if(int == personaje['inteligencia']):
                lista_heroes_int.append(personaje['nombre'])  
        if(int == ""):
            int = "No Tiene"
        else:
            int = int
        dict_inteligencia_contador = {'Inteligencia' : int, 'Heroes' : lista_heroes_int}
        lista_completa_inteligencia.append(dict_inteligencia_contador)

    for item in lista_completa_inteligencia:
        print(item)

# crear menu

def menu_desafio_uno(indice:str):
    
    menu_desafio = input("\nSeleccione una opcion del menu:\n'1 - Imprimir nombres Heroes '\n'2 - Imprimir nombre y dato especifico'\n'3 - Imprimir alturas y sus nombres'\n'4 - Calcular Maximo o Minimo entre los heroes'\n'5 - Imprimir el promedio de alturas'\n'6 - Salir'\n\n>")