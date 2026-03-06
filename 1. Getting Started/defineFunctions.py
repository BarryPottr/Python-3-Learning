import time

# A function that checks the local time hour, and greets the user based on the time
def greetUser(): # Define the function
    if time.localtime().tm_hour < 12: # Check if it's morning
        print("Good morning Flynn.")
    elif time.localtime().tm_hour == 12: # Check if it's high noon
        print("It's high noon...")
    elif (time.localtime().tm_hour > 12) and (time.localtime().tm_hour < 18): # Check if it's afternoon
        print("Good afternoon Flynn.")
    else: # Otherwise it's night
        print("Goodnight Flynn.")

greetUser() # Call/invoke the function

# ---------------------------------------------------------------------------------------------------------------
# PRACTICE: Create a dynamic vowel checker with functions
#----------------------------------------------------------------------------------------------------------------

# Get the user's word and position of the vowel to be passed into isVowel()
def getVowel():
    word = input("Please enter a word: ")
    position = int(input("Please enter the position of the letter we are checking as a vowel: ")) - 1 # Most users will enter the count of the letter (e in Cooper is the 5th letter), so subtract 1 to account for that in the list
    isVowel(word,position)

# Determines if a letter in a word is a vowel
def isVowel(value,pos):
    
    # Check if length of word is less than position
    while len(value) < pos:
        print("String too short")
        getVowel()

    # See if letter is a vowel
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"] # List of vowels
    if value[pos] in vowels: # See if the letter at position is in the list of vowels
        print(f"Yes, {value[pos]} is a vowel!")
    else:
        print(f"No, {value[pos]} is a consonant. Try again.")
        getVowel()

getVowel()

# If you're returning something, you can either print the result by printing the function, or store the return in a variable by calling a function in the variable definition