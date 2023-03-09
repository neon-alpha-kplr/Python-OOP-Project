class Product:
    def __init__(self, cost, price, brand) -> None:
        self.cost=cost
        self.price=price
        self.brand=brand

class Furniture(Product):
    def __init__(self, cost, price, brand, materials, color, dimensions):
        super().__init__(cost, price, brand)
        self.materials=materials
        self.color=color
        self.dimensions=dimensions
    def display(self):
        print(f"{self.color} de marque {self.brand} en {self.materials}. Marge brute : {self.price-self.cost}€ ({self.cost}/{self.price}). Dimensions : {self.dimensions}",end='')

class Sofa(Furniture):
    def __init__(self, cost, price, brand, materials, color, dimensions, convertible=False):
        super().__init__(cost, price, brand, materials, color, dimensions)
        self.convertible=convertible
    def display(self):
        print("Canapé ",end='')
        super().display()
        if self.convertible:
            print(". Convertible")
        else:
            print(". Non convertible")

class Chair(Furniture):
    def __init__(self, cost, price, brand, materials, color, dimensions, series="Kapok"):
        super().__init__(cost, price, brand, materials, color, dimensions)
        self.series=series
    def display(self):
        print("Chaise ",end='')
        super().display()
        print(" Série ",self.series)

class Table(Furniture):
    def __init__(self, cost, price, brand, materials, color, dimensions, extendable=False):
        super().__init__(cost, price, brand, materials, color, dimensions)
        self.extendable=extendable
    def display(self):
        print("Table ",end='')
        super().display()
        if self.extendable:
            print(". Extensible")
        else:
            print(". Non extensible")

canape1=Sofa(1000,2000,"OKLM","Cuir","Blanc","200x100x80",True)
canape2=Sofa(800,1600,"SIESTA","Tissu","Bleu","150x90x70",False)
chaise1=Chair(50,100,"PEPOUSE","Plastique","Rouge","50x50x70","Gridso")
chaise2=Chair(75,150,"PEPOUSE","Métal","Gris","60x60x80","Ironklad")
chaise3=Chair(75,150,"PEPOUSE","Bois","Chêne","60x60x80")
table1=Table(350,700,"TEX","Verre","Transparent","120x60x75",True)
table2=Table(250,500,"TEX","Bois","Chêne","150x80x75",False)
canape1.display()
canape2.display()
chaise1.display()
chaise2.display()
chaise3.display()
table1.display()
table2.display()