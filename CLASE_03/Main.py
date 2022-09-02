#import data
from data_stark import lista_personajes

#punto A
#print(lista_personajes[0:2])
"""     {
    'nombre': 'Howard the Duck', 
    'identidad': 'Howard (Last name unrevealed)', 
    'empresa': 'Marvel Comics', 
    'altura': '79.349999999999994', 
    'peso': '18.449999999999999', 
    'genero': 'M', 'color_ojos': 
    'Brown', 'color_pelo': 'Yellow', 
    'fuerza': '2', 'inteligencia': ''
    } 
"""
#punto B
""" for personaje in lista_personajes:
    print(personaje['nombre']) """

#punto C
""" for personaje in lista_personajes:
    print(personaje['nombre'], personaje['altura']) """

#punto D
""" personaje_maximo_altura = lista_personajes[0]
for personaje in lista_personajes:
    if(float(personaje['altura']) > float(personaje_maximo_altura['altura'])):
        personaje_maximo_altura = personaje

print(personaje_maximo_altura['altura']) """

#punto E
""" personaje_minimo_altura = lista_personajes[0]
for personaje in lista_personajes:
    if(float(personaje['altura']) < float(personaje_minimo_altura['altura'])):
        personaje_minimo_altura = personaje

print(personaje_minimo_altura['altura']) """

#punto F
""" acumulador_alturas = 0
for personaje in lista_personajes:
    acumulador_alturas += float(personaje['altura'])

denominador_promedio_alturas = len(lista_personajes)
promedio_alturas = acumulador_alturas/denominador_promedio_alturas

print("El promedio de alturas es : {0}".format(promedio_alturas)) """

#punto G
""" personaje_maximo_altura = lista_personajes[0]
for personaje in lista_personajes:
    if(float(personaje['altura']) > float(personaje_maximo_altura['altura'])):
        personaje_maximo_altura = personaje

print(personaje_maximo_altura['altura'], personaje_maximo_altura['nombre'])

personaje_minimo_altura = lista_personajes[0]
for personaje in lista_personajes:
    if(float(personaje['altura']) < float(personaje_minimo_altura['altura'])):
        personaje_minimo_altura = personaje

print(personaje_minimo_altura['altura'], personaje_minimo_altura['nombre']) """

#punto H
""" personaje_maximo_peso = lista_personajes[0]
for personaje in lista_personajes:
    if(float(personaje['peso']) > float(personaje_maximo_peso['peso'])):
        personaje_maximo_peso = personaje

print(personaje_maximo_peso['peso'], personaje_maximo_peso['nombre'])

personaje_minimo_peso = lista_personajes[0]
for personaje in lista_personajes:
    if(float(personaje['peso']) < float(personaje_minimo_peso['peso'])):
        personaje_minimo_peso = personaje

print(personaje_minimo_peso['peso'], personaje_minimo_peso['nombre']) """

#punto I
def superheroe_mas_alto():
    personaje_maximo_altura = lista_personajes[0]
    for personaje in lista_personajes:
        if(float(personaje['altura']) > float(personaje_maximo_altura['altura'])):
            personaje_maximo_altura = personaje

    personaje_alto = personaje_maximo_altura['altura']
    nombre_personaje_alto = personaje_maximo_altura['nombre']

    print("El personaje mas alto es: {1} y mide {0} centimetros".format(personaje_alto, nombre_personaje_alto))

def superheroe_mas_bajo():
    personaje_minimo_altura = lista_personajes[0]
    for personaje in lista_personajes:
        if(float(personaje['altura']) < float(personaje_minimo_altura['altura'])):
            personaje_minimo_altura = personaje

    personaje_bajo = personaje_minimo_altura['altura']
    nombre_personaje_bajo = personaje_minimo_altura['nombre']

    print("El personaje mas bajo es: {1} y mide {0} centimetros".format(personaje_bajo, nombre_personaje_bajo))

def promedio_altura_superheroe():
    acumulador_alturas = 0
    for personaje in lista_personajes:
        acumulador_alturas += float(personaje['altura'])

    denominador_promedio_alturas = len(lista_personajes)
    promedio_alturas = acumulador_alturas/denominador_promedio_alturas

    print("El promedio de alturas es : {0}".format(promedio_alturas))

def superheroe_mas_pesado():
    personaje_maximo_peso = lista_personajes[0]
    for personaje in lista_personajes:
        if(float(personaje['peso']) > float(personaje_maximo_peso['peso'])):
            personaje_maximo_peso = personaje
    
    personaje_pesado = personaje_maximo_peso['peso']
    nombre_personaje_pesado = personaje_maximo_peso['nombre']

    print("El personaje mas pesado es: {1} y mide {0} centimetros".format(personaje_pesado, nombre_personaje_pesado))

def superheroe_mas_liviano():
    personaje_minimo_peso = lista_personajes[0]
    for personaje in lista_personajes:
        if(float(personaje['peso']) < float(personaje_minimo_peso['peso'])):
            personaje_minimo_peso = personaje
    
    personaje_liviano = personaje_minimo_peso['peso']
    nombre_personaje_liviano = personaje_minimo_peso['nombre']

    print("El personaje mas liviano es: {1} y mide {0} centimetros".format(personaje_liviano, nombre_personaje_liviano))

#punto j

while(True):
    respuesta = input("\nSeleccione una opcion del menu:\n'1 - Ver cual es el superheroe mas alto'\n'2 - Ver cual es el superheroe mas bajo'\n'3 - Ver cual es el promedio de alturas'\n'4 - Ver cual es el superheroe mas pesado'\n'5 - Ver cual es el superheroe mas liviano'\n'6 - Salir'\n\n>")
    if(respuesta == "1"):
        superheroe_mas_alto()
    elif(respuesta == "2"):
        superheroe_mas_bajo()
    elif(respuesta == "3"):
        promedio_altura_superheroe()
    elif(respuesta == "4"):
        superheroe_mas_pesado()
    elif(respuesta == "5"):
        superheroe_mas_liviano()
    elif(respuesta == "6"):
        break

