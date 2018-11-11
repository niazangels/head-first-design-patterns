class Publisher(object):
    def __init__(self):
        self.subscribers = set()

    def add_subscriber(self, subscriber):
        self.subscribers.add(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.discard(subscriber)

    def dispatch(self, payload):
        for subscriber in self.subscribers:
            subscriber.update(payload)


class Subscriber(object):
    def __init__(self, name):
        self.name = name

    def update(self, payload):
        print(f"{self.name} received {str(payload)}")


if __name__ == "__main__":

    dhanush = Subscriber("Dhanush")
    vijay_sethupathi = Subscriber("Vijay Sethupathi")
    simbu = Subscriber("Simbu")

    box_office = Publisher()

    box_office.add_subscriber(dhanush)
    box_office.add_subscriber(vijay_sethupathi)
    box_office.add_subscriber(simbu)

    box_office.dispatch("New offer from Gautham Vasudev Menon")

    box_office.remove_subscriber(simbu)
    box_office.dispatch("Another offer from Gautham Vasudev Menon")
