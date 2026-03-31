# PEP8 says indentation should be 4 spaces within a block
def my_function():
    print("This is 4 spaces")


# This line is 79 characters long, which honestly isn't a lot of room to use..


def my_second_function():
    pass


# This is another comment

my_list = [1, 2, 3, 4, 5] # This is the correct syntax for lists

# You can space your list elements on individual lines
my_strings = [
    'Hello',
    'Howdy',
    'Hola', # You need to make sure the last element has a comma after it
]

my_tuple = (1,) # Tuples have the same rules as lists

# PEP8 says that each element of a dictionary should be defined on a separate line
my_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
}

#####################################################################
# CHALLENGE
#####################################################################

# GOAL: Fix the code below to follow PEP8 guidelines

def my_function(a, b):
    print("Hello, world!")

    my_list = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        12, 13, 14, 15, 16, 17, 18, 19, 20,
        ]
    
    another_list = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    my_dict = {
       'key1': 1,
       'key2': 2,
       'key3': 3,
       'key4': 4,
       'key5': 5,
       'key6': 6,
       'key7': 7,
       'key8': 8,
       'key9': 9,
       'key10': 10,
       }
    
    result = a + b
    
    if result > 10:
        print("Result is greater than 10")

    if result <= 10: 
        print("Result is 10 or less")

    return result


def another_function(x, y, z):
    sum = x + y + z
    print("Sum: ", sum)

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(i, end=' ')

    print()


long_string = "This is a very long string that is just way too long and adds"
+ " that annoying horizontal scroll bar to the bottom of the screen, which"
+ "  I'm not too crazy about"
my_function(1, 2)
another_function(1, 2, 3)