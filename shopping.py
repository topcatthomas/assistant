def addToList(shoppingList, name):
    try:
        shoppingList.append(name)
    except:
        shoppingList = []
        shoppingList.append(name)
    return shoppingList
def clearShoppingList(shoppingList):
    del shoppingList
    shoppingList = []
    return shoppingList
