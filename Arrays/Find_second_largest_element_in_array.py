'''
https://www.geeksforgeeks.org/find-second-largest-element-array/

Given an array of integers, our task is to write a program that efficiently finds the second-largest element present in the array. 
'''

from typing import Union

def find_second_largest_element(liste: Union[list, tuple]) -> float:
    '''
    Takes a list or an array, returns a value.
    '''

    # Raise an error if the submitted 'list' isn't of type list or tuple
    if isinstance(liste, (list, tuple)) is False:
        raise TypeError("Wrong type submitted, must be a list or a tuple")
    
    # Raise an error is the list is less than 2 elements
    if len(liste) < 2:
        raise ValueError("The 'list' passed has less than 2 elements, we can't find the 2nd largest element in a list of 1 element")

    largest_element = second_largest = float('-inf') # Defining largest and second largest as -infinty

    for el in liste:

        if not isinstance(el, (int, float)): # Check if value isn't of type int or float
            raise ValueError("All the values from the 'list' passed aren't of type integer or float")
        
        else: # If value is of right type

            if el > largest_element: # If value is more than largest element, reassign values
                second_largest, largest_element = largest_element, el
            elif second_largest < el < largest_element: # Else if it is in between largest and second largest, reassign only 2nd largest
                second_largest = el

    if second_largest == float('-inf'): # If we don't have a second largest, return Value Error
        return f"There is no second largest element in this array"
    
    return second_largest # Else return 2nd largest
        
    
test_array_1 = [12, 12, 10]
test_array_2 = [12, 12]
for test_array_ in [test_array_1, test_array_2]:
    try:
        print("The second largest element of the array {} is: {}".format(test_array_, find_second_largest_element(test_array_)))
    except Exception as e:
        print(e)