'''
Problem: String Compression
Given a list of characters chars, compress it in-place. The length after compression should be reduced as much as possible. 
You should modify the input array in-place with the following rules:

Begin with the first character, compress adjacent identical characters into the character followed by the count of repetitions.
If the character appears only once, do not add a count.
The list should be modified in-place and the new length of the array should reflect the compressed version.
Example:

chars = ["a", "a", "b", "b", "c", "c", "c"]
compress(chars)
# Output: 6
# The array is modified to ["a", "2", "b", "2", "c", "3"]

chars = ["a"]
compress(chars)
# Output: 1
# The array is modified to ["a"]

chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
compress(chars)
# Output: 4
# The array is modified to ["a", "b", "1", "2"]
'''

def compress(chars: list) -> int:
    '''This function takes a list of characters and returns a compressed version of it in the format ["char", "num"]'''

    if not isinstance(chars, list):
        raise TypeError("The input array should be of type list")
    
    # Create 2 pointers, point 1 and point 2, to go through the input
    point_1, point_2 = 0, 0

    while point_2 < len(chars):

        curr_char = chars[point_2] # Current char to check
        count = 0 # Create count var

        while point_2 < len(chars) and chars[point_2] == curr_char:
            point_2 += 1
            count += 1
            
        chars[point_1] = curr_char # write char to the array
        point_1 += 1

        if count > 1: # If more than 1 char
            for digit in str(count):
                chars[point_1] = digit
                point_1 += 1

    return chars[:point_1]

chars1 = ["a", "a", "b", "b", "c", "c", "c"]
chars2 = ["a"]
chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]

for chars_ in [chars1, chars2, chars3]:
    try:
        print(f"the compressed version of {chars_} is {compress(chars_)}")
    except Exception as e:
        print(e)