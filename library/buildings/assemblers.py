from library import Product
from library.halfstuff.lvl1 import IronPlate
from library.halfstuff.lvl2 import Gear
from library.halfstuff.lvl3 import ElectronicCircuit
from library.buildings.mods import SpeedModule1


__all__ = ['Assembler3', 'Assembler2', 'Assembler1']


class Assembler1(metaclass=Product):
    name = "Assembler 1"
    prod_time = 0.5
    recipe = {IronPlate: 9, Gear: 5, ElectronicCircuit: 3}


class Assembler2(metaclass=Product):
    name = "Assembler 2"
    prod_time = 0.5
    recipe = {IronPlate: 9, Gear: 5, ElectronicCircuit: 3, Assembler1: 1}


class Assembler3(metaclass=Product):
    name = "Assembler 3"
    prod_time = 0.5
    recipe = {Assembler2: 2, SpeedModule1: 4}

