import math

from copy import deepcopy

from library import *

import pprint
pp = pprint.PrettyPrinter(indent=4, depth=10, width=120)


class ConveyorBelt:
    bandwidth = 40


class Factory:
    base_speed = 0
    base_out = 0
    mod_slots = 0
    product = None
    mods = []

    def __init__(self, mods=None):
        if mods:
            self.mods = mods

    @property
    def speed(self):
        bonus = sum([self.base_out * mod.speed_mod for mod in self.mods])
        return self.base_speed + bonus

    @property
    def out(self):
        bonus = sum([self.base_out * mod.production_mod for mod in self.mods])
        return self.base_out + bonus

    def product_per_second(self, product):
        if product is not None:
            return (1 / product.prod_time) * self.speed
        else:
            return None

    def _calculate_number_of_factories(self, product, required_prod_per_sec):
        result = math.ceil(required_prod_per_sec / self.product_per_second(product))
        return result

    def calculate(self, product, required_prod_per_sec):
        factories_count = self._calculate_number_of_factories(product, required_prod_per_sec)
        print('To produce {prod_speed} {product} per second need {factories} factories'.format(
            product=product.name, prod_speed=required_prod_per_sec, factories=factories_count))
        return [{'factory_type' : self.__name__, 'factori_count': factories_count, 'product': product}, ]



class BaseMod:
    speed_mod = 0
    production_mod = 0


class ProductivityModule3(BaseMod):
    speed_mod = -0.15
    production_mod = 0.1


class SpeedModule3(BaseMod):
    speed_mod = 0.5


class ElectricFurnance(Factory):
    base_speed = 2
    base_out = 1
    product = None
    mod_slots = 2


if __name__ == '__main__':
    electric_furnace = ElectricFurnance()

    electric_furnace.calculate(IronPlate, ConveyorBelt.bandwidth)



