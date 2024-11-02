'''
Problem: Expression Add Operators
Given a string that contains only digits (0-9) and a target value, add binary operators (+, -, or *) between the digits 
 so that the resulting expression evaluates to the target value. Return all possible expressions that evaluate to the target.

Examples:

num = "123"
target = 6
add_operators(num, target)
# Output: ["1+2+3", "1*2*3"]

num = "232"
target = 8
add_operators(num, target)
# Output: ["2*3+2", "2+3*2"]

num = "105"
target = 5
add_operators(num, target)
# Output: ["1*0+5", "10-5"]

num = "00"
target = 0
add_operators(num, target)
# Output: ["0+0", "0-0", "0*0"]

num = "3456237490"
target = 9191
add_operators(num, target)
# Output: []  (No expressions can produce the target)
'''

def add_operators(num: str, target: int) -> list:
    '''This function takes a number num and a target "target" and returns the calculated expression of num to find the target (if exists)'''

    if not isinstance(num, str):
        raise TypeError("The entry must be a number enclosed in a string")
    
    if len(num) <= 1:
        raise ValueError("The entry must be a string of integers of at least 2 digits")
    
    expressions_calc = []
    expressions = []
    
    def expr_calc(num_, expr):

        if len(num_) > 1:

            expr_calc(num_[1:], expr+"+"+num_[0])
            expr_calc(num_[1:], expr+"*"+num_[0])
            expr_calc(num_[1:], expr+"-"+num_[0])

            if int(num_[0]) != 0:
                expr_calc(num_[1:], expr+"/"+num_[0])

        else:

            expressions_calc.append(expr+"+"+num_[0])
            expressions_calc.append(expr+"*"+num_[0])
            expressions_calc.append(expr+"-"+num_[0])
            if int(num_[0]) != 0:
                expressions_calc.append(expr+"/"+num_[0])

    expr_calc(num[1:], num[0]) # Populate the expressions_calc with all possible expressions


    for expr in expressions_calc:

        stack = [] # Create a stack as an empty list
        current_num = 0
        last_operator = '+'  # Start with '+' to handle the first number correctly

        # Iterate over each character in the string
        for i, char in enumerate(expr):
            # Build the current number if it's a digit
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            # If we reach an operator or the end of the string, process the current number
            if char in "+-*/" or i == len(expr) - 1:
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

        if sum(stack) == target:
            expressions.append(expr)

    return expressions if len(expressions) > 0 else "No combination"

couple1 = ("123", 6)
couple2 = ("232", 8)
couple5 = ("105", 5)
couple3 = ("00", 0)
couple4 = ("3456237490", 9191)
for couple_ in [couple1, couple2, couple5, couple3, couple4]:
    try:
        print(f"The expression(s) possible to calculate {couple_[1]} using the integers of {couple_[0]} is (are): {add_operators(couple_[0], couple_[1])}")
    except Exception as e:
        print(e)
