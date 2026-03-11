### The Basics ########################################################################################

my_tuple = (1, 2, 3, 4, 5) # Tuple syntax
one_element_tuple = (1,) # One element tuples require the comma after the value



### Tuple Methods ########################################################################################

# count() counts how many times a value(s) appears in a tuple
lot_of_1s = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # There are 18 1s
print(f"There are {lot_of_1s.count(1)} 1s in the Tuple.")


# index() tells us what index a value appears for the first time in a tuple
lots_of_numbers = (1, 234, 3, 42, 75, 5, 5, 6, 12, 3, 4, 1, 7, 8, 9, 10, 123, 143, 5, 6, 55, 1000)
print(f"The first 55 in the tuple is at index {lots_of_numbers.index(55)}")



### Tuple Comprehension ########################################################################################

# To use tuples with comprehension, you'll need to convert the tuple to another collector type
# To convert from one type of collector (tuples, sets, lists) to another, we use the type's Contructor
# These constructors include:
#   - list()
#   - dict()
#   - tuple()
#   - set()

simple_tuple = ('a', 'b', 'c', 'd', 'e', 'f')

# Let's say we want to make each of these letters uppercase. Since we can't modify a Tuple, we'd need to store it in another collector type, like a list
upper_list = [letter.upper() for letter in simple_tuple]
print(upper_list)



### CHALLENGE ########################################################################################

# Part 1: Create a function called index_all(). The function will check for each index of a value, instead of just the first
# Part 2: Create an append() function to use with a tuple. HINT: It will create a new tuple
# Part 3: Create an insert() function to use with a tuple. It should insert the value at any chosen index in the tuple.  HINT: It will create a new tuple

# First, let's create an input function to have the user create the tuple (input -> list -> tuple). This will be used by all 3 parts
def create_tuple():
    
    # Explain the rules to the user
    print("Hello. You will be prompted to enter individual values to be stored inside a Tuple. Please enter these values ONE AT A TIME!")
    
    # Define variables for while loop
    user_input = ''
    input_list = []

    # While the user input doesn't equal 'q' or 'Q', continue looping
    while (user_input != 'q') or (user_input != 'Q'):
        user_input = input("Enter your input. To quit, enter \"q\" or \"Q\". ")
        if (user_input == 'q') or (user_input == 'Q'):
            break
        else:
            input_list.append(user_input)
    
    return tuple(input_list)


################## Part 1

# index_all() finds all the indexes in a tuple. This will be done by converting the tuple to a list, and finding each index
def index_all(user_tuple):
    
    # Convert the tuple to a list
    user_list = list(user_tuple)

    # Print the list, and ask the user which value we are looking for
    print(user_list)
    target_value = input("What value from your tuple are we looking for? If a string/char, be sure to spell it EXACTLY THE SAME! ")

    # Make an empty list to store the indexes in. The indexes will be tracked by the counter
    value_indexes = []
    counter = 0

    # Iterate through the list to find out which indexes the value appears at
    for value in user_list:
        if user_list[counter] == target_value: # If the current value of user_list is the target_value...
            value_indexes.append(counter) # Add that index (counter) to the value_index list
            counter += 1
        else:
            counter += 1
    
    return tuple(value_indexes) # Make value_index a tuple


################## Part 2
def append_tuple(user_tuple):

    # Convert the tuple to a list
    user_list = list(user_tuple)

    # Ask the user what we are appending
    append_value = input("What would you like to append to your tuple? ")
    user_list.append(append_value)

    # Convert the list back into a tuple
    return tuple(user_list)


################## Part 3
def tuple_insert(user_tuple):

    # Convert the tuple to a list
    user_list = list(user_tuple)

    # Ask the user what they want to insert
    insert_value = input("What do you want to insert into your tuple? ")
    print(f"\n Here is your tuple: {tuple(user_list)}\n") # Print tuple for the user's reference
    insert_index = int(input(f"What index do you want to insert {insert_value} at? Remember, 0 is the beginning of the tuple: "))

    # Insert insert_value at insert_index's index
    user_list.insert(insert_index, insert_value)

    return tuple(user_list)


### Call our functions
user_tuple = create_tuple() # Create the tuple
print("That's at index(es): ", index_all(user_tuple)) # Find the indexes of a specified value
print("The appended tuple is: ", append_tuple(user_tuple)) # Append the tuple
print("The tuple now looks like: ", tuple_insert(user_tuple)) # Insert a value at a chosen index