'''
Problem: Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example:

longest_substring("abcabcbb")  # Output: 3 ("abc")
longest_substring("bbbbb")     # Output: 1 ("b")
longest_substring("pwwkew")    # Output: 3 ("wke")

Constraints:
The input string will consist of English letters, digits, symbols, and spaces.
The input string can be empty.
'''

def longest_substring(entry: str) -> int:
    '''
    This function takes a string and returns the length of the longest substring without repeating characters.
    '''
    if not isinstance(entry, str):
        raise TypeError("The entry must be of type str")
    
    # Dictionary to store the last index of each character
    char_index_map = {}
    longest = 0
    start = 0  # This is the left pointer of the window
    longest_substr = ""  # Store the actual longest substring
    
    # Loop through the string with the 'end' pointer
    for end, char in enumerate(entry):
        # If the character is already in the window, move the start pointer
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        
        # Update the last seen index of the character
        char_index_map[char] = end
        
        # Calculate the current window length
        current_window_length = end - start + 1
        
        # Update the longest substring if we found a longer one
        if current_window_length > longest:
            longest = current_window_length
            longest_substr = entry[start:end + 1]
    
    return longest_substr

sub1 = "abcabcbb"
sub2 = "bbbbb"
sub3 = "pwwkew"
sub4 = 3
sub5 = "pwwwkewatq"

for s in [sub1, sub2, sub3, sub4, sub5]:
    try:
        print(f"The longest substring without repeating character in the string {s} is {longest_substring(s)}")
    except Exception as e:
        print(e)