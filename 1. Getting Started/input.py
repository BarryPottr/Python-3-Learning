prompt = "Type your age: "
inputLog = open("inputLog.txt", "a") #Open the file in append mode so we don't overwrite previous entries

userInput = input(prompt)
while not userInput.isdigit():
    print("That's not a number. Enter your age as a number...")
    print(userInput, file=inputLog)
    userInput = input(prompt)

print(userInput, file=inputLog)
agePlusTen = int(userInput) + 10

print("Your age plus ten is", agePlusTen)