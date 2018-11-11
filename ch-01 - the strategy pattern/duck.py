# Fly Behaviors


class FlyBehavior(object):
    def __init__(self):
        return


class FlyWithWings(FlyBehavior):
    def __init__(self):
        super().__init__()

    def fly(self):
        print("I'm flying with wings")


class FlyNoWay(FlyBehavior):
    def __init__(self):
        super().__init__()

    def fly(self):
        print("No can't do!")


class FlyRocketPowered(FlyBehavior):
    def __init__(self):
        super().__init__()

    def fly(self):
        print("Flying with a 🚀")


# Quack Behaviors


class QuackBehavior(object):
    def __init__(self):
        return


class Quack(QuackBehavior):
    def __init__(self):
        super().__init__()

    def quack(self):
        print("Quack!")


class Squeak(QuackBehavior):
    def __init__(self):
        super().__init__()

    def quack(self):
        print("Squeak!")


class MuteQuack(QuackBehavior):
    def __init__(self):
        super().__init__()

    def quack(self):
        print("<!-- S i l e n c e -->")


# Duck


class Duck(object):
    def __init__(self):
        self.fly_behavior = FlyBehavior()
        self.quack_behavior = QuackBehavior()

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def perform_swim(self):
        print("All ducks float- even fake ones")

    def set_fly_behavior(self, fb):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb):
        self.quack_behavior = qb


# Mallard Duck


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a MallardDuck")


class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def display(self):
        print("I'm a ModelDuck")


if __name__ == "__main__":

    my_duck = MallardDuck()
    my_duck.display()
    my_duck.perform_quack()
    my_duck.perform_fly()

    print("\n")

    your_duck = ModelDuck()
    your_duck.display()
    your_duck.perform_quack()
    your_duck.set_fly_behavior(FlyRocketPowered())
    your_duck.perform_fly()
