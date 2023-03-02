"""Print out all the melons in our inventory."""


from melons import *


def print_melon(name):
    """Print each melon with corresponding attribute information."""
    print(f'{name.upper()}')
    attributes=sorted(melons[name])
    for attribute in attributes:
        print(f'{attribute}: {melons[name][attribute]}')
    print()

for name in melons:
    print_melon(name)
