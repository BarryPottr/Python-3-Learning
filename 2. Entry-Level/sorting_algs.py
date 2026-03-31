#####################################################################
# SELECTION SORT
#####################################################################


def selection_sort(numbers_original):
    numbers = numbers_original.copy()
    sorted_numbers = []

    for _ in range(len(numbers)):
        next_min = min(numbers)
        sorted_numbers.append(next_min)
        numbers.remove(next_min)
    
    return sorted_numbers

print(selection_sort([4, 56, -8, 45, 28, 8, 8, -100]))


#####################################################################
# BUBBLE SORT
#####################################################################


def bubble_sort(num):
    for _ in num:
        for i in range(len(num) - 1): # We use -1 so num[i + 1] doesn't cause an exception when we reach the max index
            if num[i] > num[i + 1]: # Change > to < if you want descending order
                a = num[i + 1]
                num[i + 1] = num[i]
                num[i] = a
    
    return num

print(bubble_sort([1, 5, -7, 8, 8, -100]))


#####################################################################
# INSERTION SORT
#####################################################################


def insertion_sort(num_original):
    numbers = num_original.copy()
    sorted_numbers = []

    for x in numbers:
        was_inserted = False

        for i in range(len(sorted_numbers)):
            if sorted_numbers[i] > x:
                sorted_numbers.insert(i, x)
                was_inserted = True
                break

        if not was_inserted:
            sorted_numbers.append(x)

    return sorted_numbers

print(insertion_sort([1, 5, -7, 8, 8, -100]))


#####################################################################
# CHALLENGE
#####################################################################

# GOAL: Create a function that allows the selection, bubble, and 
# insertion sort functions to work with any type of data we feed it

# TIP: Sort alphabetically

######
# PART 1: SELECTION SORT
######


def selection_sort(list_original):
    ls = list_original.copy()
    sorted_numbers = []

    for _ in range(len(ls)):
        next_min = min(ls)
        sorted_numbers.append(next_min)
        ls.remove(next_min)
    
    return sorted_numbers

print(selection_sort([4, 56, -8, 45, 28, 8, 8, -100]))


######
# PART 2: BUBBLE SORT
######


def bubble_sort(num):
    for _ in num:
        for i in range(len(num) - 1): # We use -1 so num[i + 1] doesn't cause an exception when we reach the max index
            if num[i] > num[i + 1]: # Change > to < if you want descending order
                a = num[i + 1]
                num[i + 1] = num[i]
                num[i] = a
    
    return num

print(bubble_sort([1, 5, -7, 8, 8, -100]))


######
# PART 3: INSERTION SORT
######


def insertion_sort(num_original):
    numbers = num_original.copy()
    sorted_numbers = []

    for x in numbers:
        was_inserted = False

        for i in range(len(sorted_numbers)):
            if sorted_numbers[i] > x:
                sorted_numbers.insert(i, x)
                was_inserted = True
                break

        if not was_inserted:
            sorted_numbers.append(x)

    return sorted_numbers

print(insertion_sort([1, 5, -7, 8, 8, -100]))