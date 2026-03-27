# def any_have_value(ls, key, value) - does the dictionary have any of the keys or values, return True if so
# def all_greater_than(ls, num) - are all the numbers in the list greater than num

def any_have_value(dictionary, key, value):

    values = [x.get(key, None) for x in dictionary]
    return any(v == value for v in values)

def all_greater_than(ls, num):

    return all([x > num for x in ls])

my_dict = [
    {'a': 1, 'b': 21, 'c': 3, 'd': 4, 'e': 5, 'f': 6456, 'g': 7, 'h': 8, 'i': 9, 'j': 10},
    {'a': 1, 'b': 22, 'c': 3, 'd': 4, 'e': 50, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10},
    {'a': 1, 'b': 2, 'c': 3, 'd': 400, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10},
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 11},
    ]

print(any_have_value(my_dict, 'b', 22))
print(all_greater_than([1, 2, 3, 4, 5], 0))