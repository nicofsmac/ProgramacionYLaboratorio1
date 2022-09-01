#punto 1
""" condicion = 'si'
lista_clientes = []

while(condicion == 'si'):
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    lista_clientes.append(nombre_cliente)
    condicion = input("Desea seguir ingresando clientes?: 'si' o 'no'")

print(lista_clientes) """

#punto 2

""" condicion = 'si'
lista_clientes = []
dic_data_clientes = {}

while(condicion == 'si'):
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cantidad_cervezas = input("Ingrese la cantidad de cervezas compradas: ")
    edad_cliente = input("Ingrese la edad del cliente: ")
    dic_data_clientes = {'nombre': nombre_cliente, 'cantidad_cervezas': int(cantidad_cervezas), 
                        'edad': int(edad_cliente)}
    lista_clientes.append(dic_data_clientes)
    condicion = input("Desea seguir ingresando clientes?: 'si' o 'no'")

for cliente in lista_clientes:
    if(cliente['edad'] > 30):
        print(cliente) """

#punto 3

condicion = 'si'
lista_clientes = []
dic_data_clientes = {}
lista_cervezas = [{'Ipa': {'codigo': 25007, 'ibu': 18, 'marca': "Patagonia"}, 
                    'Apa': {'codigo': 25540, 'ibu': 10, 'marca': "Quilmes"}}]

while(condicion == 'si'):
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cantidad_cervezas = input("Ingrese la cantidad de cervezas compradas: ")
    edad_cliente = input("Ingrese la edad del cliente: ")
    dic_data_clientes = {'nombre': nombre_cliente, 'cantidad_cervezas': int(cantidad_cervezas), 
                        'edad': int(edad_cliente)}
    lista_clientes.append(dic_data_clientes)
    condicion = input("Desea seguir ingresando clientes?: 'si' o 'no'")

for cliente in lista_clientes:
    if(cliente['edad'] > 30):
        print(cliente)