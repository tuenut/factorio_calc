from library import Product
from library.halfstuff.lvl1 import IronPlate
from library.halfstuff.lvl2 import SteelPlate


__all__ = ['StorageTank', 'SteelChest', 'IronChest']


class IronChest(metaclass=Product):
    name = "Iron Chest"
    prod_time = 0.5
    recipe = {IronPlate: 8}


class SteelChest(metaclass=Product):
    name = "steel Chest"
    prod_time = 0.5
    recipe = {SteelPlate: 8}


class StorageTank(metaclass=Product):
    name = "Storage Tank"
    prod_time = 3
    recipe = {IronPlate: 20, SteelPlate: 5}
