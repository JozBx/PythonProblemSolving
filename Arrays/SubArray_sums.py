'''
Problem: Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example:

subarray_sum([1, 1, 1], 2)  
# Output: 2

subarray_sum([1, 2, 3], 3)  
# Output: 2
'''

def subarray_sum(nums: list, k: int) -> int:
    '''
    This function takes a list of integers nums and an integer k and returns a list of the total number of continuous subarrays whose sum = k
    '''

    if not isinstance(nums, list):
        raise TypeError("The nums entry must be a list of integers")
    
    # Hash map to store cumulative sum frequencies
    prefix_sum_count = {0: 1}
    
    current_sum = 0
    count = 0
    
    # Iterate over the array
    for num in nums:
        current_sum += num  # Update the cumulative sum
        
        # Check if (current_sum - k) exists in the map
        if current_sum - k in prefix_sum_count:
            count += prefix_sum_count[current_sum - k]
        
        # Update the map with the current cumulative sum
        if current_sum in prefix_sum_count:
            prefix_sum_count[current_sum] += 1
        else:
            prefix_sum_count[current_sum] = 1
    
    return count

arr_1 = [[1, 2, 3, 1], 3]
arr_2 = [[1, 2, 1, 3, 5, 6, 4], 3]
arr_3 = [[1, 2, 1, 3, 1, 1, 1], 3]
for arr_ in [arr_1, arr_2, arr_3]:
    try:
        print(f"The total number of continuous subarrays whose sum = {arr_[1]} in {arr_[0]} is {subarray_sum(arr_[0], arr_[1])}")
    except Exception as e:
        print(e)