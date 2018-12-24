from library import Product
from library.halfstuff.lvl1 import PetroleumGas,  CopperPlate, IronPlate
from library.halfstuff.lvl2 import CopperCable,  Lubricant
from library.halfstuff.lvl3 import ElectronicCircuit, SulfuricAcid, EngineUnit
from library.raw import Coal


__all__ = ['PlasticBar', 'ElectricEngineUnit', 'Battery', 'AdvancedCircuit']


class PlasticBar(metaclass=Product):
    name = "Steel Plate"
    prod_time = 1
    recipe = {Coal: 1, PetroleumGas: 20}


class AdvancedCircuit(metaclass=Product):
    name = "Advanced Circuit"
    prod_time = 6
    recipe = {ElectronicCircuit: 2, CopperCable: 4, PlasticBar: 2}


class ElectricEngineUnit(metaclass=Product):
    name = "Electric Engine Unit"
    prod_time = 10
    recipe = {EngineUnit: 1, Lubricant: 15, ElectronicCircuit: 2}


class Battery(metaclass=Product):
    name = "Battery"
    prod_time = 5
    recipe = {CopperPlate: 1, IronPlate: 1, SulfuricAcid: 20}
