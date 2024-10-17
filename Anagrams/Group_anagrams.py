'''
Problem: Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.

Example:

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

group_anagrams([""])
# Output: [[""]]

group_anagrams(["a"])
# Output: [["a"]]
'''

def group_anagrams(strs: list[str]) -> list[list[str]]:
    '''
    This function takes a list of strings and returns a list of lists of string anagrams.
    '''
    
    if not isinstance(strs, list):
        raise TypeError("The input should be of type list")
    
    # Dictionary to store grouped anagrams
    anagrams_dict = {}
    
    for string in strs:
        # Sort the string to use as the key for anagrams
        sorted_string = "".join(sorted(string))
        
        # Group strings by their sorted form
        if sorted_string in anagrams_dict:
            anagrams_dict[sorted_string].append(string)
        else:
            anagrams_dict[sorted_string] = [string]

    # Return the grouped anagrams
    return list(anagrams_dict.values())


gp1 = ["eat", "tea", "tan", "ate", "nat", "bat", "eat", "tea", "tan", "ate", "nat", "bat"]
gp2 = [""]
gp3 = ["a"]

for gp_ in [gp1, gp2, gp3]:
    try:
        print(f"{group_anagrams(gp_)}")
    except Exception as e:
        print(e)
    


