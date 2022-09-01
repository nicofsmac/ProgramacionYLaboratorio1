#Punto 1
mi_dic = {'nombre': 'Karen', 'apellido': 'Jurgens', 'edad': 35, 'ocupacion': 'Periodista'}

#Punto 2
mi_dic['edad'] = 36
mi_dic['ocupacion'] = 'Editora'
mi_dic['pais'] = 'Colombia'

#Punto 3
lista_multiple = [1,3,'Nueve','Test',3548]

lista_no_numeros = []

for elemento in lista_multiple:
    if(type(elemento) == int):
       print(elemento)
    else:
        lista_no_numeros.append(elemento)
    
print(lista_no_numeros)





