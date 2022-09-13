from random import choice


def random_fruit():
    """Return a random fruit, forever"""

    while True:
        yield choice(["apple", "banana", "orange"])
