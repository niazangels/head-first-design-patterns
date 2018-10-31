class SubsciberOne(object):
    def __init__(self, name):
        self.name = name

    def update(self, payload):
        print(f'{self.name} received {str(payload)}')

# Another subsciber with a different update function
class SubsciberTwo(object):
    def __init__(self, name):
        self.name = name

    def receive(self, payload):
        print(f'{self.name} received {str(payload)}')


# Need changes in Publisher
class Publisher(object):
    def __init__(self):
        self.subscribers = {}

    def add_subscriber(self, subscriber, callback=None):
        if callback is None:
            callback = getattr(subscriber, 'update')
        self.subscribers[subscriber] = callback

    def remove_subscriber(self, subscriber):
        self.subscribers.pop(subscriber)

    def dispatch(self, payload):
        for subsciber, callback in self.subscribers.items():
            callback(payload)

if __name__ == '__main__':

    dhanush = SubsciberOne('Dhanush')
    vijay_sethupathi = SubsciberTwo('Vijay Sethupathi')
    simbu = SubsciberTwo('Simbu')

    box_office = Publisher()

    box_office.add_subscriber(dhanush)
    box_office.add_subscriber(vijay_sethupathi, vijay_sethupathi.receive)
    box_office.add_subscriber(simbu, simbu.receive)

    box_office.dispatch('New offer from Gautham Vasudev Menon')

    box_office.remove_subscriber(simbu)
    box_office.dispatch('Another offer from Gautham Vasudev Menon')

