import abc


class BaseClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def cost(self):
        pass

    @abc.abstractmethod
    def description(self):
        pass


class AddOns(BaseClass, metaclass=abc.ABCMeta):
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


class Mocha(AddOns):
    def __init__(self, base_class):
        self._base_class = base_class
        self._cost = 5
        self._description = "Mocha"

    def cost(self):
        return self._base_class.cost() + self._cost

    def description(self):
        return f"{self._base_class.description()} + {self._description}"


class Whip(AddOns):
    def __init__(self, base_class):
        self._base_class = base_class
        self._cost = 3
        self._description = "Whip"

    def cost(self):
        return self._base_class.cost() + self._cost

    def description(self):
        return f"{self._base_class.description()} + {self._description}"


class Soy(AddOns):
    def __init__(self, base_class):
        self._base_class = base_class
        self._cost = 4
        self._description = "Soy"

    def cost(self):
        return self._base_class.cost() + self._cost

    def description(self):
        return f"{self._base_class.description()} + {self._description}"


# Generic functions
def get_bill(drink):
    print(f"Current order: {drink.description()}")
    print(f"Cost: ${drink.cost()}\n")


def display_welcome():
    print("Welcome to StarBuzz Cafe!\n", "-" * 80)
    print(f"You can order: {'/ '.join(drinks)}")
    print(f"Available add ons: {'/ '.join(addons)}")
    print("-" * 80)
    print("Feel free to make your own drink!")


def new_drink(order):
    if order in drinks:
        drink = drinks[order]()
        get_bill(drink)
        return drink
    else:
        print("Please choose a drink first!")
        return None


def add_on_drink(drink, addon):
    if order in addons:
        drink = addons[order](drink)
        get_bill(drink)
        print(
            "Feel free to pile up as many add ons as you want"
            "\nThis is totally dynamic!"
        )
    else:
        print("We don't have that add on yet! \nTry an available add on.\n")
    return drink


def create_drink(drink, order):
    if drink is None:
        drink = new_drink(order)
    else:
        drink = add_on_drink(drink, order)

    return drink


if __name__ == "__main__":

    drink = None
    drinks = {
        cls.__name__: cls
        for cls in BaseClass.__subclasses__()
        if cls.__name__ != "AddOns"
    }
    addons = {cls.__name__: cls for cls in AddOns.__subclasses__()}

    display_welcome()

    while True:
        order = input("> ")
        drink = create_drink(drink, order)
