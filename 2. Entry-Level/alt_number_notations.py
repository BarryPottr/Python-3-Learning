##################################################################
# BINARY NOTATION
##################################################################

binary = 0b010101

print(binary)

bin_string = "00101010001010101" # This is 21589
print(int(bin_string, 2)) # By specifying the base we are counting in, we tell Python the number is binary

# To view a number as binary, we use bin()
num = 100
print(bin(num)) # This will output 0b1100100

### BITWISE OPERATORS
x = 0b1010
y = 0b1110

print(f"{bin(x)} AND {bin(y)} equates to {bin(x & y)}.") # This should equate to 0b1010

print(f"{bin(x)} OR {bin(y)} equates to {bin(x | y)}.") # This should equate to 0b1110

print(f"{bin(x)} XOR {bin(y)} equates to {bin(x ^ y)}.") # This should equate to 0b100

print(f"NOT {bin(x)} equates to {bin(~x)}.") # This should equate to -0b1011

print(f"{bin(x)} << 2 is {bin(x << 2)}.") # This should equate to 0b101000

print(f"{bin(x)} >> 2 is {bin(x >> 2)}.") # This should equate to 0b10

##################################################################
# OCTAL & HEXADECIMAL NOTATION
##################################################################

octal_num = 0o123
hex_num = 0xa1b2c3

print(oct(octal_num))
print(hex(hex_num))

##################################################################
# SCIENTIFIC NOTATION
##################################################################

print(9.3e7)
print(format(93000000, '.2e')) # This gives us 2 digits after the decimal point in scientific notation