#This program asks the user how much their total is broken into dollars and change
#and then determines how many quarters, dimes, nickels, and pennies to give them back

#Ask the user for the total and payment amounts
total = float(input("What is your total? "))
payment = float(input("How much are you paying? "))

#Determine if the payment is enough
changeAmt = 0.0
if (payment < total):
    print("You are not paying enough!")
else:
    changeAmt = payment - total

numQtrs = changeAmt // 0.25 #Figure out the number of quarters
changeAmt = changeAmt % 0.25 #Figure out the remaining change

numDimes = changeAmt // 0.10 #Figure out the number of dimes
changeAmt = changeAmt % 0.10 #Figure out the remaining change

numNickels = changeAmt // 0.05 #Figure out the number of nickels
changeAmt = changeAmt % 0.05 #Figure out the remaining change

numPennies = changeAmt // 0.01 #Figure out the number of pennies

print("Your change is " + str(numQtrs) + " quarters, " + str(numDimes) + " dimes, " + str(numNickels) + " nickels, and " + str(numPennies) + " pennies.")
