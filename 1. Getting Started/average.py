import fileinput

studentGrades = {}

#Takes each line from the file, and build a dictionary with them
for line in fileinput.input(): # This iterates through each line in the inputted file
    values = line.strip() # strip() removes any leading or trailing whitespace, because the end of each line will have a \n in the CSV
    values = values.split(',') # split() separates a string into a list, and you can specify the separator, which in this case is (',')

    # This will take values 0 and 1 from each loop, and build a dictionary key-value pairing. With each loop, values[0] and values[1] will be overwritten, so we want to save them in the dictionary each time
    studentGrades.update({values[0]:int(values[1])}) # .update() appends a new value onto a dictionary. We call int() to make sure the numerical value for each entry is an int

print(studentGrades)

# Add the grades for all the students
sum = 0
for student in studentGrades:
    sum += studentGrades[student]

average = sum / len(studentGrades) # Find the average

print(f"Average of the grades is {average}.") # Print the average with an f-string