# A great example of a recursive process is a factorial
# Below is an example of a factorial function with a for loop
def factorial(number):
    final = 1 # The end of the factorial multiplication
    for i in range(number, 0, -1): # We end at index -1, which is 0)
        final = final * i
    return final

print(factorial(6))


# Below is an example of the factorial function as a recursive function
def factorialRecur(number):
    if number == 1:
        return number
    else:
        return number * factorialRecur(number - 1) # This is the actual multiplication. We don't store the multiplied value, we just output it. The only thing changing is "number"

print(factorialRecur(7))