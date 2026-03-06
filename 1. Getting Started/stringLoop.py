# Demonstrate that each letter in a string is an individual character
myName = "Cooper"
print(id(myName))

# Iterate through each letter in myName, and print the letter
for letter in myName: 
    print(letter)

# This is an error and not allowed because strings are immutable, meaning they cannot be changed
# myName[2] = "q"

myName = "Pooper" # Really, this has just created a new variable, as can be seen by the variable IDs
name2 = "Pooper" # However, because myName and name2 have the same string literal, they will both have the same ID to save on memory
print(id(myName))
print(id(name2))