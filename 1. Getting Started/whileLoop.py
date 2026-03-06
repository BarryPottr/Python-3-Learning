# Gather input from the user, and turn the str input into an int
x = int(input("Please enter the value for x: "))
y = int(input("Please enter the value for y: "))

# If x isn't less than y, loop for new inputs until x is less than y
while x >= y:
    print("x must be less than y. Try again.")
    x = int(input("Please enter the value for x: "))
    y = int(input("Please enter the value for y: "))

# Print the value of x, and increase by 1
while x < y:
    print("The current value of x is", x)
    x += 1

print("The loop has completed. End of line.")