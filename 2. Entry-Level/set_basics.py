### The Basics ########################################################################################

my_numbers = {2, 3, 5, 7, 11, 13, 17, 19} # This is a set

empty_set = set() # This is an empty set. Empty sets must be defined with set()

# The values within a set must be unique. It will not count duplicates
another_set = set([1, 2, 3, 4, 5, 5, 5])
print(another_set)



### Methods ########################################################################################

# You can add items to a set with add(). NOTE: This does not necessarily add it to the end (REMINDER: sets aren't ordered), it just adds it somewhere
my_numbers.add(5656)
print("Add:", my_numbers)

# remove() removes the item from the set, but throws an error if the item isn't in the set
# my_numbers.discard('One Piece')

# discard() removes the item from the set, and just moves on if the item doesn't exist in the set
my_numbers.discard(5656)
my_numbers.discard('One Piece')
print("Discard:", my_numbers)

# clear() clears all the elements from a set
my_numbers.clear()
print("Clear:", my_numbers)



### Operators ########################################################################################

prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19}
even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

# The union "|" operator combines two sets into one (makes a new set)
union = prime_numbers | even_numbers
print("The union of prime_numbers and even_numbers is:", union)

# The intersection operator "&" only shows the elements in both/all sets
intersection = prime_numbers & even_numbers
print(f"The intersection of prime_numbers and even_numbers is {intersection}")

# The difference operator "-" leaves us with everything in set 1 that wasn't in set 2 (3, 4, 5, etc.)
difference = prime_numbers - even_numbers
print(f"The difference between prime_numbers and even_numbers is {difference}")

# The symmetric difference operator "^" leaves us with all the elements in set 1 *and* 2 (and 3, 4, 5, etc.) that aren't in both/all
symm_diff = prime_numbers ^ even_numbers
print(f"The symmetric difference between prime_numbers and even_numbers is {symm_diff}")



### CHALLENGE ########################################################################################
print("\n\n\nCHALLENGE TIME\n\n")
# GOALS: Use dictionaries behind the scenes
# Part 1: create_set(list): Take list as argument, and return a dictionary REPRESENTING the set (turn the values from the list into keys)
# Part 2: add_to_self(create_set_dict, new_value): Take dictionary from create_set() and add new value to self
# Part 3: discard_from_set(add_to_self_dict, value_to_remove): Remove value from dictionary. 
#   REQUIREMENT: Use the "In" keyword to see if something is in the dictionary

# Part 1

my_list = [1, 2, 3, 4, 5]

def create_set(l):
    
    # Iterate through list (l) and build dictionary from it
    my_dict = {num: True for num in l}

    return my_dict


# Part 2:

def add_to_self(d):
    
    # Ask the user what value we are adding to the "set"
    val = input("What would you like to add to your set?: ")

    # Update the dictionary with a key named after the user's input, and give it a value of True
    # d.update({val: True})
    d[val] = True

    return d


# Part 3:

def discard_from_set(d):

    # Ask the user what value we are discarding
    print(f"Your set is: {d.keys()}")
    val = int(input("What element would you like to remove from your set (Enter a number): "))

    # See if val is in the dictionary. If so, remove it. If not, prompt the user to choose an "element" in their "set"
    if val in d:
        del d[val] # Use del to delete the key in the dictionary
    else:
        print("That doesn't exist in your set. Good thing we are using discard() instead of remove()!")

    return d

my_set = create_set(my_list)
updated_set = add_to_self(my_set)
print(discard_from_set(updated_set))