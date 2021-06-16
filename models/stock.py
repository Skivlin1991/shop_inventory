class Stock:
    def __init__(self, name , description, manufacturer, cost, price, in_stock = True, id = None):
        self.name = name 
        self.description = description 
        self.manufacturer = manufacturer
        self.cost = cost             
        self.price = price
        self.in_stock = in_stock
        self.id = id