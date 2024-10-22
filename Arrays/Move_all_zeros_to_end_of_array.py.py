'''
https://www.geeksforgeeks.org/move-zeroes-end-array/
Given an array of integers arr[], the task is to move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

Examples: 

    Input: arr[] = {1, 2, 0, 4, 3, 0, 5, 0}
    Output: arr[] = {1, 2, 4, 3, 5, 0, 0, 0}
    Explanation: There are three 0s that are moved to the end.

    Input: arr[] = {10, 20, 30}
    Output: arr[] = {10, 20, 30}
    Explanation: No change in array as there are no 0s.

    Input: arr[] = {0, 0}
    Output: arr[] = {0, 0}
    Explanation: No change in array as there are all 0s.
'''

from typing import Union

def move_all_zeros_to_end(array: Union[list, tuple]) -> list:

    '''This function takes an array (list or tuple) and moves all zeros at the end of it
    '''

    # Raise an error if the array isn't of type list or tuple
    if isinstance(array, (list, tuple)) is False:
        raise TypeError("The array must be of type list or tuple")
    # Raise an error if at least one of the elements of the array isn't of type int/float
    if all(isinstance(x, (int, float)) for x in array) is False:
        raise TypeError("All elements of the array should be of type integer or float")
    
    # Filter out the non-zero elements
    non_zero_elements = [x for x in array if x != 0]
    
    # Count the number of zeros
    zero_count = len(array) - len(non_zero_elements)
    
    # Append the required number of zeros to the end
    arr = non_zero_elements + [0] * zero_count

    return arr

arr1 = ["cat", 0, 1, 2]
arr2 = "string"
arr3 = (1, 2, 0, 4, 3, 5, 0, 0, 0)
arr4 = [10, 20, 30]
arr5 = [0, 0]
for arr in [arr1, arr2, arr3, arr4, arr5]:
    try:
        print(f"The reorder array {arr} is {move_all_zeros_to_end(arr)}")
    except Exception as e:
        print(e)

