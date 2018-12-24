from library import Product
from library.halfstuff.lvl1 import IronPlate


__all__ = ['Pipe', 'PipeToGround']


class Pipe(metaclass=Product):
    name = "Pipe"
    prod_time = 0.5
    recipe = {IronPlate: 1}


class PipeToGround(metaclass=Product):
    name = "Pipe To Ground"
    prod_time = 0.5
    recipe = {IronPlate: 5, Pipe: 10}
