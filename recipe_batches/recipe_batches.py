#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
  # store results
    batches = []
    # loop through the ingredients
    for i in ingredients:
        # loop through the recipe
        for j in recipe:
            # check to see if our ingredients have everything the recipe needs
            if j not in ingredients:
                # if not retur zero
                return 0
            if j == i:
                # if the ingredients and recipe keys match then check to see if the recipe needs are greater than available ingredients
                if recipe[j] > ingredients[i]:
                  # if recipe needs more than available return zero
                    return 0
                  # else take the ingredients and divide them by the amount needed in the recipe
                else:
                  # store them in a variable
                    value = ingredients[i] // recipe[j]
                    # append them to the empty list and round down
                    batches.append(math.floor(value))
    # return the min number in the list as that will be the max number of batches available
    return min(batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
