'''
https://www.geeksforgeeks.org/return-maximum-occurring-character-in-the-input-string/

Given string str. The task is to find the maximum occurring character in the string str.

Examples:


    Input: geeksforgeeks
    Output: e
    Explanation: ‘e’ occurs 4 times in the string

    Input: test
    Output: t
    Explanation: ‘t’ occurs 2 times in the string
'''

def max_char_in_string(s: str) -> int:
    '''
    This function takes a string s and finds the character that has the maximum number of occurence in it
    '''

    if isinstance(s, str) is False:
        raise TypeError("The input must be a string")
    
    # Assume the character with max number of occurences is the first one:
    max, nb = s[0], s.count(s[0])
    for i in s:
        if i != max:
            if s.count(i) > nb:
                max, nb = i, s.count(i)
    
    return max, nb

string1 = "geeksforgeeks"
string2 = "test"
string3 = 3
for string in [string1, string2, string3]:
    try:
        m, n = max_char_in_string(string)
        print(f"the character with the max number of occurences in the string {string} is '{m}' with '{n}' occurences")
    except Exception as e:
        print(e)