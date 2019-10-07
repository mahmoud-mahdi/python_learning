def cakes(recipe, available):
    number_of_cakes_list = []
    for element in recipe.keys():
        if element not in available.keys():
            availabel_item = 0
        else:
            availabel_item = available[element]
        number_of_cakes_list.append(availabel_item // recipe[element])
    return min(number_of_cakes_list)

def cakes_perfect(recipe, available):
  return min(available.get(k, 0)/recipe[k] for k in recipe)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
