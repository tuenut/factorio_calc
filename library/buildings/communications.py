from library import Product
from library.halfstuff.lvl1 import IronPlate, CopperPlate
from library.halfstuff.lvl2 import SteelPlate
from library.halfstuff.lvl3 import EngineUnit
from library.halfstuff.lvl4 import AdvancedCircuit
from .pipes import Pipe


__all__ = ['MediumElectricPole', 'Substation', 'BigElectricPole', 'Pump']


class MediumElectricPole(metaclass=Product):
    name = "Medium Electric Pole"
    prod_time = 0.5
    recipe = {IronPlate: 2, CopperPlate: 2}


class BigElectricPole(metaclass=Product):
    name = "Big Electric Pole"
    prod_time = 0.5
    recipe = {IronPlate: 5, CopperPlate: 5}


class Substation(metaclass=Product):
    name = "Substation"
    prod_time = 0.5
    recipe = {SteelPlate: 5, CopperPlate: 5, AdvancedCircuit: 5}


class Pump(metaclass=Product):
    name = "Pump"
    prod_time = 2
    recipe = {SteelPlate: 1, Pipe: 1, EngineUnit: 1}

