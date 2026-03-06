name1 = "Ben"
name2 = "Finkle"

fullName = name1 + " " + name2

print(fullName)

textValue = "Hello there!"
textValue *= 5
print(textValue)

textValue = "Hello there!"
textValue = textValue[3]
print(textValue)

textValue = "Hello there!"
textValue = textValue[0:5]
print(textValue)

#------------------------------------------------------------------
# Chapter 7 "Operators and String Functions" begins here...
#------------------------------------------------------------------

name1 = "Cooper"
name2 = "Small"

# Concatentation - Adds together. NOTE: This won't add a space between the variables!
value = name1 + name2
print("Concatenation of name1 and name2 is:", value)

# Repetition - Repeats the string [X] number of times. NOTE: This won't add a space between the variables!
value = name1 * 5
print("Repetition of name1 is:", value)

# Slice - Slices an individual character from a string
value = name1[3]
print("The [3] Slice of name1 is:", value)

# Ranged Slice - Slices a range of characters from a string [starting index:ending index]
value = name1[1:5]
print("The [1:5] Ranged Slice of name1 is:", value)

# In - Checks if [X] is in the string
if "oo" in name1:
    print("\"oo\" is in name1")

# Not in - Check if [X] is not in the string
if "zz" not in name1:
    print("\"zz\" is not in name1")

# r - Ignores escape characters. NOTE: This needs to go at the beginning of the string
print(r"This includes\r\n escape characters. Gross")

# f - This is the f-string formatting
print(f"Name1 is {name1}. Name2 is {name2}")