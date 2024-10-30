'''
Problem: Basic Calculator II
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, and / operators, and empty spaces. 
The integer division should truncate toward zero.

Examples:

s = "3+2*2"
basic_calculator(s)
# Output: 7

s = " 3/2 "
basic_calculator(s)
# Output: 1

s = " 3+5 / 2 "
basic_calculator(s)
# Output: 5
'''


def basic_calculator(s: str) -> int:
    '''This function evaluates a basic expression and returns the result'''

    if not isinstance(s, str):
        raise TypeError("The input must be of type string")

    s = s.replace(" ", "")

    if "/0" in s:
        raise ZeroDivisionError("There should be no division by zero in the input")
    
    stack = [] # Create a stack as an empty list
    current_num = 0
    last_operator = '+'  # Start with '+' to handle the first number correctly

    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Build the current number if it's a digit
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        
        # If we reach an operator or the end of the string, process the current number
        if char in "+-*/" or i == len(s) - 1:
            # Process the last operator encountered
            if last_operator == '+':
                stack.append(current_num)
            elif last_operator == '-':
                stack.append(-current_num)
            elif last_operator == '*':
                stack[-1] *= current_num
            elif last_operator == '/':
                # Integer division towards zero
                stack[-1] = float(stack[-1] / current_num)
            
            # Update last_operator and reset current_num for the next number
            last_operator = char
            current_num = 0

    # The result is the sum of numbers in the stack
    return sum(stack)
    

s1 = "3+2*2"
s2 = " 3/2 "
s3 = " 3+5 / 2 "
for s_ in [s1, s2, s3]:
    try:
        print(f"The result of {s_} is {basic_calculator(s_)}")
    except Exception as e:
        print(e)