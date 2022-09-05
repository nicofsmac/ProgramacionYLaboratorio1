habilidades = [{"Nombre": "Vision-X",
                "Poder": 64},
                {"Nombre": "Vuelo",
                "Poder": 32},
                {"Nombre": "Inteligencia",
                "Poder": 256},
                {"Nombre": "Metamorfosis",
                "Poder": 1024},
                {"Nombre": "Super Velocidad",
                "Poder": 128},
                {"Nombre": "Magia",
                "Poder": 512}]

lista_completa = []
for habilidad in habilidades:
    lista_nuevo_formato = [habilidad['Nombre'],habilidad['Poder']]
    lista_completa.append(tuple(lista_nuevo_formato))

print(lista_completa)