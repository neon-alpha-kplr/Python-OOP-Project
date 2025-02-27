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
	def __init__(self, materiau, couleur, dimensions, cost, price, marque):
		super().__init__(materiau, couleur, dimensions, cost, price, marque)

class Chaise(Meubles):
	def __init__(self, materiau, couleur, dimensions, cost, price, marque):
		super().__init__(materiau, couleur, dimensions, cost, price, marque)

class Table(Meubles):
	def __init__(self, materiau, couleur, dimensions, cost, price, marque):
		super().__init__(materiau, couleur, dimensions, cost, price, marque)

class Appareils_Electromenagers(Articles_Menagers):
	def __init__(self, capacite, cost, price, marque):
		super().__init__(cost, price, marque)
		self.capacite = capacite

class Refrigerateur(Appareils_Electromenagers):
	def __init__(self, efficacite, capacite, cost, price, marque):
		super().__init__(capacite, cost, price, marque)
		self.efficacite = efficacite

class Lave_vaisselle(Appareils_Electromenagers):
	def __init__(self, programme, capacite, cost, price, marque):
		super().__init__(capacite, cost, price, marque)
		self.programme = programme

class Lave_linge(Appareils_Electromenagers):
	def __init__(self, programme, capacite, cost, price, marque):
		super().__init__(capacite, cost, price, marque)
		self.programme = programme

class Ustensiles_Cuisine(Articles_Menagers):
	def __init__(self, materiaux, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materiaux = materiaux

class Casserole(Ustensiles_Cuisine):
	def __init__(self, diametre, materiaux, cost, price, marque):
		super().__init__(materiaux, cost, price, marque)
		self.diametre = diametre

class Batterie_Cuisine(Ustensiles_Cuisine):
	def __init__(self, nombre_pieces, materiaux, cost, price, marque):
		super().__init__(materiaux, cost, price, marque)
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
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Pantalon(Vetements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Robe(Vetements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Casquette(Habillement):
	def __init__(self, couleur, cost, price, marque):
		super().__init__(cost, price, marque)
		self.couleur = couleur

class Chaussures(Habillement):
	def __init__(self, pointure, cost, price, marque):
		super().__init__(cost, price, marque)
		self.pointure = pointure
