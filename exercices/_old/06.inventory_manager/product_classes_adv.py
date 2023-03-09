class Product:
	def __init__(self, name, args:()):
		self.cost = args[0]
		self.price = args[1]
		self.marque = args[2]
		self.name=name

class Biens_Consommation(Product):
	def __init__(self, name, args:()):
		super().__init__(name, args)

class Articles_Menagers(Biens_Consommation):
	def __init__(self, name, args:()):
		super().__init__(name, args)

class Meubles(Articles_Menagers):
	def __init__(self, name, args:()):
		super().__init__(name, args[:3])
		self.materiau = args[3]
		self.couleur = args[4]
		self.dimensions = args[5]

class Canape(Meubles):
	def __init__(self, name, args:()):
		super().__init__(name, args)

class Chaise(Meubles):
	def __init__(self, name, args:()):
		super().__init__(name, args)

class Table(Meubles):
	def __init__(self, name, args:()):
		super().__init__(name, args)

class Appareils_Electromenagers(Articles_Menagers):
	def __init__(self, name, args:()):
		super().__init__(name, args[:3])
		self.capacite = args[3]

class Refrigerateur(Appareils_Electromenagers):
	def __init__(self, name, args:()):
		super().__init__(name, args[:4])
		self.efficacite = args[4]

class Lave_vaisselle(Appareils_Electromenagers):
	def __init__(self, name, args:()):
		super().__init__(name, args[:4])
		self.programme = args[4]

class Lave_linge(Appareils_Electromenagers):
	def __init__(self, name, args:()):
		super().__init__(name, args[:4])
		self.programme = args[4]

class Ustensiles_Cuisine(Articles_Menagers):
	def __init__(self, name, args:()):
		super().__init__(name, args[:3])
		self.materiaux = args[3]

class Casserole(Ustensiles_Cuisine):
	def __init__(self, name, args:()):
		super().__init__(name, args[:4])
		self.diametre = args[4]

class Batterie_Cuisine(Ustensiles_Cuisine):
	def __init__(self, name, args:()):
		super().__init__(name, args[:4])
		self.nombre_pieces = args[4]

class Habillement(Biens_Consommation):
	def __init__(self, name, args:()):
		super().__init__(name, args)

class Vetements(Habillement):
	def __init__(self, name, args:()):
		super().__init__(name, args[:3])
		self.taille = args[3]
		self.couleur = args[4]
		self.matiere = args[5]

class Haut(Vetements):
	def __init__(self, name, args:()):
		super().__init__(name, args)

class Pantalon(Vetements):
	def __init__(self, name, args:()):
		super().__init__(name, args)

class Robe(Vetements):
	def __init__(self, name, args:()):
		super().__init__(name, args)

class Casquette(Habillement):
	def __init__(self, name, args:()):
		super().__init__(name, args[:3])
		self.couleur = args[3]

class Chaussures(Habillement):
	def __init__(self, name, args:()):
		super().__init__(name, args[:3])
		self.pointure = args[3]

#c=Chaussures('c_00142',(12,25,"GAP",42))
