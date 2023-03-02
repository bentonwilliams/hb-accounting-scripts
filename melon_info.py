"""Print out all the melons in our inventory."""


from melons import *


def print_melon(name):
    """Print each melon with corresponding attribute information."""
    print(name.upper())
    print(f'price: {melon_prices[name]}')
    print(f'seedless: {melon_seedlessness[name]}')
    print(f'flesh_color: {melon_flesh_color[name]}')
    print(f'rind_color: {melon_rind_color[name]}')
    print(f'average_weight: {melon_average_weight[name]}')
    print('\n')

for name in melon_names:
    print_melon(name)
