fileObject = open("output.txt", mode="w") #Open the file in write mode. mode="w" is the "w" string literal, meaning "Write"

#This will create a file called "output.txt" and write "Hello Cooper!" to it. 
#The file will be created in the same directory as this script.
#Mode "w" will overwrite the file if it already exists.
print("Hello Cooper!" , file=fileObject) 

fileAppend = open("output.txt", mode="a") 
print("This is a new line.", file=fileAppend)

print("Hello", "Cooper", "How are you?", sep = ":")

print("Hello", end=" ")
print("Goodbye")