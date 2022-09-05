heroes_para_reclutar = ["Batman", "BatWoman", "BatGirl",
                        "Wonder Woman", "Aquaman", "Shazam",
                        "Superman", "Super Girl", "Power Girl"]
 
heroes_info = {"Super Girl": {"ID": 1,
                            "Origen": "Krypton",
                            "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
                            "Identidad": "Kara Zor-El"},
                "Shazam": {"ID": 25,
                            "Origen": "Tierra",
                            "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
                            "Identidad": "Billy Batson"},
                "Power Girl": {"ID": 14,
                            "Origen": "Krypton",
                            "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
                            "Identidad": "Karen Starr"},
                "Wonder Woman": {"ID": 29,
                                "Origen": "Amazonia",
                                "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
                                "Identidad": "Diana Prince"}}

lista_reclutados = []
dic_reclutados = {}

for heroe_i in heroes_info:
    for heroe_r in heroes_para_reclutar:
        if(heroe_r == heroe_i):
            dic_reclutados = {'ID': heroes_info[heroe_r]['ID'],
                               'Codename': heroe_r,
                               'Identidad': heroes_info[heroe_r]['Identidad'],
                               'Origen': heroes_info[heroe_r]['Origen'],
                               'Habilidades': set(heroes_info[heroe_r]['Habilidades'])}
            lista_reclutados.append(dic_reclutados)

for heroe_final in lista_reclutados:
    print("ID: {0}, Codename: {1}\nIdentidad: {2}, Origen: {3}\nHabilidades: {4}\n----------------------------------------\n\n".format(heroe_final['ID'],
                                                                                                                                        heroe_final['Codename'],
                                                                                                                                        heroe_final['Identidad'],
                                                                                                                                        heroe_final['Origen'],
                                                                                                                                        heroe_final['Habilidades']))


