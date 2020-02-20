#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = []
    for i in ingredients:
        for j in recipe:
            if j not in ingredients:
                return 0
            if j == i:
                print(j, recipe[j], i, ingredients[i])
                if recipe[j] > ingredients[i]:
                    return 0
                else:
                    value = ingredients[i] // recipe[j]
                    # print(math.floor(value))
                    batches.append(math.floor(value))

    return min(batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
