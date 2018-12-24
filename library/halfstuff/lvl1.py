from library import Product
from library.raw import *


__all__ = ['IronPlate', 'CopperPlate', 'PetroleumGas', 'LightOil']


class IronPlate(metaclass=Product):
    name = "Iron Plate"
    prod_time = 3.5
    recipe = {IronOre: 1}


class CopperPlate(metaclass=Product):
    name = "Copper Plate"
    prod_time = 3.5
    recipe = {CopperOre: 1}


class PetroleumGas(metaclass=Product):
    """By Advanced oil processing"""
    name = "Petroleum Gas"
    prod_time = 5
    prod_count = 55
    recipe = {CrudeOil: 100, Water: 100}


class LightOil(metaclass=Product):
    """By Basic oil processing"""
    name = "Petroleum Gas"
    prod_time = 5
    prod_count = 30
    recipe = {CrudeOil: 100}
