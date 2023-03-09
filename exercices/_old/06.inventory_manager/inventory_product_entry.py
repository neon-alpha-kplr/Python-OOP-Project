from product_classes import Product, Biens_Consommation, Articles_Menagers, Meubles, Canape, Chaise, Table, Appareils_Electromenagers, Refrigerateur, Lave_vaisselle, Lave_linge, Ustensiles_Cuisine, Casserole, Batterie_Cuisine, Habillement, Vetements, Haut, Pantalon, Robe, Casquette, Chaussures

# Vous allez créer une classe InventoryProductEntry qui a pour role 
# de représenter une entrée d'inventaire pour un produit spécifique.
class InventoryProductEntry:
    # Initialisation de la classe, en prenant en argument un objet Product et une quantité initiale
    def __init__(self, product:Product, quantity):
        """
        'product' : un objet de type produit qui rassemble les différents attributs et caractéristiques de ce dernier
        'quantity' : un entier qui représente le nombre des pièces du produit en question
        """
        self.product=product
        self.quantity=quantity
        # Initialisation des variables
        """
        Vous devez initialiser deux variables. 
        la variable 'sales' qui stocke le total des revenues des ventes du produit
        la variable 'expenses' qui stocke le total des dépenses pour restocker le produit
        """
        self.sales=0
        self.expenses=0

    """
    La méthode sell est utilisée pour retirer la quantité vendue du produit depuis le stock.
    Elle met également à jour les ventes totales pour le produit.
    """
    def sell(self, quantity, ghost_mode:bool=False):
        #Avant de mettre à jour l'état du stock du produit, on doit vérifier si on a déjà une quantité suffisante à vendre.
        # SI la quantité en stock est inférieure à la quantité demandée:
        # Afficher "Le stock du produit [nom du produit] est insuffisant."
        # Retourner Faux
        if self.quantity<quantity:
            print(f"Le stock du produit {self.product.name} est insuffisant.")
            return False
        # SINON:
        else:
            # Si on est en ghost_mode, on veut simplement savoir que le stock de produits est suffisant sans le mettre à jour
            if ghost_mode: return True
            # Réduire la quantité en stock par la quantité demandée
            # Ajouter le revenue total de la vente à la variable 'sales' en multipliant la quantité vendue par le prix du produit
            # Retourner Vrai
            self.quantity-=quantity
            self.sales+=self.product.price*quantity
            return True
    
    """
    La méthode restock est utilisée pour augmenter la quantité en stock lorsqu'un nouveau stock de produit est reçu. 
    Elle met également à jour les dépenses totales pour restocker ce produit.
    """
    def restock(self, quantity):
        # Ajouter la quantité reçue à la quantité en stock
        self.quantity+=quantity
        # Ajouter le coût total de la nouvelle quantité reçue à la variable 'expenses' en multipliant la quantité reçue par le coût du produit
        self.expenses+=self.product.cost*quantity
        return True

    """
    La méthode repr est utilisée pour fournir une représentation en chaîne de caractères de l'objet InventoryProductEntry, 
    qui contient des informations utiles telles que le nom du produit, la marque, la quantité en stock et le prix du produit.
    """
    def __repr__(self):
        # Retourner une chaîne de caractères formatée contenant le nom du produit, la marque, la quantité en stock et le prix du produit.
        return f"{self.product.name} ({self.product.marque}) : {self.product.price}€ ({self.quantity} en stock)"

if __name__ == '__main__':
    produit=Product(12,25,'Brandt')
    ipe=InventoryProductEntry(produit, 3)
    print(ipe.__repr__())
    ipe.restock(13)
    print(ipe.__repr__())
    ipe.sell(3)
    print(ipe.__repr__())
    ipe.sell(31)
    print(ipe.__repr__())
