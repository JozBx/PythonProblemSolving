'''
https://www.geeksforgeeks.org/find-water-in-a-glass/

There are some glasses with equal capacity as 1 litre. The glasses are kept as follows: 

                   1
                 2   3
              4    5    6
            7    8    9   10

You can put water to the only top glass. If you put more than 1-litre water to 1st glass, water overflows and fills equally in both 2nd and 3rd glasses. 
Glass 5 will get water from both 2nd glass and 3rd glass and so on. 

If you have X litre of water and you put that water in a top glass, how much water will be contained by the jth glass in an ith row?

Example. If you will put 2 litres on top. 
1st – 1 litre 
2nd – 1/2 litre 
3rd – 1/2 litre

 For 2 Liters Water

The approach is similar to Method 2 of the Pascal’s Triangle. If we take a closer look at the problem, the problem boils down to Pascal’s Triangle.  

                           1   ---------------- 1
                 2   3 ---------------- 2
                      4    5    6  ------------ 3
            7    8    9   10  --------- 4

Each glass contributes to the two glasses down the glass. Initially, we put all water in the first glass. 
Then we keep 1 litre (or less than 1 litre) in it and move rest of the water to two glasses down to it. 
We follow the same process for the two glasses and all other glasses till the ith row. There will be i*(i+1)/2 glasses till ith row. 
'''

from typing import Union

def find_water(liters: Union[int, float], row: int, col: int) -> int:
    '''
    This function takes a number of liters and returns of many glasses of water will have water in them
    '''

    if isinstance(liters, (int, float)) is False:
        raise TypeError("The number of litters must be of type integer")
    elif isinstance(row, int) is False:
        raise TypeError("The row number must be of type integer")
    elif isinstance(col, int) is False:
        raise TypeError("The col number must be of type integer")
    
    row_ = row - 1 # Create python row: row -1 to start at zero
    col_ = col - 1 # Create python col: col -1 to start at zero

    # Create a list of lists with the glasses with an extra row
    glasses = [[0]*i for i in range(1, row+1)]

    # Put water in the first glass:
    glasses[0][0] = liters

    # Loop through the rows until reaching the line of the desired glass
    for r in range(row):
        # Loop through the glasses 
        for c in range(r+1):

            if glasses[r][c] > 1:

                # Keep the overflow and state that the glass is full
                overflow = glasses[r][c] - 1
                glasses[r][c]  = 1

                # Distribute the overflow into the 2 glasses below
                glasses[r+1][c] += overflow/2
                glasses[r+1][c+1] += overflow/2

    return glasses[row_][col_]


l_1 = [2, 2, 2]
l_2 = [4, 3, 2]
l_3 = [8, 4, 3]
for l in [l_1, l_2, l_3]:
    try:
        print(f"for {l} liters poured the glass at position row {l[1]}, col {l[2]} has {find_water(l[0], l[1], l[2])} liter of water in it")
    except Exception as e:
        print(e)