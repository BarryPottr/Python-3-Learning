data = { 'a': 1, 'b': 2, 'c': 3}

for keys in data:
    print(f"{keys} is a key, and {data[keys]} is its value.")

# There are easier ways to do this ^^^

print(data.keys()) # Returns a list of all the keys the dictionary contains

# This can also be done with values
print(data.values())

# We can also get both at the same time, known as an item
print(data.items()) # This prints Tuples

### Merging Dictionaries ########################################################################################

# You can update dictonaries with the .update() method
dict_one = {'a': 1, 'b': 2, 'c': 3}
print(f"Dictionary One is: {dict_one}")
dict_one.update({'c': 10, 'd': 5, 'e':'Marathon'})
print(f"The update dictionary One is: {dict_one}")

# You could also update a dictionary with another
cooper_facts = {'name': 'Cooper', 'age': 27, 'hair_color': 'brown', 'favorite_game': 'Tears of the Kingdom'}
rebecca_facts = {'name': 'Rebecca', 'age': 26, 'hair_color': 'brown'}

cooper_facts.update(rebecca_facts) # This will overwrite cooper_facts with the items from rebecca_facts because they share the same keys. Notice how 'favorite_game' remains from cooper_facts
print(cooper_facts)

# Here's a more practical example
kadeon_facts = {'species': 'Gold Dragon', 'age': 4500, 'size': 'Gargantuan', 'status': 'Alive'}
changes = {'age': 'Over 5000', 'status': 'Unknown'}

kadeon_facts.update(changes)
print(kadeon_facts)