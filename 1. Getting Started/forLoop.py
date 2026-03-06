# Gather input from the user, and turn the str input into an int
x = int(input("Please enter the value for x: "))
y = int(input("Please enter the value for y: "))

# If x isn't less than y, loop for new inputs until x is less than y
while x >= y:
    print("x must be less than y. Try again.")
    x = int(input("Please enter the value for x: "))
    y = int(input("Please enter the value for y: "))

# Use a For loop to print the value of x, and increase by one
for i in range (x,y):
    print("This is the current value of x:", x)
    x += 1

print("The loop has completed. End of line.")

names = ["Cooper", "Rebecca", "CJ", "Kendra", "Chully", "Mallory", "Hailey", "Trenton", "Michael", "Erica", "Garrett"]

for name in names:
    print("Name is:", name)