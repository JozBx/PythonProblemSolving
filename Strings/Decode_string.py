'''
Problem: Decode String
Given an encoded string, return its decoded version.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. 
You may assume that the input string is always valid; no extra white spaces, square brackets are well-formed, etc.

Note: k is a positive integer, and there may be multiple levels of nested encodings.

Examples:

s = "3[a]2[bc]"
decode_string(s)
# Output: "aaabcbc"

s = "3[a2[c]]"
decode_string(s)
# Output: "accaccacc"

s = "2[abc]3[cd]ef"
decode_string(s)
# Output: "abcabccdcdcdef"
'''

def decode_string(s: str) -> str:
    '''This function takes a coded string in specific format and decodes it'''

    if not isinstance(s, str):
        raise TypeError("The entry must be of type string")

    def str_dec(nav: int) -> str:
        '''Decode the string recursively'''

        mult = 0
        sub_str = ""

        while nav < len(s): # Loop through the string

            if s[nav].isalpha(): # If char is alpha
                
                sub_str += s[nav]
                nav += 1

            elif s[nav].isnumeric(): # If the char is a number

                mult = mult*10 +  int(s[nav])
                nav += 1
                
            elif s[nav] == "[": # Start new encoded substring

                nav, temp_str = str_dec(nav + 1)  # Recurse to decode inner part
                sub_str += mult * temp_str  
                mult = 0  # Reset multiplier after using it

            elif s[nav] == "]":  # End of the current encoded substring
                return nav + 1, sub_str

        return nav, sub_str

    _, dec_string = str_dec(0)
    return dec_string

s1 = "3[a]2[bc]"
s2 = "3[a2[c]]"
s3 = "2[abc]3[cd]ef"
s4 = "2[a2[b3[c]]]"
for s_ in [s1, s2, s3, s4]:
    try:
        print(f"The decoded string of {s_} is {decode_string(s_)}")
    except Exception as e:
        print(e)