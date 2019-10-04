#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Cannon']


def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        name = ADJECTIVES[randint(0, 4)] + ' ' + NOUNS[randint(0, 4)]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        products.append(Product(name, price, weight, flammability))
    return products

def inventory_report(products):
    names = set(list(i.name for i in products))
    avg_price = sum(i.price for i in products) / len(products)
    avg_weight = sum(i.weight for i in products) / len(products)
    avg_flammability = sum(i.flammability for i in products) / len(products)
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT\n" +
          f"Unique product names: {len(names)}\n" +
          f"Average price: {avg_price}\n" +
          f"Average weight: {avg_weight}\n" +
          f"Average flammability: {avg_flammability}\n")



# if __name__ == '__main__':
#     inventory_report(generate_products())
