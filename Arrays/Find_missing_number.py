'''
Problem: Find the Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example:

missing_number([3, 0, 1])  
# Output: 2

missing_number([0, 1])  
# Output: 2

missing_number([9,6,4,2,3,5,7,0,1])  
# Output: 8
'''

# Solution 1: Using mathematical formula
def missing_number(nums: list[int]) -> int:
    '''
    This function takes a list of integers and returns the missing number in the range [0, n].
    '''
    
    if not isinstance(nums, (list, tuple)):
        raise TypeError("The input must be a list or tuple")
    
    n = len(nums)
    
    # Sum of numbers from 0 to n
    expected_sum = n * (n + 1) // 2
    
    # Actual sum of the numbers in the array
    actual_sum = sum(nums)
    
    # The missing number is the difference between the expected sum and the actual sum
    return expected_sum - actual_sum

#Solution 2: Without using mathematical formula

def missing_number(nums: list) -> int:
    '''
    This function takes an array of integers and returns the one missing, if no missing returns max + 1
    '''

    # Raise an exception if the nums is not list or tuple
    if isinstance(nums, (tuple, list)) is False:
        raise TypeError("The entry must be of type list or tuple")
    
    # Use the length of the array:
    len_num = len(nums)

    # Assume there is no missing number
    missing_num = 0

    # Loop through the array and make the difference between the actual sum and what it should be
    for i in range(len_num):
        missing_num += (i + 1 - nums[i])
    
    # If 0 not in the array return 0
    if missing_num == 0 and 0 not in nums:
        return 0
    
    # Else return the len of the array if no missing value, else return the missing value
    return len_num if missing_num == 0 else missing_num

nums_1 = [3, 2, 1]
nums_2 = [1, 0]
nums_3 = [9,6,4,2,3,5,7,0,1]
for nums_ in [nums_1, nums_2, nums_3]:
    try:
        print(f"the missing number in the array {nums_} is {missing_number(nums_)}")
    except Exception as e:
        print(e)