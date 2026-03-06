### Positional, Keyword, and Mixed Arguments ########################################################################################

# Arguments can be broken into 2 types: Positional and Keyword. This matters when the function is called
def add(a, b, c, d, e, f):
    return a + b + c + d + e + f

print(add(a=1, b=2, c=3, d=10, e=7, f=9)) # These arguments that specify their value are "Keyword Arguments". The order does not matter, as long as the names are correct
print(add(1, 2, 3, 4, 5, 6)) # These arguments that do not specify their respective parameter, are "Positional Arguments". Their order DOES matter

# We can determine what kinds of arguments can be used at the function's call: ([positional args], / , [positional or keyword args], * , [keyword args])
def sub(a, b, c, /, d, e, *, f):
    return a - b - c - d - e - f
print(sub(1, 2, 3, f=4, d=10, e=9))
# NOTE: Positional args must ALWAYS be called before keyword args!

### Default Parameters ########################################################################################

# We can define "Default Parameters" in the function's definition
def repeat_string(s, number_of_times=1):
    return s * number_of_times

# Because we defined the default parameter, we can choose to omit a parameter for it at the function call. 
# In this case, the function will refer to the default parameter
print(repeat_string("hello"))
print(repeat_string("I hate Moash\n", number_of_times=10)) # We can also override the default value at the time of the function call

### Arbitrary Arguments and Keywords ########################################################################################

def add(*args, **kwargs): # *args = Arbitrary Args; **kwargs = Arbitrary Keyword Args
    print(kwargs)
    total = 0
    for x in args:
        total += x
    return total

print(add(1, 2, 3, 4, 5, 6, 7, a=1, b="Hello!", c=True))
print(add(1, 2))
print(1)

### Challenge ########################################################################################
print("\n\n\nChallenge Program Below:\n\n\n")

# Calculates numbers based on chosen arithmetic and numbers
def calc(math_type, *args):

    total = 0

    if math_type == "add":
        for x in args:
            total += x
        return total
    elif math_type == "subtract":
        for x in args:
            total -= x
        return total
    elif math_type == "multiply":
        for x in args:
            total *= x
        return total
    elif math_type == "divide":
        for x in args:
            total /= x
        return total

print("Add:", calc("add", 2, 3, 4))
print("Subtract:", calc("subtract", 2, 3, 4))
print("Multiply:", calc("multiply", 2, 3, 4))
print("Divide:", calc("divide", 2, 3, 4))