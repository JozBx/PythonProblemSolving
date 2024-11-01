'''
Problem: Longest Consecutive Sequence
Given an unsorted array of integers nums, find the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time complexity.

Examples:

nums = [100, 4, 200, 1, 3, 2]
longest_consecutive(nums)
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, its length is 4.

nums = [0,3,7,2,5,8,4,6,0,1]
longest_consecutive(nums)
# Output: 9
'''

def longest_consecutive(nums: list) -> int:
    '''This function takes a list of integers and returns the number of the longest consecutive sequence'''

    if not isinstance(nums, list):
        raise TypeError("The entry should be of type list")

    num_set = list(set(nums)) # Remove duplicates
    seq = 1 # Set the max sequence to 1

    for val in num_set:
        # Only start counting if it's the beginning of a sequence
        if val - 1 not in num_set:
            current_val = val
            current_seq = 1

            # Count up while the next number exists in the set
            while current_val + 1 in num_set:
                current_val += 1
                current_seq += 1

            # Update the longest streak found
            seq = max(seq, current_seq)
    
    return seq


nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
for nums_ in [nums1, nums2]:
    try:
        print(f"The longest consecutive sequence in {nums_} is made of {longest_consecutive(nums_)} numbers")
    except Exception as e:
        print(e)