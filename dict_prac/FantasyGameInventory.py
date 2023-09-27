
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in inventory.items():
       print(v,k)
       item_total= item_total+int(v)
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
   print('Before updated:', inventory)
   for item in addedItems:
    #print(item)
    inventory.setdefault(item,0)
    inventory[item]=inventory[item]+1
   print('Updated Inventory:', inventory)
   return inventory
   
   

if __name__=='__main__':
  stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}  
  dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','axe','sword']
  inv = addToInventory(stuff, dragonLoot)
  displayInventory(inv)