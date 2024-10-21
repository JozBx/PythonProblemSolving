'''
Problem: Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is a non-negative integer.

The simplest way is to use a new array, but this would require extra space. Can you solve it in place without using extra space?

Example:

rotate_array([1,2,3,4,5,6,7], 3)
# Output: [5,6,7,1,2,3,4]

rotate_array([-1,-100,3,99], 2)
# Output: [3,99,-1,-100]
'''

# Solution without using extra space

def rotate_array(nums: list, k: int) -> None:
    
    if not isinstance(nums, list):
        raise TypeError("The array to rotate should be a list")
    elif not isinstance(k, int):
        raise TypeError("The number of element to rotate should be an integer")
    elif not k >= 0:
        raise ValueError("The number of elements to rotate should be a positive integer")
    
    n = len(nums)
    if k >= n:  # In case k is greater or equal than the array length
        k = k %n # Keep only the k % n elements to rotate
        print(f"the number of elements to rotate is more than the length of the input. \n We will rotate only the {k} remaining elements")

    # Loop through the existing array and move first element to end of the array
    i = 0

    # Solution with pop and append
    # while i < k:

    #     # Reverse the mirrored elements of the array
    #     # We then keep the same list - no extra space required
    #     # nums.append(nums.pop(0))

    #     i +=1

    # Solution using a function
    def reverse(array, start, end):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    # Reverse the array entirely
    reverse(nums, 0, n-1)

    # Reverse the left side until k
    reverse(nums, 0, k-1)

    #Reverse the right side from k to n
    reverse(nums, k, n-1)

    return nums

# Checks
r_array_1 = ([-1,-100,3,99], 2)
r_array_2 = ([1,2,3,4,5,6,7], 4)
for r_array_ in [r_array_1, r_array_2]:
    try:
        print(f"The rotated array for the input {r_array_[0]} of {r_array_[1]} elements is: {rotate_array(r_array_[0], r_array_[1])}")
    except Exception as e:
        print(e)