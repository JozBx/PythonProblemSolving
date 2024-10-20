'''
Problem: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example:

is_valid("()")  
# Output: True

is_valid("()[]{}")  
# Output: True

is_valid("(]")  
# Output: False

is_valid("([)]")  
# Output: False

is_valid("{[]}")  
# Output: True
'''

# Solution 1: Using Two-pointers approach

def is_valid(s: str) -> bool:
    '''This function takes a string of parentheses/brackets and tells if it's valid'''

    if not isinstance(s, str):
        raise TypeError("The entry should be a string of parentheses/brackets")
    
    # First create the length, if the length is odd, return negative answer
    length = len(s)
    if length % 2 > 0:
        return f"The string {s} isn't valid"
    
    # Initialize search dict
    search_op = {"[": "]", "(": ")", "{": "}"}

    # Initialize bottom and top searching indeces
    bottom, top = 0, length -1

    # Loop through the string while top > bottom
    while top > bottom:
        
        if s[bottom] in search_op and search_op[s[bottom]] == s[top]: # If the parentheses top and bottom are closing
            bottom += 1 # Add one to bottom index
            top -= 1 # Remove 1 to top index
        elif s[bottom] in search_op and search_op[s[bottom]] == s[bottom+1]: # If the parentheses top and bottom are closing
            bottom += 2 # Add 2 to bottom index and don't move top
        else:
            return f"The string {s} isn't valid"
        
    return f"The string {s} is valid"

# Solution 2: Using stack approach

def is_valid(s: str) -> bool:
    '''
    This function checks if the given string of parentheses/brackets is valid using a stack.
    '''

    if not isinstance(s, str):
        raise TypeError("The entry should be a string of parentheses/brackets")
    
    # First create the length, if the length is odd, return negative answer
    length = len(s)
    if length % 2 > 0:
        return f"The string {s} isn't valid"
    
    # Dictionary to map closing brackets to their corresponding opening brackets
    search_op = {")": "(", "]": "[", "}": "{"}
    
    # Stack to store the opening brackets
    stack = []
    
    # Iterate over each character in the string
    for char in s:
        if char in search_op:
            # Pop the top element from the stack if it's non-empty; else assign a dummy value
            top_element = stack.pop() if stack else "#"
            
            # If the mapping for this closing bracket doesn't match the top element, return False
            if search_op[char] != top_element:
                return f"The string {s} isn't valid"
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # If the stack is empty, all brackets were matched correctly
    return f"The string {s} is valid"


par_1 = "()"
par_2 = "()[]{}"
par_3 = "(]"
par_4 = "([)]"
par_5 = "{([])}"
par_6 = "{[()]}"  # New test case (valid, nested)
par_7 = "({[})]"  # New test case (invalid, mismatched nested)
par_8 = "["       # New test case (invalid, single bracket)
par_9 = "{[]}"    # New test case (valid, non-symmetrical but valid)

for par_ in [par_1, par_2, par_3, par_4, par_5, par_6, par_7, par_8, par_9]:
    try:
        print(is_valid(par_))
    except Exception as e:
        print(e)