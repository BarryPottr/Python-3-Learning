#Revision: Use different string types to print the end message, and log the total, payment, 
#and change into a file called "change.txt"

#This program asks the user how much their total is broken into dollars and change
#and then determines how many quarters, dimes, nickels, and pennies to give them back

#Open change.txt in append mode
changeLog = open("change.txt", "a")

#Ask the user for the total and payment amounts
total = float(input("What is your total? "))
payment = float(input("How much are you paying? "))

#Confirm total and payment values are positive values
while (total < 0) or (payment < 0):
    print("That's not a positive value")
    if total < 0:
        total = float(input("What is your total? "))
    else:
        payment = float(input("How much are you paying? "))

#Determine if the payment is enough
changeAmt = 0.0
if (payment < total):
    print("You are not paying enough!")
else:
    changeAmt = payment - total

#Log the total and payment amounts into change.txt
print("Total: $" + str(total), file=changeLog)
print("Payment: $" + str(payment), file=changeLog)

coins = [0.25, 0.10, 0.05, 0.01] #These are our currency value references
coinCount = [0, 0, 0, 0] # We will use this to store how much of each coin type we need to give back
coinType = ["Quarters", "Dimes", "Nickels", "Pennies"]

print("Your change is...", file=changeLog) # Print start of change message to changeLog
for i in range(0, len(coins)):
    coinCount[i] = changeAmt // coins[i] # Divide changeAmt by the corresponding currency reference value
    changeAmt -= coinCount[i] * coins[i] # Subtract amount from changeAmt before moving on
    print(f"{coinType[i]}: {coinCount[i]}") # Print the coin amount to the terminal
    print(f"{coinType[i]}: {coinCount[i]}", file=changeLog) # Print the coin amount to changeLog
