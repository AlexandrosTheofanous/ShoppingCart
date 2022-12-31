from pricer import Pricer

class Item:
    """
    Class Item is used to define new items and store instances of their type and price for faster access.
    """
    def __init__(self, name):
        self.name = name
        self.price = -1
        
    def get_name(self):
        return self.name

    def get_price(self):
        if self.price == -1:
            pricer = Pricer()
            self.price = pricer.get_price(self.name)
        return self.price
