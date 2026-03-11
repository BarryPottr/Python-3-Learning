# Rather than making a bunch of individual variables to store data, we can store them all in one list to simplify our code
studentNames = ["Cooper", "Rebecca", "CJ", "Kendra", "Chully", "Mallory", "Erica", "Hailey", "Trenton", "Michael", "Garrett"]
print(studentNames, end="\n\n") # This will print all the student names but as a list, meaning within a set of brackets, and with commas
print(studentNames[4], end="\n\n") # This will print Chully

for name in studentNames:
    print(name)

print("\n")
studentNames.append("Carson") # We can use functions to append to a list
studentNames.remove("Garrett") # We can also use functions to remove from a list

for name in studentNames:
    print(name)

studentNames[10] = 5656 # You can change the data dynamically, including the type of data in an index

print("")
for name in studentNames:
    print(name)

# ---------------------------------------------------------------------------------------------------------------
# If you want to see other list functions: https://www.w3schools.com/python/python_ref_list.asp
#----------------------------------------------------------------------------------------------------------------

studentSet = {"Garrett", "Griffin", "Quinn"} # This is a Set

# While we can't print an individual value for a Tuple or Set, we CAN use a loop to iterate and print each value in a Tuple or Set
print("\n")
for name in studentSet:
    print(name)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

### Extending Lists ########################################################################################

a.extend(b) # You can extend a list with the extend() function. It can only take 1 argument
a.extend(c)
print(a)

# NOTE:
# extend() VS append()
# Append takes an item and inserts it as an item to the list. Extend takes a LIST, and inserts each item in the given list as items.
#
# a=[1,2,3]
# a.extend([4])
# will result in [1,2,3,4]
# a.append([4])
# will result in [1,2,3,[4]]
#
# The last item being a list containing 4, and not just 4. 