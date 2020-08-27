"""
"""

import copy

class InventoryAllocator:

    def __init__(self, order, inventory):
        self.order = order
        self.inventory = inventory
        self.ans = []
    
    def getShipment(self):
        
        # check for invalid input datatypes
        if type(self.order) != dict or type(self.inventory) != list:
            self.ans = []
            return self.ans

        # check for null values
        if not self.order or not self.inventory:
            self.ans = []
            return self.ans
        
        else:
            # create deepcopy of order dictionary and inventory list
            orderCopy = copy.deepcopy(self.order)
            inventoryWarehouses = copy.deepcopy(self.inventory)

            # initialize ans list to store final shipment list
            self.ans = []

            # iterate through all the warehouse
            for warehouse in inventoryWarehouses:

                # dictionary to store items we can ship from current warehouse
                canShipFromWarehouse = {}

                # iterate through every item present in order
                for key in orderCopy.keys():

                    # check if we need to fulfill this item
                    if orderCopy[key] > 0:
                        # check if this item is present in current warehouse
                        if key in warehouse['inventory'].keys():
                            # check if said warehouse has more stock than the amount needed
                            if warehouse['inventory'][key] > orderCopy[key]:
                                canShipFromWarehouse[key] = orderCopy[key]
                                # update warehouse
                                warehouse['inventory'][key] = warehouse['inventory'][key] - orderCopy[key]
                                # current item fulfilled
                                orderCopy[key] = 0
                            else:
                                # This warehouse does not have stock to fulfil this order item
                                canShipFromWarehouse[key] = warehouse['inventory'][key]
                                orderCopy[key] = orderCopy[key] - warehouse['inventory'][key]
                                warehouse['inventory'][key] = 0

                # update ans list
                self.ans.append({warehouse['name']: canShipFromWarehouse})

            # Check if order is satisfied, or else return empty list
            for key in orderCopy.keys():
                if orderCopy[key] > 0:
                    self.ans = []
                    return self.ans

            # update inventory
            self.inventory = copy.deepcopy(inventoryWarehouses)
            # return ans list
            return self.ans

def main():
    order = {'apple': 5, 'banana': 5, 'orange': 5}
    inventory = [{ 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } }]
    ia = InventoryAllocator(order, inventory)
    ans = ia.getShipment()
    print(ans)
    print(ia.inventory)

if __name__=="__main__":
    main()