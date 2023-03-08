# Import des modules nécessaires
import json
import os
from class_generation import generate_class_def
from re import sub
from re import IGNORECASE
from unidecode import unidecode

# Charger des données JSON à partir du fichier dans un dictionnaire python
local_path = os.path.dirname(os.path.abspath(__file__))
json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))

# Reconvertir le dictionnaire en chaine de caractere pour le traiter ensuite
json_str = json.dumps(json_data)

# Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
json_data = (unidecode(json_str))

# Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
# Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
json_dict = json.loads(json_data)

"""
La méthode generate_class_hierarchy permet de générer une hiérarchie des classes en utilisant un dictionnaire comme entrée.
Elle prend les arguments suivant: 
    - json_dict : un dictionnaire Python représentant une hiérarchie des classes.
    - superclass_name : une chaîne de caractères représentant le nom de la classe parente. Par défaut, sa valeur est None pour la racine de la hiérarchie.
    - superclass_args : une liste des arguments des arguments de la classe mère à passer à la classe fille.
"""
def generate_class_hierarchy(json_dict :dict, superclass_name:str=None, superclass_args:list=[]):
    # Initialisation de la chaîne de caractères contenant les définitions de classes
    class_defs = ""
    # Itération sur les éléments du dictionnaire pour chaque nom de classe (class_name) et attribut de cette dernière (class_attrs) dans les éléments de  json_dict
    for class_name, class_attrs in json_dict.items():
        class_name=sub("[^A-Z_]", "_", class_name, 0, IGNORECASE)
        # Générer la définition de la classe avec la méthode generate_class_def() en passant les arguments superclass_name et
        # superclass_args comme entrées. Le résultat de la méthode generate_class_def() est stocké dans une variable 'class_def'
        class_def=generate_class_def(class_name, class_attrs, superclass_name, superclass_args)
        # Concaténer la définition de la classe à la chaîne de caractères class_defs
        class_defs+=class_def
        
        # Ensuite, vérifier la présence des sous-classes dans la classe courante
        # Si "subclasses" existe parmi les attributs de la classe courante
        if isinstance(class_attrs, dict):
            if 'subclasses' in class_attrs.keys():
                #print('subclasses found : ' + class_def)
                # Construire une liste "super_attr" contenant les attributs de la classe courante concaténées aux arguments de la superclasse
                """super_attr=superclass_args[:]
                for attr in class_attrs.keys():
                    super_attr.append(attr)"""
                super_attr = (list(class_attrs.keys())+superclass_args)
                # Puis, supprimer l'attribut 'subclasses' à partir de la liste créée
                super_attr.remove('subclasses')
                # Ensuite, faire une récursion pour générer la définition de la sous-classe en utilisant la méthode generate_class_hierarchy
                # en passant le nom de la classe courante en tant que superclass_name et la liste super_attr en tant que superclass_args
                # Concaténer la définition de la sous-classe à la chaîne de caractères class_defs
                class_defs+=generate_class_hierarchy(class_attrs['subclasses'], class_name, super_attr)
    
    # Retourne la chaîne de caractères contenant les définitions de classes
    return class_defs

def write_content(content, filename):
    """
    La méthode write_content va nous permet d'écrire le code généré automatiquement des classes dans un fichier Python séparé
    La méthode write_content prend deux arguments:
    -content: une chaîne de caractères qui représente le contenu que l'on veut écrire dans le fichier.
    -filename: une chaîne de caractères qui représente le nom du fichier dans lequel on veut écrire le contenu.
    La méthode utilise une clause with pour ouvrir le fichier en mode écriture ("w") en utilisant l'encodage "utf-8".
    Ensuite, elle écrit le contenu passé en argument dans le fichier à l'aide de la méthode write. 
    Après avoir terminé d'écrire dans le fichier, la méthode se termine et le fichier est automatiquement fermé grâce à l'utilisation de la clause with.
    """
    with open(filename, "w", encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    # Appeler la méthode generate_class_hierarchy pour générer le code des classes automatiquement en se basant sur le dictionnaire json_dict
    # Stocker le résultat de la classe dans une variable
    classes=generate_class_hierarchy(json_dict)

    # Appeler la fonction write_content pour stocker le code des classes dans un fichier Python 'product_classes.py'
    local_path = os.path.dirname(os.path.abspath(__file__))
    write_content(classes,os.path.join(local_path, 'product_classes.py'))