'''
Ordenamiento

lista = [14,5,20,10,23,15,7,16,29,21,-102,99,0]



'''

lista = [14,5,20,10,23,15,7,16,29,21,-102,99,0]

def orden_lista(lista:list)->list:
    lista_copia = lista.copy()
    nueva_lista = []
    for i in range(len(lista_copia) - 1):
        pivot = lista_copia[0]
        if(pivot > lista_copia[i + 1]):
            nueva_lista.insert(len(nueva_lista) + 1, lista_copia[i + 1])
    
    return nueva_lista

print(orden_lista(lista))