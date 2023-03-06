"""
Nous allons a présent charger de nouvelles données.
Prenez le temps de lire ATTENTIVEMENT le contenu du nouveau fichier json_data
En utilisant le code précédemment réalisé, générez un arbre qui en affiche le contenu
Attention : N'afficher que les Noeuds possédant des sous-classes
Autrement dit, il ne faut pas inclure les attributs des Produits, mais seulement les catégories de produit.
Pour ce faire, il ne faut inclure que les noeuds qui ne sont pas terminaux
Les noeuds sans enfants doivent être skippés.

Voici le Pseudo code pour vous aider à rédiger le code.
"""
# Import des modules nécessaires
import json
import os
from unidecode import unidecode
from treelib import Tree

# Fonction pour charger les données JSON depuis un fichier et les convertir en dictionnaire Python
def json_dict_from_file():
    """
    Cette fonction ouvre et charge les données JSON du fichier
    dans un dictionnaire Python.

    Returns:
        dict: le dictionnaire Python contenant les données JSON du fichier
    """
    # Get the directory path of the current Python file
    local_path = os.path.dirname(os.path.abspath(__file__))
    # Chargement des données JSON à partir du fichier dans un dictionnaire python
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
    
    # Il est nécessaire de reconvertir le dictionnaire en chaine de caractere pour le traiter ensuite
    json_str = json.dumps(json_data)

    # Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
    json_data = (unidecode(json_str))

    # Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
    # Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
    json_dict = json.loads(json_data)

    return json_dict

# Fonction pour créer un arbre à partir d'un dictionnaire Python
def create_tree_from_dict(json_dict):
    tree = Tree()
    tree.create_node(tag="Product Classes Hierarchy", identifier="root")
    print(type(json_dict))
    tree = recursive_tree_from_json(tree, 'root', json_dict)
    return tree

# Fonction récursive pour parcourir un dictionnaire Python et créer des noeuds dans un arbre
def recursive_tree_from_json(tree, parent_node_id, json_dict):
    for key, value in json_dict.items():
        if isinstance(value, dict):
            if(key=="subclasses"):
                # Créer récursivement le sous-arbre pour le dictionnaire courant sans créer de noeud intermédiaire "subclasses"
                recursive_tree_from_json(tree, parent_node_id, value)
            else:
                # Créer un nouveau noeud pour la clé courante du dictionnaire
                new_node_id = f"{parent_node_id}.{key}"
                tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
                # Créer récursivement le sous-arbre pour le dictionnaire courant
                recursive_tree_from_json(tree, new_node_id, value)
    return tree
#    Pour chaque clé (class_name) et valeur (class_attrs) dans le dictionnaire :
#        Créer un nouveau noeud pour la clé courante du dictionnaire (nom de la classe)
#        Ajouter le nouveau noeud en tant que fils du noeud parent
#        Si "subclasses" est dans les attributs de la classe en cours (soit : valeur(class_attrs))
#            Appeler récursivement la fonction pour créer les sous-noeuds de ce dictionnaire

# Fonction principale
def main():
    j_dict = json_dict_from_file()
    tree = create_tree_from_dict(j_dict)
    tree.show()

# Code principal
if __name__ == '__main__':
    main()

"""
Output:
Product Classes Hierarchy
└── Product
    └── Biens Consommation
        ├── Articles Menagers
        │   ├── Appareils Electromenagers
        │   │   ├── Lave-linge
        │   │   ├── Lave-vaisselle
        │   │   └── Refrigerateur
        │   ├── Meubles
        │   │   ├── Canape
        │   │   ├── Chaise
        │   │   └── Table
        │   └── Ustensiles Cuisine
        │       ├── Batterie Cuisine
        │       └── Casserole
        └── Habillement
            ├── Casquette
            ├── Chaussures
            └── Vetements
                ├── Haut
                ├── Pantalon
                └── Robe
"""
