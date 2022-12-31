import unittest

from shopping_cart import ShoppingCartConcreteCreator
from test_utils import Capturing

def create_cart(items):
    sc = ShoppingCartConcreteCreator().operation()
    for item in items:
        sc.add_item(item[0],item[1])

    return sc

class ShoppingCartTest(unittest.TestCase):
    def test_print_receipt(self):
        add_items = [("apple", 2)]
        sc = create_cart(add_items)
        with Capturing() as output:
            sc.print_receipt("item","quantity","price")
        self.assertEqual("apple - 2 - 100", output[0])
        self.assertEqual("Total = 200", output[1])

    def test_different_output_order(self):
        add_items = [("apple", 2)]
        sc = create_cart(add_items)
        with Capturing() as output:
            sc.print_receipt("item","quantity","price")
        self.assertEqual("apple - 2 - 100", output[0])
        with Capturing() as output:
            sc.print_receipt("quantity","item","price")
        self.assertEqual("2 - apple - 100", output[0])
        with Capturing() as output:
            sc.print_receipt("quantity","price","item")
        self.assertEqual("2 - 100 - apple", output[0])

    def test_doesnt_explode_on_mystery_item(self):
        add_items = [("apple",2),("banana", 5),("pear", 5)]
        sc = create_cart(add_items)
        with Capturing() as output:
            sc.print_receipt("item","quantity","price")
        self.assertEqual("apple - 2 - 100", output[0])
        self.assertEqual("banana - 5 - 200", output[1])
        self.assertEqual("pear - 5 - 0", output[2])
        self.assertEqual("Total = 1200", output[3])

    def test_same_item_scanned(self):
        add_items = [("apple", 2),("banana", 5),("orange", 5),("apple", 2),("banana", 5),("apple", 5),("mango", 1)]
        sc = create_cart(add_items)
        with Capturing() as output:
            sc.print_receipt("item","quantity","price")
        self.assertEqual("apple - 9 - 100", output[0])
        self.assertEqual("banana - 10 - 200", output[1])
        self.assertEqual("orange - 5 - 300", output[2])
        self.assertEqual("mango - 1 - 250", output[3])
        self.assertEqual("Total = 4650", output[4])

    def test_empty_cart(self):
        add_items = []
        sc = create_cart(add_items)
        with Capturing() as output:
            sc.print_receipt("item","quantity","price")
        self.assertEqual("Empty cart",output[0])

    def test_empty_cart_initially(self):
        add_items = []
        sc = create_cart(add_items)
        with Capturing() as output:
            sc.print_receipt("item","quantity","price")
        self.assertEqual("Empty cart",output[0])
        add_items = [("apple", 2),("banana", 5),("orange", 5),("apple", 2),("banana", 5),("apple", 5),("mango", 1)]
        for item in add_items:
            sc.add_item(item[0],item[1])
        with Capturing() as output:
            sc.print_receipt("item","quantity","price")
        self.assertEqual("apple - 9 - 100", output[0])
        self.assertEqual("banana - 10 - 200", output[1])
        self.assertEqual("orange - 5 - 300", output[2])
        self.assertEqual("mango - 1 - 250", output[3])
        self.assertEqual("Total = 4650", output[4])

unittest.main(exit=False)
