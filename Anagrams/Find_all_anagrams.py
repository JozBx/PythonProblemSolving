'''
Problem: Find All Anagrams in a String
Given two strings s and p, return a list of all the anagrams of p's. You may return the answer in any order.

An anagram is a rearrangement of a string. For example, "abc" is an anagram of "cba", and "bac" is an anagram of "abc".

Example:

find_anagrams("cbaebabacd", "abc")  # Output: [cba, bac]
find_anagrams("abab", "ab")         # Output: [ab, ba, ab]
'''

# Solution 1 -> Without the collections module

def find_anagrams(s: str, p: str) -> list:
    '''
    This function takes to string s and p, and checks how many anagrams of p are in s, and prints them
    '''

    # Check if the s and p inputs are strings
    if isinstance(s, str) is False:
        raise TypeError("first input of the function must be of type string")
    if isinstance(p, str) is False:
        raise TypeError("second input of the function must be of type string")

    # created length of strings and empty list of anagrams, as well as the sorted p string
    len_s, len_p = len(s), len(p)
    if len_p > len_s:
        return []  # If p is longer than s, there can't be any anagrams
    list_anagrams = []
    sorted_p = sorted(p)

    # Move through the string character by character
    for char in range(len_s - len_p + 1):
        if sorted(s[char:char+len_p]) == sorted_p: # Check if the sorted string is equal to sorted p string
            list_anagrams.append(s[char:char+len_p]) # If yes, append to the list of anagrams

    return list_anagrams


# Solution 2 -> Using the collections module

from collections import Counter

def find_anagrams(s: str, p: str) -> list:
    '''
    This function takes two strings, s and p, and returns the actual anagrams of p found in s.
    '''
    
    # Check if inputs are valid strings
    if not isinstance(s, str):
        raise TypeError("First input must be a string")
    if not isinstance(p, str):
        raise TypeError("Second input must be a string")
    
    len_s, len_p = len(s), len(p)
    if len_p > len_s:
        return []  # If p is longer than s, there can't be any anagrams
    
    # Initialize counters for p and the first window in s
    p_count = Counter(p)
    s_count = Counter(s[:len_p - 1])
    
    result = []
    
    # Sliding window across the string s
    for i in range(len_p - 1, len_s):
        # Add the current character to the window
        s_count[s[i]] += 1
        
        # Compare window with p_count
        if s_count == p_count:
            result.append(s[i - len_p + 1:i + 1])  # Append the actual anagram substring
        
        # Remove the character that's sliding out of the window
        s_count[s[i - len_p + 1]] -= 1
        if s_count[s[i - len_p + 1]] == 0:
            del s_count[s[i - len_p + 1]]  # Remove count if it drops to 0
    
    return result

test_1 = ("cbaebabacd", "abc")
test_2 = ("abab", "ab")
for test in [test_1, test_2]:
    try:
        print(f"the anagrams of {test[1]} present in {test[0]} are {find_anagrams(test[0], test[1])}")
    except Exception as e:
        print(e)

