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

numQtrs = changeAmt // 0.25 #Figure out the number of quarters
changeAmt = changeAmt % 0.25 #Figure out the remaining change

numDimes = changeAmt // 0.10 #Figure out the number of dimes
changeAmt = changeAmt % 0.10 #Figure out the remaining change

numNickels = changeAmt // 0.05 #Figure out the number of nickels
changeAmt = changeAmt % 0.05 #Figure out the remaining change

numPennies = changeAmt // 0.01 #Figure out the number of pennies

#Print the amount of change to the terminal
print("Your change is...")
print("Quarters:",numQtrs)
print("Dimes:%s" % (numDimes))
print("Nickels: {}".format(numNickels))
print(f"Pennies: {numPennies}")

#Print the amount of change to the log file
print("Your change is...", file=changeLog)
print("Quarters:",numQtrs, file=changeLog)
print("Dimes: ", "%s" % (numDimes), file=changeLog)
print("Nickels: {}".format(numNickels), file=changeLog)
print(f"Pennies: {numPennies}", file=changeLog)
print("\n", file=changeLog)