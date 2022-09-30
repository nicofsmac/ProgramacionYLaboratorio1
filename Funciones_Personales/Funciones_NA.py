#Validar una lista

def is_lista_ok(lista:list)->bool:
    '''
    recibe una lista y valida si el tipo, el largo

    retorna True si es correcto
    '''
    retorno = False

    if(len(lista) > 0 and type(lista) == list):
        retorno = True

    return retorno

def is_int_ok(valor:int)->bool:
    '''
    
    '''
    retorno = False
    return retorno
