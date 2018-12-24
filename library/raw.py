from library import Ore, Product


__all__ = ['Coal', 'CopperOre', 'IronOre', 'Stone', 'CrudeOil', 'Water']


class IronOre(metaclass=Ore):
    name = "Iron Ore"
    prod_speed = 0.525


class CopperOre(metaclass=Ore):
    name = "Copper Ore"
    prod_speed = 0.525


class Coal(metaclass=Ore):
    name = "Coal"
    prod_speed = 0.525


class Stone(metaclass=Ore):
    name = "Stone"
    prod_speed = 0.65


class CrudeOil(metaclass=Ore):
    name = "Crude Oil"
    prod_speed = 10


class Water(metaclass=Product):
    name = "Water"
    prod_time = 0
