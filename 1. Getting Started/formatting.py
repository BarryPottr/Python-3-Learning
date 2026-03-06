name = "Cooper"
age = 27

print("Hello", name, "you are", str(age), "years old.")

print("Hello %s" % name) #The %s is a placeholder for a string, and the value to replace it with is given after the % operator

#%-Format
print("Hello %s, you are %s years old." % (name, age)) #(name, age) is a tuple (you'll learn more about them later)

#String Format
print("Hello {}, you are {} years old.".format(name, age))

print("Hello {1}, you are {0} years old.".format(name, age)) #You can also specify the order for the curly braces with numbers

#F-String Format
print(f"Hello {name}, you are {age} years old.")

print(f"Hello {name}, in ten years you'll be {age + 10} years old.")

message = (
    f"Hello {name},"
    f"You are {age} years old."
    f"In ten years you'll be {age + 10} years old."
)
print(message)