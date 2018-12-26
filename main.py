import json
import os
import functools
import math

import pprint

pp = pprint.PrettyPrinter(indent=4, depth=10, width=80)

with open('/home/tuenut/Downloads/Telegram Desktop/recipes.json', 'r') as file:
    recipes = json.load(file, )

PRODUCT_TYPES = {'advanced-crafting',
                 'centrifuging',
                 'chemistry',
                 'crafting',
                 'crafting-with-fluid',
                 'oil-processing',
                 'rocket-building',
                 'smelting'}

producers = {
    "electric-furnace": {
        "name": "electric-furnace",
        "prod_types": ['smelting'],
        "speed": 2,
        "mod slots": 2
    },
    "assembling-machine-1": {
        "name": "assembling-machine-1",
        "prod_types": ['crafting'],
        "speed": 0.5,
        "mod slots": 0
    },
    "assembling-machine-2": {
        "name": "assembling-machine-2",
        "prod_types": ['crafting', 'crafting-with-fluid', 'advanced-crafting'],
        "speed": 0.75,
        "mod slots": 2
    },
    "assembling-machine-3": {
        "name": "assembling-machine-3",
        "prod_types": ['crafting', 'crafting-with-fluid', 'advanced-crafting'],
        "speed": 1.25,
        "mod slots": 4
    },
    "oil-refinery.basic": {
        "name": "oil-refinery.basic",
        "prod_types": ['oil-processing'],
        "speed": 1,
        "mod slots": 3
    },
    "oil-refinery.advanced": {
        "name": "oil-refinery.advanced",
        "prod_types": ['oil-processing'],
        "speed": 1,
        "mod slots": 3
    },
    "oil-refinery.coal-liquefaction": {
        "name": "oil-refinery.coal-liquefaction",
        "prod_types": ['oil-processing'],
        "speed": 1,
        "mod slots": 3
    },
    "chemical-plant": {
        "name": "chemical-plant",
        "prod_types": ['chemistry'],
        "speed": 1.25,
        "mod slots": 3
    },
}


class Calculator:
    product = None
    product_asms = None
    amount = None
    target_speed = None
    time = None
    assemblers_schema = []

    EXCLUDE_LIST = ['iron-ore', 'copper-ore', 'coal', 'petroleum-gas', 'stone', 'water']



    def input_data(self, product_name=None, amount=0, time=0, available_assemblers=list()):
        self.assemblers_schema = []
        self.product = recipes[product_name]
        self.product_asms = available_assemblers
        self.amount = amount
        self.time = time
        self.target_speed = amount / time

    def calc(self, ):
        if not self.product_asms:
            return "Cant craft without assemblers. Self craft not implemented."

        product_out = [p['amount'] for p in self.product['products'] if p['name'] == self.product['name']][0]
        assembler_obj = self._get_asm(self.product['category'])
        product_time = self.product['energy'] / assembler_obj['speed']
        product_speed = product_out / product_time
        amount_af_assemblers = self.target_speed / product_speed

        children = []
        calculated = {
            self.product['name']: {
                'amount': self.amount,
                'int': math.ceil(amount_af_assemblers),
                'producer': assembler_obj['name'],
                'speed': product_speed,
                'children': children
            }
        }

        self.assemblers_schema.append(calculated)

        if self.product['ingredients']:
            self._calc_recursive(self.product['ingredients'], self.amount, parent=children)

        return self.assemblers_schema

    def _calc_recursive(self, ingredients, amount_of_parent, parent=None):
        for item in ingredients:
            try:
                product = recipes[item['name']]
            except KeyError:
                continue

            product_out = [p['amount'] for p in product['products'] if p['name'] == product['name']][0]
            amount_of_product = amount_of_parent * (item['amount'] )
            assembler_obj = self._get_asm(product['category'])
            product_time = product['energy'] / assembler_obj['speed']
            product_speed = product_out / product_time
            amount_af_assemblers = amount_of_product / self.time / product_speed

            children = []
            calculated = {
                product['name']: {
                    'amount': amount_of_product,
                    'int': amount_af_assemblers,
                    'producer': assembler_obj['name'],
                    'speed': product_speed,
                    'children': children
                }
            }
            parent.append(calculated)

            if product['ingredients'] and item['name'] not in self.EXCLUDE_LIST:
                self._calc_recursive(product['ingredients'],
                                     amount_of_product / product_out,
                                     parent=children)



    def _get_asm(self, prod_type):
        asm = [producers[asm_name]
               for asm_name in self.product_asms
               if prod_type in producers[asm_name]['prod_types']]
        return asm[0]


if __name__ == '__main__':
    calculator = Calculator()
    amount_dict = {}
    prods = ['high-tech-science-pack', 'military-science-pack', 'production-science-pack', 'science-pack-1', 'science-pack-2', 'science-pack-3']

    for prod in prods:
        calculator.input_data(product_name=prod,
                              amount=100,
                              time=60,
                              available_assemblers=['assembling-machine-3', 'electric-furnace', 'chemical-plant',
                                                    'oil-refinery.basic'])
        a = calculator.calc()
        # pp.pprint(a)


        def get_amount(item):
            for iitem in item:
                name, val = list(iitem.items())[0]
                get_amount(val['children'])
                try:
                    amount_dict[name] += val['amount']
                except KeyError:
                    amount_dict[name] = val['amount']

        for key in a:
            name, val = list(key.items())[0]
            get_amount(val['children'])
            try:
                amount_dict[name] += val['amount']
            except KeyError:
                amount_dict[name] = val['amount']

    pp.pprint(amount_dict)