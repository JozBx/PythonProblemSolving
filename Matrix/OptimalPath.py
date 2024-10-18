"""
Instructions to candidate:

You are a point collector. 
You must create the path that returns the biggest amount of points on your way from the start of your journey (always the bottom left of the Grid)
to the end of your journey (always the upper right of the Grid)

Note: You can only travel either north (up) or east (right).

Here is an example:
                                                         ^
               [[0,0,0,0,5], End                         N
                [0,1,1,1,0],                         < W   E >
          Start [2,0,0,0,0]]                             S
                                                         v
The total for this example would be 10 (2+0+1+1+1+0+5).
"""

def optimalPath(grid: list) -> int:
    '''
    Function finding the optimal path to collect more points between the start (bottom left) and end (upper right) of the Grid
    '''

    if isinstance(grid, list) is False:
        raise TypeError("The grid input should be of type list")

    # Answer the case of an empty grid
    if not grid[0]:
        return 0

    # Search for the size of the grid (number of lists), and its depth (size of each list)
    rows = len(grid)
    cols = len(grid[0])

    def collectMaxPoints(i, j):
        '''Recursive function / nested function to calculate the optimal path
        '''

        # Base case: when reaching the top-right corner
        if i == 0 and j == cols - 1:
            return grid[i][j]
        
        # Initialize the maximum points collected from this point
        max_points = 0

        # Check if we can move right
        if j + 1 < cols:
            max_points = max(max_points, collectMaxPoints(i, j + 1))

        # Check if we can move up
        if i - 1 >= 0:
            max_points = max(max_points, collectMaxPoints(i - 1, j))

        # Return the value at grid[i][j] plus the best path's max points
        return grid[i][j] + max_points

    return collectMaxPoints(rows - 1, 0) # Start at the bottom row on the left corner


# Examples
print(optimalPath([[0, 0, 0, 0, 5],
                    [0, 1, 1, 1, 0],
                    [2, 0, 0, 0, 0]])) #10
print(optimalPath([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])) #33
print(optimalPath([[7, 0, 0, 0, 5],
                    [8, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0]])) #21
print(optimalPath([[1, 2],
                   [3, 4]])) #9