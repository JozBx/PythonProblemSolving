'''
https://stackoverflow.com/questions/55587041/looping-through-string-array-find-the-two-strings-with-the-most-overlap-and-mer

I have a string array named 'collection' as shown below. 
I want to loop through the array and find the strings with the most overlap - that is the most same characters in a row. 
Once I find the two strings I want to append a new string to the array with the concatenation of these two strings and then 
remove the original strings. The catch is that the concatenation must ignore common characters. 

For example: 'hello wo' & 'o world' will become 'hello world'. I want to repeat this process until one string is left.

collection = ["all is well", "ell that en", "hat end", "t ends well"];
longestOverlap = 0;
longestOverlapChars = '';

# Output
"all is well that ends well"
'''

from typing import Union

def concat_strings(array: Union[list, tuple]) -> str:
    '''
    This function concatenates strings with the largest overlap
    '''
    
    if not isinstance(array, (list, tuple)):
        raise TypeError("The input must be an array (list or tuple)")

    len_array = len(array)
    string = array[0]  # Initialize with the first string of the array
    max_overlap = ""

    for i in range(1, len_array):  # Loop through strings starting with the 2nd in the array
        len_str_ = len(array[i])  # Temporary length for checking overlap
        
        # Find the largest overlap by reducing from the right side of current string and left side of next string
        while array[i][:len_str_] != string[-len_str_:] and len_str_ > 0:
            len_str_ -= 1

        # Concatenate the remaining non-overlapping part of the second string
        string = string + array[i][len_str_:]
        
        # Update the max overlap if the current overlap is the largest
        current_overlap = array[i][:len_str_]
        if len(current_overlap) > len(max_overlap):
            max_overlap = current_overlap

    return string


s1 = ["all is well", "ell that en", "hat end", "t ends well"]
s2 = 122344
for s_ in [s1, s2]:
    try:
        print(f"From the array {s_}, the string with no overlapping sections is: {concat_strings(s_)}")
    except Exception as e:
        print(e)