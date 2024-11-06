'''
Problem: Container With Most Water
You are given an array height of positive integers where each integer represents the height of a vertical line on a 2D plane. 
The lines are drawn such that the two endpoints of the line are at (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Example:

max_area([1,8,6,2,5,4,8,3,7])  # Output: 49
max_area([1,1])               # Output: 1
'''

from typing import Union

def max_area(height: Union[list, tuple]) -> tuple:
    '''
    This function takes an array of integer values and calculates the biggest surface between the integers:
    height numbers difference * height values difference
    '''
    
    if isinstance(height, (list, tuple)) is False:
        raise TypeError("The height input should be of type list or tuple")
    
    # Create min_height and max height and max_surface dict
    min_height = 0 # Start at beginning of the list
    max_height = len(height) - 1 # End of the list
    if max_height < 1:
        raise ValueError("The height input must contain at least two elements.")
    max_surface = {"surface": 0, "min_height_num": None, "max_height_num": None} 

    # Loop until min_height and max_height meet
    while min_height != max_height:
        x = max_height - min_height # Define x as diff between max height and min height
        y = min(height[min_height], height[max_height]) # Define y as minimum between values of height at min height and max height

        # If x * y is superior to existing max surface, replace the max surface dict
        if x * y > max_surface["surface"]:
            max_surface = {"surface": x * y, "min_height_num": min_height, "max_height_num": max_height}

        # Then move to left or right depending of the heights values, by default add 1 to min_height
        if height[min_height] > height[max_height]:
            max_height -= 1
        else:
            min_height += 1

    return max_surface["surface"], [max_surface["min_height_num"], max_surface["max_height_num"]]


height_1 = [1,8,6,2,5,4,8,3,7]
height_2 = [1,1]
height_3 = "test"
height_4 = [1]

for height_ in [height_1, height_2, height_3, height_4]:
    try:
        amount_of_water, coordinates = max_area(height_)
        print(f"For the heights {height_}, the biggest amount of water that can be contained in \n a container is {amount_of_water} obtained from coordinates {coordinates}")
    except Exception as e:
        print(e)