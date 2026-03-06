# Using break control statements
for x in range(0,10):
    print("Value of x:", x)
    answer = input("Press y then enter to END: ")
    if answer == "y":
        break

print("End of line for BREAK loop")

x = 10
y = 20

while x < y:
    print("Value of x:", x)
    answer = input("Press y then enter to CONTINUE: ")
    if answer == "y":
        continue

    if answer == "x":
        # Do some code in the future here
        pass # Pass lets the program continue, even if this part of the program does nothing

    x += 1
else:
    print("The whole loop ran.") # This only runs if the loop reaches its natural conclusion

print("End of line for CONTINUE loop")