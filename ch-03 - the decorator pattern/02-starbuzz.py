import abc


class BaseClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def cost(self):
        pass

    @abc.abstractmethod
    def description(self):
        pass


class Decorator(BaseClass, metaclass=abc.ABCMeta):
    def __init__(self, base_class):
        self._base_class = base_class

    @abc.abstractmethod
    def cost(self):
        return self._base_class.cost() + self.cost

    @abc.abstractmethod
    def description(self):
        return f"{self._base_class.description()} {self.description}"


class HouseBlend(BaseClass):
    def __init__(self):
        self._cost = 10
        self._description = "House Blend"

    def cost(self):
        return self._cost

    def description(self):
        return self._description


class Mocha(Decorator):
    def __init__(self, base_class):
        self._base_class = base_class
        self._cost = 5
        self._description = "Mocha"

    def cost(self):
        return self._base_class.cost() + self._cost

    def description(self):
        return f"{self._base_class.description()} + {self._description}"


class Whip(Decorator):
    def __init__(self, base_class):
        self._base_class = base_class
        self._cost = 3
        self._description = "Whip"

    def cost(self):
        return self._base_class.cost() + self._cost

    def description(self):
        return f"{self._base_class.description()} + {self._description}"


class Soy(Decorator):
    def __init__(self, base_class):
        self._base_class = base_class
        self._cost = 4
        self._description = "Soy"

    def cost(self):
        return self._base_class.cost() + self._cost

    def description(self):
        return f"{self._base_class.description()} + {self._description}"


if __name__ == "__main__":

    def get_bill(drink):
        print(f"You ordered a {drink.description()}")
        print(f"That will be ${drink.cost()}\n")

    drink = HouseBlend()
    get_bill(drink)

    drink = HouseBlend()
    drink = Mocha(drink)
    get_bill(drink)

    drink = HouseBlend()
    drink = Mocha(drink)
    drink = Mocha(drink)
    drink = Soy(drink)
    drink = Whip(drink)
    get_bill(drink)
