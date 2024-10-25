'''
https://www.geeksforgeeks.org/binary-search/
Binary Search Algorithm is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. 
The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 
'''

from typing import Union
from math import ceil

def binary_searching(array: Union[list, tuple], value: int) -> int:
    '''This function takes an ordered array and search for the position of the value using Binary Search Algorithm
    '''

    # Raise an error if the array is not of type list/tuple or if the value searched is not of type integer
    if isinstance(array, (list, tuple)) is False:
        raise TypeError("The array must be of type list or tuple")
    elif isinstance(value, int) is False:
        raise TypeError("The value searched must be of type int")    
    elif all(isinstance(x, int) for x in array) is False:
        raise TypeError("All values of the array must be integers")

    # Create 3 values start_l, start_m and start_h for research purpose
    start_l = 0 # lower pos to start the search with
    start_m = ceil(len(array)/2) # Divides the length of the array by 2 and start the search at the upper value if float
    start_h = len(array)

    search_n = 0 # Number of rounds it took to find the position

    # While start_l is different than start_h
    while start_l+1 != start_h:
        search_n += 1
        if value == array[start_m]:
            return start_m+1, search_n
        else:
            if value > array[start_m]:
                start_l = start_m
                start_m = ceil((start_h+start_m)/2)
            else:
                start_h = start_m
                start_m = ceil((start_l + start_m)/2)

    print("The value isn't in the array")
    return None, None


arr = (2, 5, 7, 8, 11, 12, 16, 16, 17, 20, 22, 38, 56, 72, 91)
x = 38
position, num_search = binary_searching(arr, x)
if position is not None:
    print(f"The value {x} can be found in the array {arr} at the position number {position}, it took {num_search} iterations to find it")