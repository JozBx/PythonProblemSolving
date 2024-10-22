'''
Problem: Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example:
python
Copy code
top_k_frequent([1,1,1,2,2,3], 2)  
# Output: [1, 2]

top_k_frequent([1], 1)  
# Output: [1]
'''

# Solution 1: Without heap and collections modules

def top_k_frequent(nums: list, k: int) -> list:
    '''This function takes an array of integers and return the k most frequent elements'''

    if not isinstance(nums, (list, tuple)):
        raise TypeError("The entry should be a list or a tuple")
    if not isinstance(k, int):
        raise TypeError("The number of most frequent elements to return should be an integer")
    
    freq = {}    # Set the frequencies as empty dict

    # Loop through the array
    for el in nums:

        if el in freq: # If element already in frequency
            freq[el] += 1 # Add 1 to the count

        else:
            freq[el] = 1 # Else add new element in freq with count as 1

    sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True) # Sort the freq dictionary in descending order

    return [num[0] for num in sorted_freq[:k]]

# Solution 2: using collections and heapq modules

from collections import Counter
import heapq

def top_k_frequent(nums: list, k: int) -> list:
    '''This function takes an array of integers and returns the k most frequent elements'''
    
    if not isinstance(nums, (list, tuple)):
        raise TypeError("The entry should be a list or a tuple")
    if not isinstance(k, int):
        raise TypeError("The number of most frequent elements to return should be an integer")
    
    # Step 1: Count the frequency of each element using Counter
    freq = Counter(nums)
    
    # Step 2: Use a heap to find the k most frequent elements
    return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda item: item[1])]

# Test cases
nums_1 = ([1, 1, 1, 2, 2, 3], 2)  # Expected output: [1, 2]
nums_2 = ([1], 1)                 # Expected output: [1]

for nums_ in [nums_1, nums_2]:
    try:
        print(f"The {nums_[1]} most frequent integers in the array {nums_[0]} are {top_k_frequent(nums_[0], nums_[1])}")
    except Exception as e:
        print(e)
