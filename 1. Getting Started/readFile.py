import fileinput

for line in fileinput.input():
    print(line, end='') #Each line in the text file already has a newline at the end, so we remove print()'s newline