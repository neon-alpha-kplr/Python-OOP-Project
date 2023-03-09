import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#import generator
import json
import readline
#import utils
from re import sub, IGNORECASE
from treelib import Tree
from unidecode import unidecode
from inventory_manager.inventory_manager import InventoryManager
from class_generation.product_classes import *

# Define the prompt_for_instance function 
# that takes a class name as a string as input
def prompt_for_instance(cls):
    # Get the class object from the class name string
    # Get the names of the constructor arguments
    arg_names = cls.__init__.__code__.co_varnames[1:]
    # Prompt the user for the values of the arguments 
    print(cls.__name__,":")
    args = [input("Saisissez la valeur pour {}: ".format(name)) for name in arg_names]
    # Create an instance of the class using the entered values
    return cls(*args)

def rec_generate_tree_hierarchy(tree:Tree, json_dict:dict, parent_node_id=None):
    for class_name, class_attrs in json_dict.items():
        if isinstance(class_attrs, dict):
            if(class_name=="subclasses"):
                rec_generate_tree_hierarchy(tree, class_attrs, parent_node_id)
            else:
                class_name=sub("[^A-Z_]", "_", class_name, 0, IGNORECASE)
                if parent_node_id==None:
                    new_node_id = class_name.lower()
                else:
                    new_node_id = f"{parent_node_id}.{class_name.lower()}"
                tree.create_node(tag=class_name, identifier=new_node_id, parent=parent_node_id)
                rec_generate_tree_hierarchy(tree, class_attrs, new_node_id)
    return tree
                
def generate_tree_hierarchy(json_dict:dict):
    tree = Tree()
    tree = rec_generate_tree_hierarchy(tree, json_dict)
    return tree

# on cree une classe Tree qui herite de treelib.Tree
# et rajoute deux fonctionnalités supplémentaires
# get_penultimate_nodes -> recupère les avant derniers noeuds
# get_children_nodes -> recupère les noeud terminaux
class TreeExt(Tree):
    def __init__(self):
        super().__init__()
    
    def get_penultimate_nodes(self):
        penultimate_nodes = set()
        for node in self.all_nodes():
            if not self.children(node.identifier):
                parent_node = self.parent(node.identifier)
                if parent_node is not None and not self.children(node.identifier):
                    penultimate_nodes.add(parent_node.identifier)
        return penultimate_nodes
    
    # Define a function to get the immediate children nodes of a specified node
    def get_children_nodes(self, node_name):
        children_nodes = []
        node = self.get_node(node_name)
        if node is not None:
            children = self.children(node.identifier)
            children_nodes = [child.identifier for child in children]
        return children_nodes

def sep():
    print("====================")

def main():
    inventory_manager = InventoryManager()
    # write code to read json file as dict
        #
        #    

    readline.set_completer_delims(' \t\n')
    readline.parse_and_bind("tab: complete")

    # Define a function to handle user input
    def auto_complete(text, ac_list):
        matching_entry = [entry for entry in ac_list if entry.startswith(text)]
        if len(matching_entry) == 1:
            entry_name = matching_entry[0]
            remaining_text = entry_name[len(text):]
            if remaining_text:          
                readline.insert_text(remaining_text)
                readline.redisplay()
                
    def set_autocomplete(ac_list):
        readline.set_completer(lambda text, state: auto_complete(text, ac_list))

    while True:
        print("""
			Que souhaitez-vous faire ? :
			A. Ajouter un nouveau produit au stock
			R. Réapprovisionner un produit
			V. Vendre un produit
			S. Supprimer un produit du stock
			L. Afficher les produits en stock
			B. Afficher le solde du compte
			Q. Quitter
		""")

        choice = input("Saisissez votre choix : ")
        choice = choice.upper()
        
        if choice == "A":
            #print_list
            # write code to get class tree hierachy
            local_path = os.path.dirname(os.path.abspath(__file__))
            json_data = json.load(open(os.path.join(local_path, '../class_generation/json_data.json'), "rb"))
            json_str = json.dumps(json_data)
            json_data = (unidecode(json_str))
            json_dict = json.loads(json_data)
            # convert the tree object to TreeExt to get the new functionalities 
            # described above in TreeExt class
            # class_tree = TreeExt(generate_tree_hierarchy(json_dict))
            class_tree = TreeExt(generate_tree_hierarchy(json_dict))
            
            # ecrire le code pour récupérer les avant dernier noeuds de classe
            # (dernier niveau de catégories de produits)
            product_classes = class_tree.get_penultimate_nodes()
            sep()
            # write code to print list of product_classes
            print(p for p in product_classes)
            set_autocomplete(product_classes)
            category = input("Saisissez la catégorie de produit : ")
            
            # Get the immediate children nodes of node 'B'
            children_nodes = class_tree.get_children_nodes(category)
            # write code to print list of children_nodes
            print(c for c in children_nodes)
            set_autocomplete(children_nodes)
            product_name = input("Saisissez le type de produit : ")   
            #print(f"{name} has been added to stock with a quantity of {quantity}.")

            # write code to create a instance of classe product_name
            product_entry = prompt_for_instance(globals()[product_name])
            quantity = int(input("Saisissez la quantité : "))
            
            # write code to add product_entry and quantity in Inventory Manager
            inventory_manager.add_product(product_entry, quantity)

        elif choice == "R":
            name = input("Saisissez le nom du produit : ")
            quantity = int(input("Saisissez la quantité à réapprovisionner : "))
            # write code to get product by name
            product=inventory_manager.get_product(name)
            # write code to restock product
            inventory_manager.restock_product(product,quantity)

        elif choice == "V":
            name = input("Saisissez le nom du produit : ")
            quantity = int(input("Saisissez la quantité à vendre : "))
            # write code to get product by name
            product=inventory_manager.get_product(name)
            # write code to sell product
            inventory_manager.sell_product(product,quantity)

        elif choice == "S":
            name = input("Saisissez le nom du produit : ")
            # write code to get product
            product=inventory_manager.get_product(name)
            if product:
                # write code to remove product
                if inventory_manager.remove_product(product):
                    print(f"Le produit {name} a bien été supprimé du stock.")
            else:
                print(f"Le produit {name} ne fait pas partie du stock.")

        elif choice == "L":
            inventory_manager.list_products()

        elif choice == "B":
            # write code to print current balance
            print(f"Le solde du compte entrepôt est de {inventory_manager.profit_tracker.balance}€.")
            print(f"Les dépenses totales depuis le début de la session ont été de {inventory_manager.profit_tracker.total_cost}€.")
            
        elif choice == "Q":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")


if __name__ == '__main__':
    main()
