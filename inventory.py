
class Inventory:
  def __init__(self):
    self.inventory = {}

  def add_product(self, name, quantity):
    if name in self.inventory:
      self.inventory[name] += quantity
    else:
      self.inventory[name] = quantity

  def remove_product(self, name, quantity):
    if name in self.inventory:
      if self.inventory[name] >= quantity:
        self.inventory[name] -= quantity
      else:
        print("Not enough quantity in inventory.")
    else:
      print("Product not found in inventory.")

  def get_inventory(self):
    print("Inventory:")
    for name, quantity in self.inventory.items():
      print(f"{name}: {quantity}")

inventory = Inventory()
inventory.add_product("apple", 10)
inventory.add_product("banana", 5)
inventory.add_product("orange", 15)
inventory.get_inventory()
inventory.remove_product("banana", 3)
inventory.get_inventory()