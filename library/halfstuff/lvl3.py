from library import Product
from library.halfstuff.lvl1 import IronPlate
from library.halfstuff.lvl2 import CopperCable, SteelPlate, Sulfur, Gear
from library.raw import Water
from library.buildings.pipes import Pipe


__all__ = ['ElectronicCircuit', 'EmptyBarrel', 'SulfuricAcid', 'EngineUnit']


class ElectronicCircuit(metaclass=Product):
    name = "Electronic Circuit"
    prod_time = 0.5
    recipe = {IronPlate: 1, CopperCable: 3}


class EmptyBarrel(metaclass=Product):
    name = "Empty Barrel"
    prod_time = 1
    recipe = {SteelPlate: 1}


class SulfuricAcid(metaclass=Product):
    name = "Sulfuric Acid"
    prod_time = 1
    recipe = {Water: 100, Sulfur: 5, IronPlate: 1}


class EngineUnit(metaclass=Product):
    name = "Engine Unit"
    prod_time = 10
    recipe = {SteelPlate: 1, Gear: 1, Pipe: 2}
