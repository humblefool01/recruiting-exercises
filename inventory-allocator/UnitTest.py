import unittest
from InventoryAllocator import InventoryAllocator

class UnitTest(unittest.TestCase):

    def testHappyCase(self):
        # test for happy case
        order = {'apple': 5}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}]
        output = [{'owd': {'apple': 5}}]
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.getShipment(), output)

    def testNotEnoughInventory(self):
        # test for not enough stock in inventory
        order = {'apple': 5}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = []
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.getShipment(), output)

    def testSplitAcrossWarehouses(self):
        # test to ship items from multiple warehouses
        order = {'apple': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        output = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.getShipment(), output)

        # test to split order across multiple warehouses
        order = {'apple': 5, 'banana': 5, 'orange': 5}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 5}}, {'name': 'dm', 'inventory': {'banana': 5, 'orange': 5}}]
        output = [{'owd': {'apple': 5, 'orange': 5}}, {'dm': {'banana': 5}}]
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.getShipment(), output)

        # test to split items and split orders across warehouses
        order = {'apple': 15, 'banana': 5, 'orange': 5}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}},
                     {'name': 'dm', 'inventory': {'apple': 10, 'banana': 5, 'orange': 10}}]
        output = [{'owd': {'apple': 5, 'orange': 5}}, {'dm': {'apple': 10, 'banana': 5}}]
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.getShipment(), output)

    def testNoOrder(self):
        # test for no order present
        order = {}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = []
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.getShipment(), output)

    def testNoInventory(self):
        # test for no inventory present
        order = {'apple': 1}
        inventory = []
        output = []
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.getShipment(), output)

    def testNoOrderNoInventory(self):
        # test for no order and no inventory
        order = {}
        inventory = []
        output = []
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.getShipment(), output)

    def testNoItem(self):
        # test for item not found in inventory
        order = {'kiwi': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = []
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.getShipment(), output)

    def testInvalidInputFormat(self):
        # test for invalid input format
        order = ['kiwi', 1]
        inventory = {'name': 'owd', 'inventory': {'apple': 1}}
        output = []
        ia = InventoryAllocator(order, inventory)
        self.assertEqual(ia.getShipment(), output)

if __name__=='__main__':
    unittest.main()