from data_stark import lista_personajes

""" {'nombre': 'Howard the Duck', 
'identidad': 'Howard (Last name unrevealed)', 
'empresa': 'Marvel Comics', 
'altura': '79.349999999999994', 
'peso': '18.449999999999999', 
'genero': 'M', 
'color_ojos': 'Brown', 
'color_pelo': 'Yellow', 
'fuerza': '2', 
'inteligencia': ''} """

#punto A
""" for personaje in lista_personajes:
    if(personaje['genero'] == "M"):
        print(personaje['nombre']) """

#punto B
""" for personaje in lista_personajes:
    if(personaje['genero'] == "F"):
        print(personaje['nombre']) """

#punto C
""" flag = 0
personaje_alto_masc = ""
for personaje in lista_personajes:
    if(personaje['genero'] == "M"):
        altura_personaje = float(personaje['altura'])
        if(flag == 0 or altura_personaje > max_alto_masc):
            max_alto_masc = altura_personaje
            personaje_alto_masc = personaje['nombre']
            flag = 1
            
print("El personaje mas alto del genero M es: {0} Y su altura es: {1}".format(personaje_alto_masc, 
                                                                                max_alto_masc)) """

#punto D
""" flag = 0
personaje_alto_fem = ""
for personaje in lista_personajes:
    if(personaje['genero'] == "F"):
        altura_personaje = float(personaje['altura'])
        if(flag == 0 or altura_personaje > max_alto_fem):
            max_alto_fem = altura_personaje
            personaje_alto_fem = personaje['nombre']
            flag = 1
            
print("El personaje mas alto del genero F es: {0} Y su altura es: {1}".format(personaje_alto_fem, 
                                                                                max_alto_fem)) """

#punto F
""" flag = 0
personaje_bajo_fem = ""
for personaje in lista_personajes:
    if(personaje['genero'] == "F"):
        altura_personaje = float(personaje['altura'])
        if(flag == 0 or altura_personaje < min_bajo_fem):
            min_bajo_fem = altura_personaje
            personaje_bajo_fem = personaje['nombre']
            flag = 1
            
print("El personaje mas bajo del genero F es: {0} Y su altura es: {1}".format(personaje_bajo_fem, 
                                                                                min_bajo_fem)) """

#punto E

""" def primer_personaje_masc():
    personaje_masc = {}
    for personaje in lista_personajes:
        if(personaje['genero'] == "M"):
            personaje_masc = personaje
            break
    return personaje_masc

nombre_personaje_bajo_masc = ""
personaje_bajo_masc = primer_personaje_masc()
altura_baja = float(personaje_bajo_masc['altura'])
for personaje in lista_personajes:
    if(personaje['genero'] == 'M'):        
        altura = float(personaje['altura'])
        if(altura < altura_baja):
            altura_baja = altura
            nombre_personaje_bajo_masc = personaje['nombre']
        else:
            nombre_personaje_bajo_masc = personaje_bajo_masc['nombre']

print("El personaje mas bajo del genero M es: {0} y su altura es: {1}".format(nombre_personaje_bajo_masc, altura_baja)) """

#punto G
""" 
acumulador_alturas = 0
contador_personajes_masc = 0

for personaje in lista_personajes:
    if(personaje['genero'] == 'M'):        
        acumulador_alturas += float(personaje['altura'])
        contador_personajes_masc += 1

promedio_alturas_masc = acumulador_alturas/contador_personajes_masc

print("El promedio de alturas del genero M es: {0}".format(promedio_alturas_masc)) """

#punto H
""" acumulador_alturas = 0
contador_personajes_fem = 0

for personaje in lista_personajes:
    if(personaje['genero'] == 'F'):        
        acumulador_alturas += float(personaje['altura'])
        contador_personajes_fem += 1

promedio_alturas_masc = acumulador_alturas/contador_personajes_fem

print("El promedio de alturas del genero F es: {0}".format(promedio_alturas_masc)) """

#punto J
#lista unica (con set) de colores posibles
""" lista_color_ojos = []
for personaje in lista_personajes:
    lista_color_ojos.append(personaje['color_ojos'])
    set_color_ojos = set(lista_color_ojos)

#recorro cada color, hago su contador, lo guardo y luego muestro el resultado
lista_completa_ojos = []
dict_color_contador = {}
for color in set_color_ojos:
    contador_color = 0
    for personaje in lista_personajes:
        if(color == personaje['color_ojos']):
            contador_color += 1   
    dict_color_contador = {'Color' : color, 'Total' : contador_color}
    lista_completa_ojos.append(dict_color_contador)

for item in lista_completa_ojos:
    print(item) """

#punto K
#lista unica (con set) de colores posibles
""" lista_color_pelo = []
for personaje in lista_personajes:
    lista_color_pelo.append(personaje['color_pelo'])
    set_color_pelo = set(lista_color_pelo)

#recorro cada color, hago su contador, lo guardo y luego muestro el resultado
lista_completa_pelos = []
dict_color_contador = {}
for color in set_color_pelo:
    contador_color = 0
    for personaje in lista_personajes:
        if(color == personaje['color_pelo']):
            contador_color += 1   
    dict_color_contador = {'Color' : color, 'Total' : contador_color}
    lista_completa_pelos.append(dict_color_contador) """

#punto L
""" lista_inteligencia = []
for personaje in lista_personajes:
    lista_inteligencia.append(personaje['inteligencia'])
    set_color_int = set(lista_inteligencia)

#recorro cada color, hago su contador, lo guardo y luego muestro el resultado
lista_completa_inteligencia = []
dict_inteligencia_contador = {}
for int in set_color_int:
    contador_int = 0
    for personaje in lista_personajes:
        if(int == personaje['inteligencia']):
            contador_int += 1   
    if(int == ""):
        int = "No Tiene"
    else:
        int = int
    dict_inteligencia_contador = {'Inteligencia' : int, 'Total' : contador_int}
    lista_completa_inteligencia.append(dict_inteligencia_contador)

for item in lista_completa_inteligencia:
    print(item) """

#punto M
""" lista_color_ojos = []
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
    print(item) """

#punto N

""" lista_color_pelo = []
for personaje in lista_personajes:
    lista_color_pelo.append(personaje['color_pelo'])
    set_color_pelo = set(lista_color_pelo)

lista_completa_pelos = []
dict_color_contador = {}
for color in set_color_pelo:
    lista_heroes_pelo = []
    for personaje in lista_personajes:
        if(color == personaje['color_pelo']):
            lista_heroes_pelo.append(personaje['nombre']) 
    dict_color_contador = {'Color' : color, 'Heroes' : lista_heroes_pelo}
    lista_completa_pelos.append(dict_color_contador)

for item in lista_completa_pelos:
    print(item) """

#punto O
lista_inteligencia = []
for personaje in lista_personajes:
    lista_inteligencia.append(personaje['inteligencia'])
    set_color_int = set(lista_inteligencia)

lista_completa_inteligencia = []
dict_inteligencia_contador = {}
for int in set_color_int:
    lista_heroes_int = []
    for personaje in lista_personajes:
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

