'''
Problem: Find the Minimum Window Substring
Given two strings s and t, return the minimum window in s that contains all the characters in t. 
If there is no such window, return an empty string "".
t is made of unique characters in this version

Example:

s = "ADOBECODEBANC"
t = "ABC"
minimum_window_substring(s, t)
# Output: "BANC"

s = "a"
t = "a"
minimum_window_substring(s, t)
# Output: "a"

s = "a"
t = "ab"
minimum_window_substring(s, t)
# Output: ""
'''

def minimum_window_substring(s: str, t: str) -> str:
    '''This function takes 2 strings s and t and returns the smallest window of s containing all chars of t'''

    if not isinstance(s, str) or not isinstance(t, str):
        raise TypeError("The entries must be of type string")
    
    start = 0
    end = 0
    window = float('inf')

    # Creation of chars_t, dictionary of the characters of t
    chars_t = {}
    for char in list(t):
        chars_t.update({char: -1})

    for i in range(len(s)): # Loop through the string s

        if s[i] in chars_t: # If the character is in the string t
            chars_t[s[i]] = i
            if -1 not in chars_t.values(): # If the dictionary contains no more of -1 values
                temp_window = max(chars_t.values()) - min(chars_t.values())
                if temp_window < window:
                    start, end, window = min(chars_t.values()), max(chars_t.values())+1, temp_window

    return s[start:end] if start > -1 and end > -1 else ""


s1 = "ADOBECODEBANC"
t1 = "ABC"

s2 = "a"
t2 = "a"

s3 = "a"
t3 = "ab"

for st_ in [(s1, t1), (s2, t2), (s3, t3)]:
    try:
        print(f"the smallest substring window for {st_[1]} in {st_[0]} is {minimum_window_substring(st_[0], st_[1])}")
    except Exception as e:
        print(e)