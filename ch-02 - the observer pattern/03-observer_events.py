from collections import defaultdict


class Publisher(object):
    def __init__(self):
        # Dict for events
        self.events = defaultdict(dict)

    def add_subscriber(self, event, subscriber, callback=None):
        if callback is None:
            callback = subscriber.update
        self.events[event][subscriber] = callback
        print(f"** {subscriber.name} subscribed to {event} **")

    def remove_subscriber(self, event, subscriber):
        self.events[event].pop(subscriber)
        print(f"** {subscriber.name} unsubscribed to {event} **")

    def dispatch(self, event, payload):
        for subscriber, callback in self.events[event].items():
            callback(payload)


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

    box_office.add_subscriber("offers", dhanush)
    box_office.add_subscriber("offers", vijay_sethupathi)
    box_office.add_subscriber("offers", simbu)

    box_office.dispatch("offers", "OFFER: New offer from Gautham Vasudev Menon")

    box_office.remove_subscriber("offers", simbu)
    box_office.dispatch("offers", "OFFER: Another offer from Gautham Vasudev Menon")

    box_office.add_subscriber("gossip", simbu)
    box_office.dispatch(
        "gossip", "GOSSIP: There's another Enthiran movie coming!"
    )
