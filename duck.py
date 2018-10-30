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


# Mallard Duck

class MallardDuck(Duck):
    
    def __init__(self):
        super().__init__()
    
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()


if __name__=='__main__':
    my_duck = MallardDuck()
    my_duck.perform_quack()
    my_duck.perform_fly()    
