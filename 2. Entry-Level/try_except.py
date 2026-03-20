#######################################################
# TRY-EXCEPT BLOCKS
#######################################################

user_input = input('Please enter a number: ')

try:
    number = int(user_input) # If the exception occurs here, the rest of the try-block underneath would be skipped, and the program would move to the exception
    print(f'The number you entered plus 1 is {number + 1}')
except ValueError:
    print('You must enter a NUMBER.')

user_input_2 = input('Please enter a second number: ')

try:
    number = int(user_input_2)
    print(f'The number you entered minus 1 is {number - 1}')
except ValueError:
    print('That isn\'t a number.')

#######################################################
# HANDLING MULTIPLE EXCEPTIONS
#######################################################

user_input = input('Please enter a number: ')

try:
    number = int(user_input) # If the exception occurs here, the rest of the try-block underneath would be skipped, and the program would move to the exception
    print(f'The number you entered plus 1 is {number + "1"}')
except ValueError:
    print('You must enter a NUMBER.')
except TypeError: # You typically need as many except-blocks as exceptions you might encounter
    print('Looks like the program made an oopsie whoopsie')

user_input_2 = input('Please enter a second number: ')

try:
    number = int(user_input_2)
    print(f'The number you entered minus 1 is {number - 1}')
except Exception: # "Exception" is a generic, catch-all exception
    print('Something went wrong')

# NOTE: Having except-blocks can be useful in troubleshooting programs or identifying what specifically caused an exception in a program

#######################################################
# CHALLENGE
#######################################################

# GOALS:
# 1) Create a simple program that asks the user for 2 numbers, and add them. If the user doesn't enter a number, go back and ask for the input until you get a number
# 2) Create a function called input_number() that takes the functionality from step 1's looping number prompt, and keeps asking the user for a number

#####
# Step 1
#####
print('\nChallenge time!\n\n\n')
input_1 = input('Please enter your first number: ')
first_number_valid = False

while not first_number_valid:
    try:
        input_1 = int(input_1) # See if input_1 is an int
        first_number_valid = True
    except ValueError:
            print('\nYou FOOL. The first number you entered is not a number. That\'s something else!')
            input_1 = input('\nPlease enter your first number: ')
            
    
    # NOTE: I revised this section after watching the instructor demonstrate using a while loop before the try-except block
    #while not isinstance(input_1, int): # If input_1 isn't an int, then loop until we get an int
        #print('\nYou FOOL. The first number you entered is not a number. That\'s something else!')
        #input_1 = input('\nPlease enter your first number: ')
        #try:
            #input_1 = int(input_1)
        #except ValueError:
            #continue

input_2 = input('\nPlease enter your second number: ')
second_number_valid = False

while not second_number_valid:
    try:
        input_2 = int(input_2) # See if input_2 is an int
        print(f'\nThe sum of {input_1} and {input_2} is {input_1 + input_2}')
        second_number_valid = True
    except ValueError:
            print('\nYou FOOL. The second number you entered is not a number. That\'s something else!')
            input_2 = input('\nPlease enter your second number: ')

    # NOTE: I revised this section after watching the instructor demonstrate using a while loop before the try-except block
    #while isinstance(input_1, int): # If input_2 isn't an int, then loop until we get an int
        #print('\nYou FOOL. The second number you entered is not a number. That\'s something else!')
        #input_2 = input('\nPlease enter your second number: ')
        #try:
            #input_2 = int(input_2)
            #break
        #except ValueError:
            #pass

    #print(f'\nThank you for entering an int. The sum of {input_1} and {input_2} is {input_1 + input_2}')

#####
# Step 2
#####
print("\n\n\nNow we do it in a function!")

def input_number(prompt):
     while True:
        try:
            user_input = input(prompt)
            x = int(user_input)
            return x
        except ValueError:
            print('\nYou FOOL. That\'s not a number!')

num_1 = input_number("\nEnter the first number: ")
num_2 = input_number("\nEnter the second number: ")

print(f'The sum of those numbers is {num_1 + num_2}')