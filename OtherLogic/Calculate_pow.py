'''
https://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/
Given two integers x and n, write a function to compute xn. We may assume that x and n are small and overflow doesn’t happen.
'''

from typing import Union

def calculate_pow(num: int, pow: int) -> Union[int, float]:
    '''
    This function calculate the number num to the power pow and returns and integer or float rounded at 2 digits if negative.
    '''

    # Define the number to return
    number = num

    # Raise an error if the value of the number to power isn't an integer
    if not isinstance(num, int):
        raise TypeError("The value of the number to power should be an integer")
        
    # Raise an error if the power isn't an integer
    if not isinstance(pow, int):
        raise TypeError("The value of the power should be an integer")

    # If pow = 0 then the answer will always be 1    
    if pow == 0:
        return 1
    # Else, calculate the result
    else: 
        i = 1 # Iterate the multiplication
        while i < abs(pow):
            number *= num
            i += 1
        if pow > 0: # If power is positive
            return number
        else: # If power is negative
            return round(1/number, 2)

print(calculate_pow(3, -1))