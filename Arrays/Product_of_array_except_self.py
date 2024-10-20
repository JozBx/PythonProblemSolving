'''
Problem: Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The solution should be O(n) time complexity and should not use division.

You need to compute the product of all elements of the array except for the current element at index i, and return this as an output array.
Note: You are not allowed to use division, which means you cannot just calculate the total product and divide by each element.

Example:

product_except_self([1, 2, 3, 4])  
# Output: [24, 12, 8, 6]

product_except_self([-1, 1, 0, -3, 3])  
# Output: [0, 0, 9, 0, 0]
'''

# Solution 1: Looping through the array once and calculate the left and right sums

def product_elements(arr):

    res = 1 # Assume the result is 1 be consistent
    if arr is None: # If the array does not exist, return the result straight away
        return res
    else: # Else, multiply all elements
        for num in arr:
            res *= num
        return res # return the result of all elements multiplied


def product_except_self(array: list) -> list:
    '''
    This function takes an array of X elements and returns for each element, the products of all the other elements of the array 
    '''

    # Check if the input is list or tuple - raise Exception if it isn't

    if isinstance(array, list) is False:
        raise TypeError("The array should be of type list or tuple")
    
    len_array = len(array) # Number of elements of the array
    output_array = [] # Create empty output array

    # Loop throught the array
    for el in range(len_array):

        left_s = product_elements(array[0:el]) # Calculate left side
        right_s = product_elements(array[el+1:len_array]) # Calculate right side

        output_array.append(left_s*right_s) # Append the multiplication of left and right side of the element

    return output_array


# Solution 2: Calculate left and right products one after the other and multiply them during the right run

def product_except_self(array: list) -> list:
    '''
    This function takes an array of X elements and returns for each element, the products of all the other elements of the array 
    '''

    # Check if the input is list or tuple - raise Exception if it isn't

    if not isinstance(array, list):
        raise TypeError("The input should be a list of integers")
    
    len_array = len(array) # Number of elements of the array
    
    # Initialize the result array with 1s
    output_array = [1] * len_array

    # Pass 1: Calculate the product of all elements to the left of each index
    left_product = 1
    for el in range(len_array):
        output_array[el] = left_product
        left_product *= array[el]

    # Pass 2: Calculate the product of all elements to the right of each index
    right_product = 1
    for el in range(len_array - 1, -1, -1):
        output_array[el] *= right_product
        right_product *= array[el]

    return output_array


array1 = [1, 2, 3, 4]
array2 = [-1, 1, 0, -3, 3]
for array_ in [array1, array2]:
    try:
        print(f"The product except self output of the array {array_} is {product_except_self(array_)}")
    except Exception as e:
        print(e)