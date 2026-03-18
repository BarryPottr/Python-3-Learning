### The Basics ########################################################################################

# This is a 2D Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# To print, we use 2 square brackets
print(f"The value of matrix[1][0] is {matrix[1][0]}") # This will print "4"

# We can make finding the values a little easier by butting the rows into variables
first_row = matrix[0]
print(f"The value of first_row[1] is {first_row[1]}") # This will print "2"

# We can change the value of an element in the matrix
matrix[2][2] = 9000 # This changes the value of 9 to 9000
print(f"matrix[2][2] was 9, but is now {matrix[2][2]}")



### Looping Through Multi-Dimensional Lists ########################################################################################

# You'll generally need as many nested For loops as dimensions in the list
def looping_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end=' ')
        print()

looping_matrix(matrix)

# We can use comprehension to simplify the above For loop
comp_matrix = [[x * 2 for x in row] for row in matrix]
print(comp_matrix)



### Tuples, Dictionaries, and Sets as Matrices ########################################################################################

# Tuples
tuple_matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Good for adding rows, but not columns
list_tuple_matrix = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
]

# Good for adding columns, not rows
tuple_list_matrix = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

tuple_list_matrix[0].append(4)
tuple_list_matrix[1].pop(0)

print(tuple_list_matrix)

# Dictionary
matrix_dictionary = {
    'a': {1: 'first', 2: 'second', 3: 'third'},
    'b': {4: 'fourth', 5: 'fifth', 6: 'sixth'},
    'c': {7: 'seventh', 8: 'eighth', 9: 'ninth'}
}

print(f"The value of matrix_dictionary['a'][2] is {matrix_dictionary['a'][2]}") # This prints "second"

# Sets
my_set = {
    frozenset([1, 2, 3]),
    frozenset([4, 5, 6]),
    frozenset([7, 8, 9])
}

looping_matrix(my_set)

###########################################################################################
# CHALLENGE
###########################################################################################

# GOALS:
# 1) Make min_matrix() and max_matrix() functions that do the same thing as min)_ and max(). Find the min/max values in a matrix
#   1.5) Use comprehension in the for loop
# 2) Make a len)matrix() function that finds how many elements are in the matrix
# 3) Make a transpose_matrix function that does the same thing as the transpose() function on a matrix

challenge_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

###
# PART 1
###

# Find the minimum value in a matrix
def min_matrix(c_mat):
    
    # Find the minimum value of the matrix
    min_value = min([min(row) for row in c_mat])
            
    print(f"The minimum value in challenge_matrix is {min_value}.")

def max_matrix(c_mat):

    max_value = c_mat[2][2]

    # Find the maximum value of the matrix
    for row in c_mat:
        for x in row:
            if x >= max_value:
                max_value = x

    print(f"The maximum value in challenge_matrix is {max_value}.")

###
# PART 2
###

def len_matrix(c_mat):

    length = sum(1 for row in c_mat for x in row)

    print(f"The length of challenge_matrix is {length}.")


###
# PART 3
###

def transpose_matrix(c_mat):

    # Define our rows and columns
    total_rows = len(c_mat)
    total_cols = len(c_mat[0])

    # Define our transposed_matrix variable to avoid index errors
    transposed_matrix = [[0 for _ in range(total_rows)] for _ in range(total_cols)]

    for row in range(total_rows):
        for col in range(total_cols):
            transposed_matrix[col][row] = c_mat[row][col] 

    print(transposed_matrix)



min_matrix(challenge_matrix)
max_matrix(challenge_matrix)
len_matrix(challenge_matrix)
transpose_matrix(challenge_matrix)