import abc


class BaseClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def cost(self):
        pass


class Decorator(BaseClass, metaclass=abc.ABCMeta):
    def __init__(self, base_class):
        self._base_class = base_class

    @abc.abstractmethod
    def cost(self):
        pass


class ConcreteBase(BaseClass):
    def cost(self):
        pass


class ConcreteDecoratorA(Decorator):
    def cost(self):
        self._base_class.cost()


class ConcreteDecoratorB(Decorator):
    def cost(self):
        self._base_class.cost()


if __name__ == "__main__":
    concrete_component = ConcreteBase()
    concrete_decorator_a = ConcreteDecoratorA(concrete_component)
    concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)
    concrete_decorator_b.cost()
