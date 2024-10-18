'''
Median is the middle value of any data when arranged in ascending or descending order.
'''

from typing import Union

def find_median(liste: Union[list, tuple]) -> Union[float, int]:
    '''
    Takes a list or a tuple, returns a value.
    '''

    # Raise an error if the submitted 'list' isn't of type list or tuple
    if isinstance(liste, (list, tuple)) is False:
        raise TypeError("Wrong type submitted, must be a list or a tuple")
    
    # Raise an error is the list is less than 2 elements
    if len(liste) < 2:
        raise ValueError("The 'list' passed has less than 2 elements, we can't find the median in a list of 1 element")

    liste_t = list(liste) # Force transformation to list in case a tuple is submitted

    if all(isinstance(x, (int, float)) for x in liste_t) is True:
        # If all elements are of type int or float, sort them and get the 2nd largest value
        liste_t.sort() # Sort the list transformed
        if len(liste_t) % 2 == 1:
            median = liste_t[len(liste_t) // 2] # Get the mid element of the sorted list
        else:
            median = (liste_t[len(liste_t) // 2] + liste_t[len(liste_t) // 2 - 1]) / 2
        return median
    
    else:
        # If all elements aren't integer or float, return an error
        raise ValueError("All the values from the 'list' passed aren't of type integer or float")
    
test_array = [12, 10, 12, 10, 12, 12, 10]
print("The median of the array {} is {}".format(test_array, find_median(test_array)))