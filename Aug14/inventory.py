inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'],
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
 }

#Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']+=50

print inventory
