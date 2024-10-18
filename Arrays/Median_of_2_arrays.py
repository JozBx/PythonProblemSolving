'''
Given two sorted arrays, arr1[] and arr2[], the task is to find the median of these sorted arrays.
Where n is the number of elements in the first array, and m is the number of elements in the second array. 
'''

from typing import Union

def median_of_two_arrays(array1: Union[list, tuple], array2: Union[list, tuple]) -> Union[float, int]:
    '''Take 2 arrays and return the median of their union
    '''

    # Raise an error if the submitted 'list' isn't of type list or tuple
    if isinstance(array1, (list, tuple)) is False or isinstance(array2, (list, tuple)) is False:
        raise TypeError("Wrong type submitted for one of the arrays, they must be lists or tuples")

    arr1 = list(array1) # Force list
    arr2 = list(array2) # Force list

    l_ar1 = len(arr1) # Length of the 1st array submitted
    l_ar2 = len(arr2) # Length of the 2nd array submitted

    # Current index of list arr1
    i = 0
    j = 0

    m1 = -1 # m1 to store the middle element
    m2 = -1 # m2 to store the second middle element which is used when total number of elements are even
    
    # Loop till (m+n)/2
    for count in range((l_ar1 + l_ar2) // 2 + 1):
        m2 = m1
        
        # If both the arrays have remaining elements
        if i != l_ar2 and j != l_ar1:
            if arr1[i] > arr2[j]:
                m1 = arr2[j]
                j += 1
            else:
                m1 = arr1[i]
                i += 1
                
        # If only arr1 has remaining elements
        elif i < l_ar2:
            m1 = arr1[i]
            i += 1
        
        # If only arr2 has remaining elements
        else:
            m1 = arr2[j]
            j += 1
    
    # Return median based on odd/even size
    if (l_ar1 + l_ar2) % 2 == 1:
        return m1
    else:
        return (m1 + m2) / 2


# Example usage
arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]

print(median_of_two_arrays(arr1, arr2))