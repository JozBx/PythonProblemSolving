'''
https://www.geeksforgeeks.org/reverse-a-string-in-java/
Reverse a string. String are immutable elements.
'''

# Solution 1

def revers_string(string: str) -> str:
    '''Reverse a string. The output is the reversed string
    '''

    # Check if the input is a string

    if isinstance(string, str) is False:
        return TypeError("The element submitted should be of type string")
    
    # Loop through the string in reverse order
    reversed_string = "" 
    for char in string[::-1]:
        reversed_string += char
    
    return reversed_string # Return the reversed string

# Solution 2 - Using slices

def revers_string(string: str) -> str:
    '''Reverse a string. The output is the reversed string
    '''

    # Check if the input is a string

    if isinstance(string, str) is False:
        return TypeError("The element submitted should be of type string")
    
    reversed_string = string[::-1] # Create the reversed string
    
    return reversed_string


message = "uoY olleH"

for mess in [message]:
    try:
        print("The reversed string of '{}' is '{}'".format(message, revers_string(message)))
    except Exception as e:
        print(e)