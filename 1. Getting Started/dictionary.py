studentGrades = {"Cooper": 80, "Rebecca": 100, "CJ": 64, "Kendra": 94, "Chully": 87, "Mallory": 70}
print(studentGrades)
print(studentGrades["CJ"]) # When calling on the dictionary, we use brackets

# We can also use a dictionary to hold multiple items for one person/thing
cooperGrades = {"English": 94, "Physics": 80, "Calculus": 70, "History": 100, "Drama": 94, "Seminary": 100}
print(cooperGrades["History"])

# Dictionaries can also be nested together in a list
gameNominees = ({"Game": "Baldur's Gate 3", "Developer": "Larian Studios", "Release Year": 2023, "Platform": "PC - Steam"},
           {"Game": "Tears of the Kingdom", "Developer": "Nintendo", "Release Year": 2023, "Platform": "Nintendo Switch"},
           {"Game": "Spider-Man 2", "Developer": "Insomniac", "Release Year": 2023, "Platform": "PS5"},
           {"Game": "Super Mario Bros. Wonder", "Developer": "Nintendo", "Release Year": 2023, "Platform": "Nintendo Switch", "Rating": ("E", "PEGI 3")}) # Notice how we have a list within our dictionary
print(gameNominees[1]) # This will print all of the second dictionary, which is Tears of the Kingdom
print(gameNominees[1]["Developer"]) # We can dive even deeper into what we call from our dictionary
print(gameNominees[3]["Rating"][1], end="\n\n") # We can call on our rating list within dictionary 3 by adding another bracket to our print() statement. This should print "PEGI 3"

# ---------------------------------------------------------------------------------------------------------------
# Working with dictionaries
#----------------------------------------------------------------------------------------------------------------

# This will print each item in the list
for item in cooperGrades:
    print(cooperGrades[item]) 

# We can also check if a key is in a list
print("")
if "History" in cooperGrades:
    print(f"Yes, History is in cooperGrades, and he has a {cooperGrades["History"]} in it.")

# ---------------------------------------------------------------------------------------------------------------
# Dictionary Lists
#----------------------------------------------------------------------------------------------------------------

# We can also check if a value is in a list, but this will return a Dictionary Values List, which isn't a true dictionary or list. It's a dictionary list
print("")
if 100 in cooperGrades.values():
    print("Yes, Cooper has a 100 in History and Seminary.")

print("")
print(cooperGrades.values()) # This should return "dict_values([94, 80, 70, 100, 94, 100])". This is a dictionary list

values = cooperGrades.values() # If we tried to assign the dictionary list to a variable, it WILL assign the dict_list to the variable
# print(values[1]) # But we can't call on the individual indexes in the list because it's not a true list
valuesList = list(values) # HOWEVER, we can use the list() function to cast/convert the dict_list into a normal list
print("")
print(valuesList[1], end="\n\n") # This should return 80

# The same can be done with keys. We'd get a dict_keys list, but we can cast it into an actual list
keys = cooperGrades.keys()
keysList = list(keys)
print(keysList[1], end="\n\n") # This should print "Physics"

# This is a bit complicated, but is here to show what you could do while iterating through a list and dictionary together
# This will iterate through each index of keyList, to iterate through each key in the cooperGrades dictionary
for i in range (0, len(values)):
    print(cooperGrades[keysList[i]])

items = cooperGrades.items() # This will produce a dict_items list
print(items)

itemsList = list(items) # This will turn the dict_items list into an actual List of Lists
print(itemsList[0]) # This will print "('English', 94)"
print(itemsList[0][0]) # This will print the 0th value in the itemsList List of Lists: English