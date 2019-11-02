from random import randint, sample, uniform
from acme import Product
import pandas as pd
# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome ', 'Shiny ', 'Impressive ', 'Portable ', 'Improved ']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """
    Generates a dataframe of random products, with random weights, prices, etc.
    """
    products = []
    price = []
    weight = []
    flammability = []
    for i in range(num_products):
        i = random.choice(ADJECTIVES)
        k = random.choice(NOUNS)
        products.append(i + k)
        price.append(randint(5, 101))
        weight.append(randint(5, 101))
        flammability.append(uniform(0.0, 2.5))

    df = pd.DataFrame(list(zip(products, price, weight, flammability)),
                      columns=['name', 'price', 'weight', 'flammability'])
    return df


def inventory_report(products):
    """
    Gives a nice inventory report of the items generated above.
    """
    from collections import Counter
    from statistics import mean
    unique_names_count = sum(Counter(products['name']).values())
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names: " + str(unique_names_count))
    print("Average price: " + str(mean(products['price'])))
    print("Average weight: " + str(mean(products['weight'])))
    print("Average flammability: " + str(mean(products['flammability'])))


if __name__ == '__main__':
    inventory_report(generate_products())
