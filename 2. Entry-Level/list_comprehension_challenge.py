##############################################################
# QUESTION 1
##############################################################

# Write a function called long_words(words) that takes a list of strings and uses a 
# list comprehension to return a new list containing only the words that have more 
# than 4 characters, with each word converted to lowercase.
#
# Example behavior:
#   long_words(["Apple", "Cat", "Banana", "Hi", "GRAPE"])
#   Expected output: ["apple", "banana", "grape"]

def long_words(words):
    
    newlist = [x.lower() for x in words if len(x) > 4]

    return newlist 

print(f"The answer to Question 1 is {long_words(["Apple", "Cat", "Banana", "Hi", "GRAPE"])}.")

# FEEDBACK: You could simplify this by returning the list comprehension

##############################################################
# QUESTION 2
##############################################################
print("")
# Write a function called even_doubles(numbers) that takes a list of integers and 
# uses a list comprehension to return a new list containing only the even numbers, 
# each multiplied by 2.
#
# Example behavior:
#   even_doubles([1, 2, 3, 4, 5, 6])
#   Expected output: [4, 8, 12]

def even_doubles(numbers):

    return [x * 2 for x in numbers if x % 2 == 0]

print(f"The answer to Question 2 is {even_doubles([1, 2, 3, 4, 5, 6])}.")

##############################################################
# QUESTION 3
##############################################################
print("")
# Write a function called flat_odds(nested) that takes a list of lists of integers 
# and uses a single list comprehension to return a flat list containing only the 
# odd numbers from all the inner lists.
#
# Example behavior:
#   flat_odds([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#   Expected output: [1, 3, 5, 7, 9]

def flat_odds(nested):
    
    return [col for row in nested for col in row if col % 2 != 0]

print(f"The answer to Question 3 is {flat_odds([[1, 2, 3], [4, 5, 6], [7, 8, 9]])}.")

# NOTE: To convert a 2D matrix into a single flat list, the for clauses are ordered 
# differently: the outer loop iterates over the sublists, and the inner loop iterates 
# over the elements within each sublist

##############################################################
# QUESTION 4
##############################################################
print("")
# Write a function called word_lengths(sentences) that takes a list of strings (sentences) 
# and uses a dictionary comprehension to return a dictionary where each word is a key and 
# its length is the value. If a word appears more than once across all sentences, the last 
# occurrence wins.
#
# Function call: word_lengths(["hello world", "hello there"])

def word_lengths(sentences):

    # Split the sentences into individual words with split()
    # Iterate through each word.len() and put it into the dictionary
    new_sentences = [col for row in sentences for col in row.split()]

    return {word: len(word) for word in new_sentences}


print(f"The answer to Question 4 is {word_lengths(["hello world", "hello there"])}.")

# FEEDBACK: You could combine both comprehensions into one:
#   return {col: len(col) for row in sentences for col in row.split()}
# Keeping it as two comprehensions is fine, and can help with readability. It's up to you

##############################################################
# QUESTION 5
##############################################################
print("")
# Write a function called invert_dict(d) that takes a dictionary and uses a dictionary 
# comprehension to return a new dictionary where the keys and values are swapped. Only 
# include pairs where the value is a string.
#
# Function call: invert_dict({"name": "Alice", "age": 30, "city": "Paris"})

def invert_dict(d):
    
    return {value: key for key, value in d.items() if type(value) == str}

print(f"The answer to Question 5 is {invert_dict({"name": "Alice", "age": 30, "city": "Paris"})}.")

##############################################################
# QUESTION 6
##############################################################
print("")
# Write a function called group_by_length(words) that takes a list of strings and returns 
# a dictionary where each key is a word length and each value is a list of words with that 
# length.
#
# Function call: group_by_length(["cat", "dog", "elephant", "ant", "bear"])

def group_by_length(words):

    # Sort through list: x for x in words
    # Dictionary: len(val).setdefault(x).append(x)

    my_dict = {}
    for x in words:
        my_dict.setdefault(len(x), []).append(x) # While the value within the brackets of setdefault() can be omitted, you still need to include the brackets. Otherwise the default value is "None" which can't be appended

    return my_dict

print(f"The answer to Question 6 is {group_by_length(["cat", "dog", "elephant", "ant", "bear"])}.")

# NOTE: In this case, a simple loop is better than a comprehension. 
# The issue is that .append() always returns None. It modifies the list in place and returns 
# nothing. So the comprehension is collecting the return values of .append(), which are all 
# None.
#
# This is also using {} which makes it a set comprehension, not a dictionary — so it's collecting 
# all those None values into a set, giving us {None}.

# NOTE: setdefault(key, default) is a great tool for building dictionaries of lists

##############################################################
# QUESTION 7
##############################################################
print("")
# Write a function called uppercase_values(data) that takes a dictionary of dictionaries and 
# returns a new dictionary where all string values in the inner dictionaries are uppercased. 
# Non-string values should be left unchanged.
#
# Function call: 
#   uppercase_values({
#       "person1": {"name": "alice", "age": 30},
#       "person2": {"name": "bob", "city": "paris"}
#   })

def uppercase_values(data):
    
    # Outer comprehension: key: inner_dict for key, inner_dict in data.items()
    #   NOTE: .items() gives us a tuple of the key:value, and we can unpack them into a dictionary by saying key:value for key,value
    
    # Inner comprehension: inner_key: inner_value.upper() if isinstance(inner_value, str) else inner_value for inner_key,inner_value in inner_dict.items()

    return {key: {inner_key: inner_value.upper() if isinstance(inner_value, str) else inner_value for inner_key, inner_value in inner_dict.items()} for key, inner_dict in data.items()}

print(f"The answer to Question 7 is {uppercase_values({"person1": {"name": "alice", "age": 30},"person2": {"name": "bob", "city": "paris"}})}.")
