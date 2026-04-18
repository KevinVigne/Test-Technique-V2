#Déclaration de la variable contenant la largeur maximale d'un bloc
MAX_WIDTH =  100

#Création de la Bibliothèque de phrase
library = {
    "first_line":{
        "box": 1,
        "text": "Le code propre facilite la maintenance",
        "show": True,
    },
    "second_line":{
        "box": 2,
        "text": "Tester souvent évite beaucoup d'erreurs",
        "show": True,
    },
    "third_line":{
        "box": 2,
        "text": "Cette phrase ne doit pas s'afficher",
        "show": False,
    },
    "fourth_line":{
        "box": 3,
        "text": "Cette phrase ne dois pas s'afficher",
        "show": True,
    },
    "fifth_line":{
        "box": 3,
        "text": "Un bon code doit rester simple et clair",
        "show": True,
    },
    "sixth_line":{
        "box": 3,
        "text": "La simplicité améliore la qualité du code",
        "show": True,
    },
    "seventh_line":{
        "box": 3,
        "text": "Refactoriser améliore la compréhension",
        "show": True,
    },
}

#Fonction de Création d'un bloc
def box_creation(library):
    #Initialisation d'un tableau
    boxes = {}
    #Boucle sur la librairie
    for entry in library.values():
        #N'affiche rien si show est faux
        if (entry["show"] == False):
            continue

        box_number = entry["box"]
        text = entry["text"].lower()
        # Si ce numéro de bloc n'existe pas encore dans 'boxes'
        if (box_number not in boxes):
            # on crée une liste vide pour l'accueillir
            boxes[box_number] = []
        boxes[box_number].append(text)

    #On trie le dictionnaire par numéro de bloc
    sorted_boxes = dict(sorted(boxes.items()))
    return sorted_boxes

def calculate_width(number,lines):
    width = len("bloc" + str(number))

    for line in lines:
        # Si cette ligne est plus longue que la largeur actuelle, on l'agrandit
        if len(line)> width:
            width = len(line)
        #Assurance que la largeur maximale ne sera pas dépassée
        if width > MAX_WIDTH - 4:
            width = MAX_WIDTH - 4
    return width        

#Affichage d'un seul bloc dans le terminal
def show_box(number,lines):
    # On calcule la largeur intérieure adaptée à ce bloc
    width = calculate_width(number , lines)
    # Le séparateur est une ligne de tirets (+4 pour prendre en compte les "| " de chaque coté).
    separator = "-" * (width + 4)
    # Ligne du haut
    print(separator)
    #Affichage du titre du bloc
    title = "bloc " + str(number)
    print("| " + title.ljust(width) + " |")
    # Affichage de chaque phrase du bloc, avec le même alignement
    for line in lines:
        print("| " + line.ljust(width) +" |")

    print(separator)

def show_all_boxes(library):
    # Récupération des blocs regroupés et triés
    boxes = box_creation(library)

    # Affichage du contenu pour chaque bloc
    for number, lines in boxes.items():
        show_box(number,lines)
        # Ligne vide entre chaque bloc pour aérer l'affichage
        print()

# Lancement de l'affichage en passant la bibliothèque 
show_all_boxes(library)