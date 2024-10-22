'''
Problem: Find All Duplicates in an Array
Given an integer array nums of length n where all integers are in the range [1, n], some elements appear twice and others appear once. 
Find all the elements that appear twice in this array.

You must solve the problem without using extra space (i.e., modify the input array in place) and in O(n) time.

Example:

find_duplicates([4,3,2,7,8,2,3,1])
# Output: [2, 3]

find_duplicates([1,1,2])
# Output: [1]

find_duplicates([1])
# Output: []
'''

# Solution: place a sign in the array so that the code understands the number has already been seen earlier
# Note: This method works only if there's just one duplicate in the array i.e not [3, 3, 3, 1] => would produce messed up results
# To solve this other kind of problem, I'd use a marker as 0 if number already crossed and then remove all zeros

def find_duplicates(array: list) -> list:
    '''This functions takes a list of integers and returns all the duplicated integers within the list'''

    if not isinstance(array, list):
        raise TypeError("The input array should be of type list")

    duplicates = [] # Create empty duplicates list
    
    # Loop through the array and mark elements
    for i in range(len(array)):

        # Use the absolute value of the current element as an index
        index = abs(array[i]) - 1
        
        # If the number at that index is negative, it's a duplicate
        if array[index] < 0:
            duplicates.append(index + 1)
        else:
            # Transform the number at the index of the array as the negative
            array[index] = -array[index]
    
    return duplicates


dup_1 = [4,3,2,7,8,2,3,1]
dup_2 = [1,1,2]
dup_3 = [1]

for dup_ in [dup_1, dup_2, dup_3]:
    try:
        print(f"The duplicate(s) from the array {dup_} is (are): {find_duplicates(dup_)}")
    except Exception as e:
        print(e)