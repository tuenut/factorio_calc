from library import Product
from library.raw import Water, IronOre
from library.halfstuff.lvl1 import IronPlate, CopperPlate, PetroleumGas, LightOil


__all__ = ['Gear', 'IronStick', 'CopperCable', 'SteelPlate', 'Sulfur', 'Lubricant']


class Gear(metaclass=Product):
    name = "Gear"
    prod_time = 0.5
    recipe = {IronPlate: 2}


class IronStick(metaclass=Product):
    name = "Iron Stick"
    prod_time = 0.5
    recipe = {IronOre: 1}


class CopperCable(metaclass=Product):
    name = "Copper Cable"
    prod_time = 0.5
    recipe = {CopperPlate: 1}


class SteelPlate(metaclass=Product):
    name = "Steel Plate"
    prod_time = 17.5
    recipe = {IronPlate: 5}


class Sulfur(metaclass=Product):
    name = "Sulfur"
    prod_time = 1
    recipe = {Water: 30, PetroleumGas: 30}


class Lubricant(metaclass=Product):
    """By Basic oil processing"""
    name = "Petroleum Gas"
    prod_time = 1
    prod_count = 10
    recipe = {LightOil: 10}