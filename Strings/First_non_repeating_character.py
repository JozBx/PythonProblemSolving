'''
Given a string, find the first non-repeating character in it.
'''

# First solution: Looping through the string

def first_non_repeating_char(entry: str) -> str:
    """Takes a string, finds the first non repeating character. Approach using count()
    """

    # Raise en an error if the entry provided isn't a string
    if isinstance(entry, str) is False:
        raise TypeError("This function can only deal with strings! Please provide a string")

    for char in entry:
        # Iterate through the string and search for the 1st non repeating character
        if char.isalpha() is True and entry.lower().count(char.lower()) == 1: # Make sure the characters are all lower so 
            print(f"The first non repeated in the string {entry} provided is {char}")
            return char
        else:
            continue
        
    print("None of the characters in the string provided is a non-repeated character")

# Second solution: Using dictionary

def first_non_repeating_char(entry: str) -> str:
    """Takes a string, finds the first non repeating character. Approach using dictionary
    """

    # Raise en an error if the entry provided isn't a string
    if isinstance(entry, str) is False:
        raise TypeError("This function can only deal with strings! Please provide a string")
    
    # Create an empty dictionary
    char_dic = {}

    # Populate the dictionary
    for char in entry:
        if char.lower() in char_dic.keys():
            char_dic[char.lower()] += 1
        else:
            char_dic[char.lower()] = 1

    # Search for the first non repeated character
    for char in entry:
        # Iterate through the string and search for the 1st non repeating character
        if char.isalpha() is True and char_dic[char.lower()] == 1: 
            print(f"The first non repeated in the string {entry} provided is {char}")
            return char
        else:
            continue
        
    print("None of the characters in the string provided is a non-repeated character")
        
string = "Geeks3ForGees"
first_non_repeating_char(entry=string)