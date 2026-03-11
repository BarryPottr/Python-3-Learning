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


lowercase = {'1': 'a', '2': 'b', '3': 'c'}
uppercase = {'4': 'A', '5': 'B', '6': 'C'}

combinedCase = lowercase | uppercase # We can merge dictionaries with the | operator. If they keys are the same, the second dictionary will overwrite the first

print(combinedCase)

allDictionaries = lowercase | uppercase | kadeon_facts | changes # We can mergee multiple dictionaries into one

print(allDictionaries)

### Copying Dictionaries ########################################################################################

master_dict = {'a': 1, 'b': 2, 'c': 3}
copied_dict = master_dict.copy() # If we want to copy a dictionary, we can use the .copy() function
print(copied_dict)

# NOTE: Saying copied_dict = master_dict doesn't give copied_dict the value of master_dict. THIS IS NOT A VALID WAY TO COPY!

### Setting Defaults ########################################################################################

# You can set default individual keys with .setdefault()
cooper_facts = {'name': 'Cooper', 'age': 27, 'hair_color': 'brown', 'favorite_game': 'Tears of the Kingdom'}
defaults = {'name': 'N/A', 'age': 0, 'hair_color': 'N/A', 'favorite_game': 'N/A', 'favorite_movie': 'N/A', 'favorite_show': 'N/A', 'favorite_color': 'N/A'}

cooper_facts.setdefault('name', 'N/A') # If we set a default key/value for one the dictionary already has, nothing will happen. This does NOT overwrite what already exists in the dictionary
cooper_facts.setdefault('religion', 'N/A') # If we set a default key/value that does NOT exist in the dictionary, it will append this default value to the end of the dictionary

print(cooper_facts)

print(defaults)
print(cooper_facts)
print(defaults | cooper_facts) # We can print over the defaults by putting it as the first dictionary in the merge call



### CHALLENGE ########################################################################################

# GOAL: Use dictionaries to count how many times certain characters appear in a string
# PLAN: 
#   1) Get string input from user
#   2) Loop through the string, and give each character a key in a dictionary if it doesn't already exist in the dictionary
#   3) Increase the count of the key if it's character appears
#   4) Print the number of times each character appears as long as its count (value) isn't 0

user_string = input("Enter the string we will count character's for: ") # Get the user's string

# Count how many times each character appears in a string, and store the count in a dictionary. Skip space characters.
def character_count(string):

    counter = 0 # Define our variable for character counting

    appearance_count = {} # Define our dictionary

    # Iterate through each character in a string
    for char in string:
        if char in appearance_count: # See if the character exists as a key in the dictionary
            appearance_count[char] += 1
        elif char == ' ': # If the character is a space, don't add it to the dictionary
                continue
        else: # If it's the character's first time appearing in the string, set it's value as 1 to be iterated upon later
            counter = 1
            appearance_count[char] = counter
    
    return appearance_count

appearances = character_count(user_string)
print("\nThese characters appear this many times in your string:")
for keys in appearances:
    print(f"{keys}: {appearances[keys]}")



### CHALLENGE 2 ########################################################################################

# GOAL: Remake the program from challenge 1, but use dictionary merging and defaults

user_string = input("Enter the string we will count character's for: ") # Get the user's string

# Count how many times each character appears in a string, and store the count in a dictionary. Skip space characters.
def character_count(string):

    appearance_count = {} # Define our dictionary

    # Iterate through each character in a string
    for char in string:
        if char == ' ':
            continue
        else:
            appearance_count.setdefault(char, 0) # Set a default value to add the character to the dictionary
            update = {char: appearance_count.get(char, 0) + 1} # .get() gets the value of the key. In this case, we get the value of char's key, and then increment it by 1
            appearance_count = appearance_count|update # Update appearance count (which currently has defaults) with the values in update

    return appearance_count

appearances = character_count(user_string)
print("\nThese characters appear this many times in your string:")
for keys in appearances:
    print(f"{keys}: {appearances[keys]}")