
'''
otra forma de llamar al archivo
with open(path, 'r') as file
    codigo
    codigo
    codigo

cuando salgo del with se cierra solo

'''
import json

#funcion para cargar el json
def cargar_json(path:str)->list:
    file = open(path, "r")
    buffer_dict = json.load(file)
    file.close()
#    with open(path, "r") as file
#      buffer_dict = json.load(file)

    return buffer_dict[]



#funcion para mostrar
#buscar la doc del format para dejarlo con mas estetica
def mostrar(lista:list):
    for elemento in lista:
        print("{0}-{1}-{2}".format(elemento['views'], elemento['length'], elemento['title'] ))