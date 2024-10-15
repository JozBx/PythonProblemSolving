'''
Problem: Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example:

longest_palindrome("babad")  
# Output: "bab" or "aba"

longest_palindrome("cbbd")  
# Output: "bb"
'''

def expand_around_center(s: str, left: int, right: int) -> str:
    # Expand the window while the characters are equal and within bounds
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # Return the palindromic substring found (note: left and right will have over-expanded)
    return s[left + 1:right]

def longest_palindrome(s: str) -> str:
    '''
    This function takes a string and returns the longest palindrome
    '''

    # Check that the input is a string

    if isinstance(s, str) is False:
        raise TypeError("The input should be of type string")
    
    longest_palindrome = "" # set up longest palindrome to empty string

    # Loop through the string
    for i in range(len(s)):

        # Expand around the center for odd-length palindromes
        odd_palindrome = expand_around_center(s, i, i)
        
        # Expand around the center for even-length palindromes
        even_palindrome = expand_around_center(s, i, i + 1)
        
        # Update the longest palindrome found
        longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)
    
    return longest_palindrome

s1 = "babad"
s2 = "cbbd"
s3 = "nweuognwrgonajgngjownejgnqejgnefjnaejghgnaerjl"
for s_ in [s1, s2, s3]:
    try:
        print(f"the longest palindrome in the string {s_} is {longest_palindrome(s_)}")
    except Exception as e:
        print(e)