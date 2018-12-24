from library import Product
from library.halfstuff.lvl2 import SteelPlate, CopperCable
from library.halfstuff.lvl3 import ElectronicCircuit
from library.halfstuff.lvl4 import AdvancedCircuit
from library.halfstuff.lvl5 import ProcessingUnit

__all__ = ['Beacon', 'SpeedModule3', 'SpeedModule2', 'SpeedModule1', 'ProductivityModule2', 'ProductivityModule1',
           'EfficiencyModule2', 'EfficiencyModule1', 'ProductivityModule3', 'EfficiencyModule3']


class Beacon(metaclass=Product):
    name = "Beacon"
    prod_time = 15
    recipe = {SteelPlate: 10, CopperCable: 10, ElectronicCircuit: 20, AdvancedCircuit: 20}


class SpeedModule1(metaclass=Product):
    name = "Speed Module 1"
    prod_time = 15
    recipe = {ElectronicCircuit: 5, AdvancedCircuit: 5}


class SpeedModule2(metaclass=Product):
    name = "Speed Module 2"
    prod_time = 30
    recipe = {SpeedModule1: 4, ProcessingUnit: 5, AdvancedCircuit: 5}


class SpeedModule3(metaclass=Product):
    name = "Speed Module 3"
    prod_time = 60
    recipe = {SpeedModule2: 5, ProcessingUnit: 5, AdvancedCircuit: 5}


class EfficiencyModule1(SpeedModule1, metaclass=Product):
    name = "Efficiency Module 1"


class EfficiencyModule2(metaclass=Product):
    name = "Efficiency Module 2"
    prod_time = 30
    recipe = {EfficiencyModule1: 4, ProcessingUnit: 5, AdvancedCircuit: 5}


class EfficiencyModule3(metaclass=Product):
    name = "Efficiency Module 3"
    prod_time = 60
    recipe = {EfficiencyModule2: 4, ProcessingUnit: 5, AdvancedCircuit: 5}


class ProductivityModule1(SpeedModule1, metaclass=Product):
    name = "Productivity Module 1"


class ProductivityModule2(metaclass=Product):
    name = "Productivity Module 2"
    prod_time = 30
    recipe = {ProductivityModule1: 4, ProcessingUnit: 5, AdvancedCircuit: 5}


class ProductivityModule3(metaclass=Product):
    name = "Productivity Module 3"
    prod_time = 60
    recipe = {ProductivityModule2: 4, ProcessingUnit: 5, AdvancedCircuit: 5}
