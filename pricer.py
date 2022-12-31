
class Pricer:
    """
    a datastore for the available products in the supermarket
    """
    def __init__(self):
        self.__pricing_database = {"apple": 100, "banana": 200, "orange" : 300, "mango" : 250}

    def get_price(self, itemtype: str):
        """ Returns the price of the item passed, in Euro-cent.
        Eg. if an item costs €1, this will return 100
        If itemType is an unknown string, store policy is that the item is free.
        """
        if itemtype not in self.__pricing_database:
            return 0
        return self.__pricing_database[itemtype]

    # update_item and add_item seperation was implemented to minimize human error
    # def add_item(self, item_type, item_price):
    #     if item_type in self.__pricing_database:
    #         print("Item already in database. Please use the update funtion")
    #         return
    #     self.__pricing_database[item_type] = item_price

    # def update_item(self, item_type, item_price):
    #     if item_type not in self.__pricing_database:
    #         print("Item not in database. Please use the add funtion")
    #         return
    #     self.__pricing_database[item_type] = item_price

    # def remove_item(self, item_type, item_price):
    #     del self.__pricing_database[item_type]

