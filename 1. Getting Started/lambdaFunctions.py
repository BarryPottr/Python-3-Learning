doubleIt = lambda x: x*2 # Our lambda function. The x next to lambda ("lambda X") is our perameter

print(doubleIt(5)) # We call our lambda function by calling the variable it's assigned to. This will output "10"

my_list = [1, 5, 4, 7, 16, 3, 2]

# This filter will take all the values from my_list, and filter them against the lambda function. Any which are true according to the lambda function are kept.
# The lambda function sees if a number is even.
newList = filter(lambda x: (x%2 == 0) , my_list) 
newList = list(newList)
print(newList)