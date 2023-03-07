class Product:
	def __init__(self, cost, price, marque):
		self.cost = cost
		self.price = price
		self.marque = marque
		self.name=type(self).__name__

class Biens_Consommation(Product):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Articles_Menagers(Biens_Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Meubles(Articles_Menagers):
	def __init__(self, materiau, couleur, dimensions, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materiau = materiau
		self.couleur = couleur
		self.dimensions = dimensions

class Canape(Meubles):
	def __init__(self, cost, price, marque, materiau, couleur, dimensions):
		super().__init__(cost, price, marque, materiau, couleur, dimensions)

class Chaise(Meubles):
	def __init__(self, cost, price, marque, materiau, couleur, dimensions):
		super().__init__(cost, price, marque, materiau, couleur, dimensions)

class Table(Meubles):
	def __init__(self, cost, price, marque, materiau, couleur, dimensions):
		super().__init__(cost, price, marque, materiau, couleur, dimensions)

class Appareils_Electromenagers(Articles_Menagers):
	def __init__(self, capacite, cost, price, marque):
		super().__init__(cost, price, marque)
		self.capacite = capacite

class Refrigerateur(Appareils_Electromenagers):
	def __init__(self, efficacite, cost, price, marque, capacite):
		super().__init__(cost, price, marque, capacite)
		self.efficacite = efficacite

class Lave_vaisselle(Appareils_Electromenagers):
	def __init__(self, programme, cost, price, marque, capacite):
		super().__init__(cost, price, marque, capacite)
		self.programme = programme

class Lave_linge(Appareils_Electromenagers):
	def __init__(self, programme, cost, price, marque, capacite):
		super().__init__(cost, price, marque, capacite)
		self.programme = programme

class Ustensiles_Cuisine(Articles_Menagers):
	def __init__(self, materiaux, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materiaux = materiaux

class Casserole(Ustensiles_Cuisine):
	def __init__(self, diametre, cost, price, marque, materiaux):
		super().__init__(cost, price, marque, materiaux)
		self.diametre = diametre

class Batterie_Cuisine(Ustensiles_Cuisine):
	def __init__(self, nombre_pieces, cost, price, marque, materiaux):
		super().__init__(cost, price, marque, materiaux)
		self.nombre_pieces = nombre_pieces

class Habillement(Biens_Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Vetements(Habillement):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(cost, price, marque)
		self.taille = taille
		self.couleur = couleur
		self.matiere = matiere

class Haut(Vetements):
	def __init__(self, cost, price, marque, taille, couleur, matiere):
		super().__init__(cost, price, marque, taille, couleur, matiere)

class Pantalon(Vetements):
	def __init__(self, cost, price, marque, taille, couleur, matiere):
		super().__init__(cost, price, marque, taille, couleur, matiere)

class Robe(Vetements):
	def __init__(self, cost, price, marque, taille, couleur, matiere):
		super().__init__(cost, price, marque, taille, couleur, matiere)

class Casquette(Habillement):
	def __init__(self, couleur, cost, price, marque):
		super().__init__(cost, price, marque)
		self.couleur = couleur

class Chaussures(Habillement):
	def __init__(self, pointure, cost, price, marque):
		super().__init__(cost, price, marque)
		self.pointure = pointure

