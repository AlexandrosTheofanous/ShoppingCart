from abc import ABC, abstractmethod
from typing import Dict

from shopping_cart_interface import IShoppingCart
from pricer import Pricer
from item import Item


class ShoppingCart(IShoppingCart):
    """
    Implementation of the shopping tills in our supermarket.
    """
    def __init__(self, pricer: Pricer):
        self.pricer = pricer
        self.total = 0
        self._contents: Dict[str,int] = {}

    def add_item(self, item_type: str, number: int):
        # adds new item to or update existing item in the shopping cart
        #if the item already exists in self._contents then we modify the relevant dictionary element
        # otherwise we create a new Item object to store in the dictionary
        cur_item = next((x for x in self._contents if x.get_name() == item_type), Item(item_type))
        if cur_item in self._contents:
            self._contents[cur_item] += number
        else:
            self._contents[cur_item] = number
        self.total += cur_item.get_price() * number

    # the order that price, quantity and item_type are printed in the receipt is defined by the order they are given
    # as parameters
    def print_receipt(self, first, second, third):
        # check if the cart is empty
        if not self._contents:
            print("Empty cart")
        else:
            #by traversing the dictionary linearly the items are printed in the order they were scanned
            for item in self._contents: 
                #Future elements that need to be printed can be added and modified easily
                ord_dic = {"price" : item.get_price(), "item" : item.get_name(), "quantity" : self._contents[item]}       
                print(f"{ord_dic[first]} - {ord_dic[second]} - {ord_dic[third]}")        
            print(f"Total = {self.total}")                   

class ShoppingCartCreator(ABC):
    """
    Interface for the ShoppingCart creator.
    The creation process will be delegated to the subclasses of this class.
    """
    @abstractmethod
    def factory_method(self) -> ShoppingCart:
        # return the ShoppingCart object
        pass

    def operation(self) -> ShoppingCart:
        # Here more operations can be performed on the ShoppingCart object
        # returns ShoppingCart object
        return self.factory_method()

class ShoppingCartConcreteCreator(ShoppingCartCreator):
    """
    Concrete class for the ShoppingCart creator.
    Implements the factory_method
    """
    def factory_method(self) -> ShoppingCart:
        # returns ShoppingCart object
        return ShoppingCart(Pricer())


