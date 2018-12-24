from library import Product
from library.halfstuff.lvl2 import SteelPlate
from library.halfstuff.lvl3 import ElectronicCircuit, SulfuricAcid
from library.halfstuff.lvl4 import AdvancedCircuit, Battery, ElectricEngineUnit


__all__ = ['ProcessingUnit', 'FlyingRobotFrame']


class ProcessingUnit(metaclass=Product):
    name = "Processing Unit"
    prod_time = 10
    recipe = {ElectronicCircuit: 20, AdvancedCircuit: 2, SulfuricAcid: 5}


class FlyingRobotFrame(metaclass=Product):
    name = "Flying Robot Frame"
    prod_time = 20
    recipe = {SteelPlate: 1, Battery: 2, ElectronicCircuit: 3, ElectricEngineUnit: 1}
