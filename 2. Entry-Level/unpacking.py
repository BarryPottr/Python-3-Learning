### Unpacking Lists ########################################################################################

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

# What if we wanted a new list including the values from a, b, and c, but we wanted some values in-between a, b, and c's values?
# We could use the unpacking operator *[list_name]

d = [0, *a, 100, 2000, 420, *b, -100, 21, *c, 99] # Unpacking allows us to easily add other lists to a new one in the middle of the list

print(d) # This will print [0, 1, 2, 3, 100, 2000, 420, 4, 5, 6, -100, 21, 7, 8, 9, 99]

### Unpacking Dictionaries ########################################################################################

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5, 'f': 6}
d3 = {'a': 100, 'c': 345, 'f': 0}

# To unpack dictionaries, you'd use **[dictionary_name]. It will still overwrite values if any keys are shared between dictionaries
d4 = {**d1, **d2, **d3} # This will overwrite a, c, and f with the values from d3
print(d4)

d5 = {'alpha': 100, 'bravo': 'Wow, the land of make believe!', **d1, 'charlie': 30, **d2, 'delta': 55}
print(d5)



### CHALLENGE ########################################################################################

# GOALS:
# Part 1: Create a function called reverse_halves(list). Take a list, and slice it in half. Put the second half before the first half
# Part 2: Create a function called apply_defaults(dictionary, default dictionary). Return a new dictionary where the defaults have been applied to the first dictionary

# Part 1

# Define our list
even_list = [1, 2, 3, 4, 5, 6]
odd_list = [1, 2, 3, 4, 5, 6, 7]

def reverse_halves(list):

    # Define our midpoint
    midpoint = len(list) // 2

    # Slice the list into two strings
    first_half = list[:midpoint] # The colons define the start or end of the list
    second_half = list[midpoint:]

    # Return list with last half and then first half
    return [*second_half, *first_half]

print(reverse_halves(even_list))
print(reverse_halves(odd_list))


# Part 2

# Define our dictionary
my_dictionary = {'a': 1, 'b': 2, 'c': 3}

def apply_defaults(dict):

    # Define our default dictionary
    default_dict = {'d': 10, 'e': 61, 'c': 0}

    # Apply the default dictionary's values to the dictionary
    return {**dict, **default_dict}

print(apply_defaults(my_dictionary))