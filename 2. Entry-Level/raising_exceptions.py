#######################################################
# RAISING EXCEPTIONS
#######################################################

# Repeat a string a number of times equal to the amount specified by the user
def repeat_string(s, number_of_times=1): # number_of_times=1 is a default value if no argument is passed for it when the function is called

    # We need raised exceptions to account for the user not entering a string or a number
    if type(s) is not str:
        raise TypeError(f'Arg 1 should be a string', {'arg_number': 1, 'should_be_type:': str, 'received': s}) # In this example, we add on additional arguments to the TypeError exception, so we can pass this information in our exception messages later
    
    if type(number_of_times) is not int:
        raise TypeError(f'Arg 2 should be an int', {'arg_number': 2, 'should_be_type:': int, 'received': number_of_times}) 

    return s * number_of_times

# We can prevent our raised exceptions from crashing the program by using a try-except block with it.
# Because we used the same exception type (TypeError) from our function as in our except-block, if one  
# of the raised exceptions is triggered, it will be reflected in our except-block's exception message
try:
    print(repeat_string('wow ', 10))
except TypeError as e:
    if 'Arg 1' in str(e): # str(e) will be our triggered raised exception message because our except-block and the exception type are the same
        print(f'It looks like you messed up argument 1. You entered {e.args}')
        print(f'Error is {type(e)}') # You can also print the type of exception
    elif 'Arg 2' in str(e):
        print(f'It looks like you messed up argument 2. You entered {e.args}') # We can also print the arguments passed with the exception (TypeError in this case)
        print(f'Error is {type(e)}') # You can also print the type of exception

#######################################################
# ELSE & FINALLY BLOCKS
#######################################################

# The else and finally blocks will be continuations of our repeat_string() program above
else:
    print('This is the else block') # Good for "safe" code that isn't likely to cause any errors or exceptions
finally:
    print('The program is ending, goodbye!') # This will print, even if we changed the except statement to a ValueError (repeat_string() won't give us a ValueError), and caused the program to hard crash. It will print the finally block before the error statement

# Think of the different blocks like this:
# - Try: Meant for "dangerous" code that's potentially going to cause an error or exception
# - Except: Meant for handling errors or exceptions
# - Else: Meant for "safe" code that isn't likely to cause an error or exception
# - Finally: Meant to be run at the end of the program/section NO MATTER WHAT

#######################################################
# CHALLENGE
#######################################################

# GOAL:
# 1) Write an "except Exception:" block that behaves like a more complex series of except statements

try:
    raise TypeError('Oh no, our program, it\'s broken!')
except Exception as e:
    if type(e) is TypeError:
        print(f'{e} It\'s a TypeError!')
    if type(e) is ValueError:
        print(f'{e} It\'s a ValueError')