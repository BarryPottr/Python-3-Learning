var1 = "Cooper \"the man\" Small" # If we didn't include the backslash, and instead wrote "Cooper "the man" Small", we'd get a syntax error
print(var1)

# What if I want to print a backslash in my code?
var2 = "This is a backslash: \\. These are FOUR backslashses: \\\\\\\\" # Need equal number of backslashes. Each pair of backslashes, makes a backslash string character.
print(var2)

# Can also use the opposite quote (single or double) to quote in a string
var3 = "Cooper 'the man' Small" 
var4 = 'Cooper "the man" Small'
print(var3)
print(var4)

# \r is a Carriage Return, so it returns the cursor to the beginning of the line, and begins typing again. 
# This will overwrite anything previously entered, up to the remaining characters left
var5 = "Hello\rThere" # This should print "There"
var6 = "Yessiree\rMa'am" # This should print "Ma'amree"
print(var5)
print(var6)

# If you want to learn more about these escape characters: https://www.w3schools.com/python/python_strings_escape.asp