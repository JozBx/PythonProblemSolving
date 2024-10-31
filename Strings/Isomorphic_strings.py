'''
Problem: Isomorphic Strings
Given two strings s and t, determine if they are isomorphic. 
Two strings are isomorphic if the characters in s can be replaced to get t.

Note:

Each character in s must map to a unique character in t.
The order of characters must be preserved.
Examples:

s = "egg"
t = "add"
is_isomorphic(s, t)
# Output: True
# Explanation: 'e' maps to 'a', and 'g' maps to 'd'.

s = "foo"
t = "bar"
is_isomorphic(s, t)
# Output: False
# Explanation: 'o' cannot map to two different characters ('a' and 'r').

s = "paper"
t = "title"
is_isomorphic(s, t)
# Output: True
# Explanation: 'p' maps to 't', 'a' maps to 'i', 'p' maps to 't', 'e' maps to 'l', 'r' maps t
'''

from collections import Counter

def is_isomorphic(s: str, t: str) -> str:
    '''This function takes 2 strings and checks if they are isomorphic'''

    if not isinstance(s, str) or not isinstance(t, str):
        raise TypeError("Both entries must be of type string")
    if len(s) != len(t):
        return "The strings can't be isomorphic as they aren't the same length"
    
    dic_s, dic_t = {}, {} # Create 2 empty dictionaries for s and t

    for char in s: # Loop through s
        # Add new character to dic_s if it does not exist, else add 1 to the count
        if char not in dic_s:
            dic_s[char] = 1
        else:
            dic_s[char] += 1

    for char in t:
        # Add new character to dic_t if it does not exist, else add 1 to the count
        if char not in dic_t:
            dic_t[char] = 1
        else:
            dic_t[char] += 1

    if len(dic_s) != len(dic_t): # If there are unequal number of unique characters, strings aren't isomorphic
        return "The strings aren't isomorphic"
    else:
        if Counter(dic_t.values()) == Counter(dic_s.values()):
            return "The strings are isomorphic"
        else:
            return "The strings aren't isomorphic"

c1 = "egg", "add"
c2 = "foo", "bar"
c3 = "paper", "title"
for c_ in [c1, c2, c3]:
    try:
        print(f"Are the strings {c_} isomorphic? {is_isomorphic(c_[0], c_[1])}")
    except Exception as e:
        print(e)
