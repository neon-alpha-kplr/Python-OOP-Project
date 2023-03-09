from product_classes import Product, Biens_Consommation, Articles_Menagers, Meubles, Canape, Chaise, Table, Appareils_Electromenagers, Refrigerateur, Lave_vaisselle, Lave_linge, Ustensiles_Cuisine, Casserole, Batterie_Cuisine, Habillement, Vetements, Haut, Pantalon, Robe, Casquette, Chaussures
from inventory_product_entry import InventoryProductEntry

#La classe "InventoryManager" est une classe qui permet de gérer un inventaire de produits. 
class InventoryManager:
    # Initialisation de la classe
    def __init__(self):
        # Vous initialisez un dictionnaire 'inventory' qui stocke l'inventaire de tous les produits
        # Il prend comme clé le nom du produit, et la valeur est un objet InventoryProductEntry
        self.inventory : Dict[str, InventoryProductEntry] = {}
    
    """"
    La méthode product_exists prend un objet Product en entrée et vérifie si son nom est une clé dans le dictionnaire self.inventory. 
    Si c'est le cas, la fonction retourne True, sinon elle retourne False.
    """
    def product_exists(self, product_name):
        return product_name in self.inventory
    
    """
    La méthode add_product est utilisée pour ajouter un nouveau produit à l'inventaire.
    Elle prend en argument un objet Product et une quantité initiale.
    """
    def add_product(self, product:Product, quantity:int=0):
        # SI le produit existe déjà dans l'inventaire: 
        if self.product_exists(product.name):
            # Afficher un message pour informer l'utilisateur
            print("Le produit est déjà présent dans l'inventaire.")
            return False
        else:
            # Sinon:
            # Créer un nouvel objet InventoryProductEntry en utilisant le produit et la quantité fournis
            # Ajouter le nouvel objet au dictionnaire 'inventory'
            self.inventory[product.name]=InventoryProductEntry(product, quantity)
            return True
    
    """
    La méthode remove_product est utilisée pour supprimer un produit de l'inventaire.
    Elle prend en argument un nom de produit et supprime l'entrée correspondante dans le dictionnaire 'inventory'.
    """
    def remove_product(self, product_name):
        # Utiliser la méthode product_exists pour vérifier si le produit existe dans l'inventaire
        if self.product_exists(product_name):
            # Supprimer le produit de l'inventaire
            self.inventory.pop(product_name)
            return True
        else:
            #Sinon, afficher un message d'erreur indiquant que le produit n'a pas été trouvé
            print("Le produit n'existe pas dans l'inventaire")
            return False
    
    """
    La méthode sell_product est utilisée pour vendre une quantité donnée d'un produit.
    Elle prend en argument le nom du produit et la quantité à vendre.
    """
    def sell_product(self, product_name, quantity):
        # Utiliser une boucle pour parcourir les clés du dictionnaire 'inventory'
        for ipe in self.inventory:
            # Pour chaque itération, on vérifie si le nom du produit fourni est égal à la clé du dictionnaire.
            if product_name==ipe:
                # Si le produit est trouvé, appeler la méthode 'sell' de l'objet InventoryProductEntry correspondant avec la quantité à vendre
                self.inventory[ipe].sell(quantity)
                return True
        # Sinon, afficher un message d'erreur indiquant que la vente a échoué
        print("La vente a échoué")
        return False
    
    """
    La méthode restock_product est utilisée pour restocker une quantité donnée d'un produit.
    Elle prend en argument le nom du produit et la quantité à restocker.
    """
    def restock_product(self, product_name, quantity):
        # Vérifier si le produit existe déjà dans l'inventaire
        if self.product_exists(product_name):
            # Si le produit est trouvé, appeler la méthode 'restock' de l'objet InventoryProductEntry correspondant avec la quantité à restocker
            if self.inventory[product_name].restock(quantity):
                # Si le réapprovisionnement est réussi, afficher un message de confirmation
                print(f"Le stock de {product_name} a bien été réapprovisionné de {quantity} unités. Il est désormais de {self.inventory[product_name].quantity}")
            else:
                print("Une erreur s'est produite lors du réapprovisionnement (impossible de restocker le produit)")
        else:
            # Sinon, on appelle la méthode add_product pour ajouter le produit en stock avec une quantité nulle et on rappelle la fonction restock_product pour le restocker
            if self.add_product(product_name, 0):
                self.restock_product(product_name, quantity)
            else:
                print("Une erreur s'est produite lors de l'approvisionnement (impossible d'ajouter le produit à l'inventaire)")
    
    """
    La méthode get_product retourne toutes les informations liées au produit en faisant une recherche par son nom.
    Elle prend en entrée un nom de produit.
    """
    def get_product(self, product_name):
        # Pour chaque inventory_product_entry_key dans self.inventory
        for inventory_product_entry_key in self.inventory:
            # Si inventory_product_entry_key == nom de produit:
            if inventory_product_entry_key==product_name:
                # Retourner self.inventaire[inventory_product_entry_key].product
                return self.inventory[inventory_product_entry_key]
        # Afficher un message pour indiquer que le produit n'existe pas
        print("Le produit n'existe pas dans l'inventaire")

    """
    La méthode list_products(self) parcourt tous les produits de l'inventaire et affiche les informations relatives à chacun d'entre eux
    (nom, quantité disponible, prix unitaire, coût unitaire, prix de vente unitaire, bénéfice unitaire). 
    """
    def list_products(self, detailed_view:bool=False):
        # Ppour chaque clé du dictionnaire 'inventory'
        for ipe_key, inventory_product_entry in self.inventory.items():
            # Afficher la valeur correspondante à cette clé
            if detailed_view:
                product=inventory_product_entry.product
                print(f"{type(product).__name__} {product.name} {product.marque} {product.cost}€/{product.price}€ (marge de {product.price-product.cost}€ = {1-product.cost/product.price:.2%}) | Stock : {inventory_product_entry.quantity} | Ventes : {inventory_product_entry.sales}€ | Dépenses : {inventory_product_entry.expenses}€")
            else:
                print(ipe_key)
        # Retourner le dictionnaire inventaire
        return self.inventory
    
import json
import os
from unidecode import unidecode

def import_inventory_data_from_json(inventory_manager, filename):
    local_path = os.path.dirname(os.path.abspath(__file__))
    json_data = json.load(open(os.path.join(local_path, filename), "rb"))
    json_str = json.dumps(json_data)
    json_data = unidecode(json_str)
    json_dict = json.loads(json_data)
    
    product_classes_module=__import__('product_classes_adv')
    product_classes={}
    for product in json_dict.items():
        if not product[1]['type'] in product_classes:
            product_classes[product[1]['type']]=getattr(product_classes_module,product[1]['type'])
        args=list(product[1].values())
        product_instance=product_classes[product[1]['type']](product[0],args[1:-1])
        inventory_manager.add_product(product_instance,product[1]['quantity'])

if __name__ == '__main__':
    myIM=InventoryManager()
    import_inventory_data_from_json(myIM, "products.json")
    myIM.list_products(True)
    myIM.sell_product('c_t1238',621)
    print('-'*100)
    myIM.list_products(True)
