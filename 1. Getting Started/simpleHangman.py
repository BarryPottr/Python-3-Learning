# This is a very simple game of hangman
#
# RULES:
# 1) Loop max turn count: 6
# 2) Get a guess
# 3) Check guess
# 4) If guess is wrong, increase turn count
# 5) Print correct letters
# 6) If all letters are correct, then Break

# Designate an answer
answer = input("Please enter the answer for the game. It should be one word: ")
lettersGuessed = ""

# The number of wrong attempts before the player loses
failureCount = int(input("How many failures do you want to allow? Please enter a number: "))

# Loop until the player has made too many failed attempts
# Loop will break if they succeed instead
while failureCount > 0:

    # Ask user to guess a letter
    guess = input("Enter a letter for your guess: ")

    # Check if letter is in answer
    if guess in answer:
        print(f"That's a correct letter! There is one or more {guess} in the answer.")
    else:
        print(f"Sorry, {guess} is not in the answer. You have {failureCount - 1} guess(es) left.")
        failureCount -= 1

    # Maintain a list of the guessed letters
    lettersGuessed += guess
    wrongLetterCount = 0

    for letter in answer: # Iterates through each letter in answer
        if letter in lettersGuessed:
            print(f"{letter}", end="") # Print the correct letters for the player to see
        else:
            print("_", end="") # Print underscores to show which letters are still missing
            wrongLetterCount += 1
    print("")

    if wrongLetterCount == 0: # If all the letters in answer have been guessed, the player has won the game
        print("Congratulations! You've won!")
        break # End the loop early so we don't trigger the Game Over message

else: # If the loop isn't broken, it means the player lost. Display a Game Over message
    print("You lose! Game Over.")

