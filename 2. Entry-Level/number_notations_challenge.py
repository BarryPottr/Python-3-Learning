##################################################################
# CHALLENGE
##################################################################

# GOAL: Create a script that prints out the numbers 1-16 in base 10, binary, octal, hex, and scientific notation

for num in range(1, 17):
    print(f"==={num}===")
    print(f"    Binary: {bin(num)}")
    print(f"    Octal: {oct(num)}")
    print(f"    Hexadecimal: {hex(num)}")
    print(f"    Scientific Notation: {format(num, '.1e')}")
    print("")
