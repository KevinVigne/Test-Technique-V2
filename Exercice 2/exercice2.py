
#Stockage des catégories et des plats
menu = {
    "entrées":[
        {"nom": "Salade César" ,"prix": 8 , "disponible": True },
        {"nom": "Soupe du jour" ,"prix": 6 , "disponible": False },
    ],
    "plats":[
        {"nom": "Steak frites" ,"prix": 15 , "disponible": True },
        {"nom": "Cabillaud" ,"prix": 15 , "disponible": False },
        {"nom": "Poisso grillé" ,"prix": 14 , "disponible": True },
        {"nom": "Plat du che" ,"prix": 18 , "disponible": False },
    ],
    "desserts":[
        {"nom": "Tiramisu" ,"prix": 7 , "disponible": True },
        {"nom": "Glace" ,"prix": 5 , "disponible": True },
        {"nom": "Dessert mystère","prix": 9 , "disponible": False },
    ],
    "boissons":[
        {"nom": "Café Latte", "prix": 5, "disponible" : True},
        {"nom": "Coca Cola", "prix": 3, "disponible" : True},
    ]
}

#Fonction d'affichage du menu
def affichage_menu():
    #Pour chaque catégorie
    for categorie , plats in menu.items():
        print("--- "+ categorie +" ---")
        #Pou chaque plat
        for plat in plats:
            if (plat["disponible"] == True):
                print(plat["nom"].lower() + " - " + str(plat["prix"]) + "€")


affichage_menu()