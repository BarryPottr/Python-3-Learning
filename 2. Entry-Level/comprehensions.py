### List Comprehensions ########################################################################################

# NOTE: The two examples below are NOT comprehensions

#Example 1: Lets say we want to double each element in the "numbers" list...

numbers = [1, 2, 3, 4, 5]
doubled = []

for x in numbers:
    doubled.append(x * 2)

print(doubled)


# Example 2: What if we had a list of dictionaries, and we want the names from each dictionary?
people = [{'name': 'Cooper', 'age': 27, 'favorite_color': 'purple'}, {'name': 'Rebecca', 'age': 26, 'favorite_color': 'pink'}, {'name': 'Tricky', 'age': 5000, 'favorite_color': 'green'}]
names = []

for p in people:
    names.append(p['name']) # We use square brackets because we are looking up a value inside a dictionary. We only use curly braces when defining the dictionary (or for f-strings)

print(names)


# Now let's use comprehensions!
# Example 3: Let's take the code from Example 1. We can simplify it a ton with comprehensions...
numbers = [1, 2, 3, 4, 5]
double_comprehension = [x * 2 for x in numbers] # In this case, we can put it all in one line!
print(double_comprehension)


# Example 4: Let's apply this to Example 2's code...
people = [{'name': 'Cooper', 'age': 27, 'favorite_color': 'purple'}, {'name': 'Rebecca', 'age': 26, 'favorite_color': 'pink'}, {'name': 'Tricky', 'age': 5000, 'favorite_color': 'green'}]
names_comprehension = [p['name'] for p in people]
print(names_comprehension)



### Filtering with Comprehensions ########################################################################################

# Example 5: Let's say we want to filter out all the elements in the "numbers" list that are even...
numbers = [1, 2, 3, 4, 5]
odds = [x for x in numbers if x % 2 != 0] # "x for x" just means we aren't incrementing x in the loop
print(odds)


# Example 6: Let's say we want to filter out the names of all the people younger than 26 from the "peoples" list
people = [{'name': 'Cooper', 'age': 27, 'favorite_color': 'purple'}, {'name': 'Rebecca', 'age': 26, 'favorite_color': 'pink'}, {'name': 'Tricky', 'age': 5000, 'favorite_color': 'green'}]
old_people = [p['name'] for p in people if p['age'] > 26]
print(old_people)



### Dictionary Comprehensions ########################################################################################

# Example 7: Make a dictionary comprehension that copies the keys/values of d1 into d1_copy
d1 = {'a': 1, 'b': 2, 'c': 3}
d1_copy = {key: value for key, value in d1.items()} 
print(d1_copy)

# Syntax: 
# "key: value" is what we want the keys and values to be (Ex: key: value * 2 would multiply all the values by 2)
# "key, value" are the arguments for the For loop


# Like lists, we can filter by adding an If statement to the end of the comprehension
# Example 8: Filter out any values greater than 2
d2 = {'a': 1, 'b': 2, 'c': 3}
d2_updated = {key: value for key, value in d2.items() if value < 3}
print(d2_updated)



### CHALLENGE ########################################################################################

# GOALS:
# Part 1: Create a function called uppercase_keys(dictionary). Use comprehension to return a list of all the keys in uppercase
# Part 2: Create a function called squares_map(num). Takes a number (num) and multiplies all the squares up to that number. Go from a list to a dictionary

# Part 1

# Define our dictionary
lowercase = {'a': 1, 'b': 2, 'c': 3}

def uppercase_keys(dict):

    # Define our list, capitalize the key letters in the dictionary, and store them in the uppercase list
    return [letter.upper() for letter in dict.keys()]

print(uppercase_keys(lowercase))


# Part 2

def squares_map(number):

    # Define our dictionary, add num as key, and add num * num as value for said key
    return {num: num * num for num in range(1, number + 1)} # Because we are starting with a string, we don't say "for num, num" because we don't have keys and values. We only have elements

print(squares_map(20))