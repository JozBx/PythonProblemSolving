'''
https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
Given an integer n, write a function that returns count of trailing zeroes in n!. 

Examples : 

    Input: n = 5
    Output: 1 
    Explanation: Factorial of 5 is 120 which has one trailing 0.

    Input: n = 20
    Output: 4
    Explanation: Factorial of 20 is 2432902008176640000 which has 4 trailing zeroes.

    Input: n = 100
    Output: 24
'''

def return_trailing_zeroes_fact(n: int) -> int:

    '''This function takes an integer n, gets its factorial number and returns the number of trailing zeros
    '''

    if isinstance(n, int) is False:
        raise TypeError("The parameter must be of type integer")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    count_zeros = 0
    power_of_five = 5

    # Count how many multiples of 5, 25, 125, etc... are in n

    while n // power_of_five > 0:
        count_zeros += n // power_of_five
        power_of_five *= 5

    return count_zeros

n1 = 5
n2 = 20
n3 = 100
n4 = -1
n5 = 1
for var in ["test", 4.8, n1, n2, n3, n4, n5]:
    try:
        print(f'The number of trailing zeroes for the factorial of {var} is {return_trailing_zeroes_fact(var)}')
    except Exception as e:
        print(e)