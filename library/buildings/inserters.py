from library import Product
from library.halfstuff.lvl1 import IronPlate
from library.halfstuff.lvl2 import Gear
from library.halfstuff.lvl3 import ElectronicCircuit
from library.halfstuff.lvl4 import AdvancedCircuit


__all__ = ['StackInserter', 'LongInserter', 'Inserter', 'FilterInserter', 'FastInserter', 'BurnerInserter']


class BurnerInserter(metaclass=Product):
    name = "Burner Inserter"
    prod_time = 0.5
    recipe = {IronPlate: 1, Gear: 1}


class Inserter(metaclass=Product):
    name = "Inserter"
    prod_time = 0.5
    recipe = {IronPlate: 1, Gear: 1, ElectronicCircuit: 1}


class LongInserter(metaclass=Product):
    name = "Long Inserter"
    prod_time = 0.5
    recipe = {IronPlate: 1, Gear: 1, Inserter: 1}


class FastInserter(metaclass=Product):
    name = "Fast Inserter"
    prod_time = 0.5
    recipe = {IronPlate: 2, ElectronicCircuit: 2, Inserter: 1}


class FilterInserter(metaclass=Product):
    name = "Filter Inserter"
    prod_time = 0.5
    recipe = {ElectronicCircuit: 4, Inserter: 1}


class StackInserter(metaclass=Product):
    name = "Filter Inserter"
    prod_time = 0.5
    recipe = {Gear: 15, ElectronicCircuit: 15, AdvancedCircuit: 1, FastInserter: 1}
