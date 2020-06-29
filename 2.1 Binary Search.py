"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    st = 0
    end = len(input_array)-1
    while st != end:
        mid = st + (end-st) //2
        if input_array[mid] == value:
            return mid
        elif value > input_array[mid]:
            st = mid+1
        else:
            end = mid-1
    if  input_array[st] == value:
        return st 
    else :
        return -1     

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))