class Item(object):
    def __init__(self, name, value, quantity=1):
        self.name = name
        self.raw = name.strip().lower()
        self.quantity = quantity

        self.value = value
        self.netValue = quantity * value

    def recalc(self):
        self.netValue = self.quantity * self.value


class Container(object):
    def __init__(self, name):
        self.name = name
        self.inside = {}

    def __iter__(self):
        return iter(self.inside.items())

    def __len__(self):
        """Retourne le nombre d'items présent dans l'inventaire"""
        return len(self.inside)

    def __contains__(self, item):
        return item.raw in self.inside

    def __getitem__(self, item):
        return self.inside[item.raw]

    def __setitem__(self, item, value):
        self.inside[item.raw] = value
        return self[item]

    def add(self, item, quantity=1):
        if quantity < 0:
            raise ValueError("Negative quantity. Use remove() instead")

        if item in self:
            self[item].quantity += quantity
            self[item].recalc()
        else:
            self[item] = item

    def remove(self, item, quantity=1):
        if item not in self:
            raise KeyError("Item not in container")
        if quantity < 0:
            raise ValueError("Negative quantity. Use add() instead")

        if self[item].quantity <= quantity:
            del self.inside[item.raw]
        else:
            self[item].quantity -= quantity
            self[item].recalc()


backpack = Container("Backpack")

sword = Item("Sword", 10)
gold = Item("Gold Coin", 1, 50)
potion = Item("Potion", 5)

backpack.add(sword)
backpack.add(gold)
backpack.add(potion)


def purchase(*items):
    for item in items:
        if item.value > backpack[gold].quantity:
            print("You don't have enough money !")
            print(f"Come back when you have {item.value} mode gold")
        else:
            backpack.remove(gold, item.value)
            backpack.add(item)
            print(f"You purchased a '{item.name}'")

print(backpack[gold].quantity)
purchase(sword, potion)
print(backpack[gold].quantity)