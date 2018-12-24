from library import Product
from library.halfstuff.lvl1 import IronPlate
from library.halfstuff.lvl2 import Gear
from library.halfstuff.lvl3 import ElectronicCircuit


__all__ = ['UndergroundBelt', 'TransportBelt', 'Splitter', 'FastUndergroundBelt', 'FastTransportBelt', 'FastSplitter']


class TransportBelt(metaclass=Product):
    name = "Transport Belt"
    prod_time = 0.5
    prod_count = 2
    recipe = {IronPlate: 1, Gear: 1}


class FastTransportBelt(metaclass=Product):
    name = "Fast Transport Belt"
    prod_time = 0.5
    recipe = {TransportBelt: 1, Gear: 5}


class UndergroundBelt(metaclass=Product):
    name = "Underground Belt"
    prod_time = 1
    prod_count = 2
    recipe = {IronPlate: 10, TransportBelt: 5}


class FastUndergroundBelt(metaclass=Product):
    name = "Fast Underground Belt"
    prod_time = 2
    prod_count = 2
    recipe = {Gear: 40, UndergroundBelt: 2}


class Splitter(metaclass=Product):
    name = "Splitter"
    prod_time = 1
    recipe = {IronPlate: 5, TransportBelt: 4, ElectronicCircuit: 5}


class FastSplitter(metaclass=Product):
    name = "Fast Splitter"
    prod_time = 2
    recipe = {Gear: 10, ElectronicCircuit: 10, Splitter: 1}
