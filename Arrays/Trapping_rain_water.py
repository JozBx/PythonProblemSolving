'''
https://www.geeksforgeeks.org/trapping-rain-water/

Trapping Rainwater Problem states that given an array of n non-negative integers arr[] representing an elevation map 
 where the width of each bar is 1, compute how much water it can trap after rain.
Trapping Rainwater Problem

Trapping Rainwater Problem
Examples:

Let us understand Trapping Rainwater problem with the help of some examples:  

    Input: arr[] = {3, 0, 1, 0, 4, 0, 2}
    Output: 10
    Explanation: The expected rainwater to be trapped is shown in the above image.

    Input: arr[]   = {3, 0, 2, 0, 4}
    Output: 7
    Explanation: We trap 0 + 3 + 1 + 3 + 0 = 7 units.

    Input: arr[] = {1, 2, 3, 4}
    Output: 0
    Explanation : We cannot trap water as there is no height bound on both sides

    Input: arr[] = {10, 9, 0, 5}
    Output: 5
    Explanation : We trap 0 + 0 + 5 + 0 = 5

'''

from typing import Union

def trapping_rain_water(map: Union[list, tuple]) -> int:

    '''
    This function takes a list (or tuple) representing hills in an elevated map (values of the list)
    And returns an integer equivalent to the amount of water that could be trapped between the hills
    '''

    # Execute few checks for data consistency
    if isinstance(map, (list, tuple)) is False:
        raise TypeError("The map must be of type list or tuple")
    elif all(isinstance(hill, int) for hill in map) is False:
        raise TypeError("All the map elements must be of type integer")
    elif all(hill >= 0 for hill in map) is False:
        raise ValueError("The hills must be positive integers")
    
    trapped_water = 0

    # Create list of max height hill from end to beginning
    max_hill_rl = []
    max_val = 0
    for hill in map[::-1]:
        if hill > max_val:
            max_val = hill
        max_hill_rl.insert(0, max_val)

    # Calculate the amount of rain trapped
    max_val = 0 # reset max_val to zero
    for i in range(len(map)):
        if map[i] > max_val:
            max_val = map[i]
        if min(max_val, max_hill_rl[i]) - map[i] > 0:
            trapped_water += (min(max_val, max_hill_rl[i]) - map[i])
    
    return trapped_water

map_1 = (3, 0, 1, 0, 4, 0, 2)
map_2 = [3, 0, 2, 0, 4]
map_3 = [1, 2, 3, 4]
map_4 = (10, 9, 0, 5)
for map_ in [map_1, map_2, map_3, map_4]:
    try:
        print(f"the amount of water trapped in the elevated map {map_} is {trapping_rain_water(map_)}")
    except Exception as e:
        print(e)