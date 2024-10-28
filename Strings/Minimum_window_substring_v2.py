'''
Problem: Find the Minimum Window Substring
Given two strings s and t, return the minimum window in s that contains all the characters in t. 
If there is no such window, return an empty string "".

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
    
    if not t or not s:
        return ValueError("Inputs should be 2 non empty strings")

    # Creation of chars_t, dictionary of the characters of t
    chars_t = {}
    for char in t:
        chars_t[char] = chars_t.get(char, 0) + 1

    window = {} # Dictionary that counts characters in the window

    start, end = 0, 0 # Start and end of the window

    win_pos = float('inf'), None, None # Tuple to record smallest window
    len_win = 0 # length of window formed with characters from t

    for i in range(len(s)): # Loop through the string s

        window[s[i]] = window.get(s[i], 0) + 1 # Add char to window
        end += 1

        if s[i] in chars_t and window[s[i]] == chars_t[s[i]]: # If the character is in the string t
            len_win += 1

        while start < end and len_win == len(chars_t): # While start is below end and length of window is equal to len of chars_t
            
            char = s[start]

            if end - start + 1 < win_pos[0]: # If end - start is less than smallest window
                win_pos = (end - start + 1, start, end) # Recreate tuple

            window[char] -= 1  # Remove 1 char from the window

            if char in chars_t and window[char] < chars_t[char]: 
                len_win -= 1 # Remove 1 from the window length 

            start += 1

    return s[win_pos[1]:win_pos[2]+1] if win_pos[0] < float("inf") else ""


s1 = "ADOBECODEBANC"
t1 = "ABCA"

s2 = "a"
t2 = "a"

s3 = "a"
t3 = "aa"

for st_ in [(s1, t1), (s2, t2), (s3, t3)]:
    try:
        print(f"the smallest substring window for {st_[1]} in {st_[0]} is {minimum_window_substring(st_[0], st_[1])}")
    except Exception as e:
        print(e)