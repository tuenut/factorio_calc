class Product(type):
    name = str()
    prod_time = float()
    recipe = dict()
    prod_count = 1

    @property
    def summary_time(self):
        """Суммарное время производства с учетом всех материалов"""
        items = [item.summary_time * self.recipe[item] for item in self.recipe]
        recipe_time = sum(items)
        return (recipe_time + self.prod_time) / self.prod_count

    @property
    def _recipe_name2class(self):
        """Вспомогательная ерунда для получения класса материала из рецепта по названию."""
        return {klass.name.lower(): klass for klass in self.recipe.keys()}

    def get_mat_count(self, mat_name):
        """Вернет количество материала на производство продукта"""
        # TODO расширить для поиска вглубь
        return self.recipe[self._recipe_name2class[mat_name.lower()]]

    def __str__(self):
        return '"%s" with full production time %s' % (self.name, self.summary_time)

    __repr__ = __str__


class Ore(Product):
    """для добычи руды известна скорость добычи, а не время производства, поэтому премя происзводства рассчитывается"""
    prod_speed = float()

    @property
    def prod_time(self):
        return 1 / self.prod_speed
