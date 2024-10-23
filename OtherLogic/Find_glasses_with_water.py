'''
https://www.geeksforgeeks.org/find-water-in-a-glass/

There are some glasses with equal capacity as 1 litre. The glasses are kept as follows: 

                   1
                 2   3
              4    5    6
            7    8    9   10

You can put water to the only top glass. If you put more than 1-litre water to 1st glass, water overflows and fills equally in both 2nd and 3rd glasses. 
Glass 5 will get water from both 2nd glass and 3rd glass and so on. 

Derived: how many glasses will have water in them with X liters of water to pour?
'''

def numb_glasses(liters: int) -> int:
    '''
    This function takes a number of liters and returns of many glasses of water will have water in them
    '''

    if isinstance(liters, int) is False:
        raise TypeError("The number of litters must be of type integer")
    
    # Initialize a list to represent glasses (we need to find how many rows can fit the water)
    glasses = [[0] * k for k in range(1, 100)]  # Arbitrary large number of rows (100) to handle overflow.
    
    # Pour X liters of water into the top glass
    glasses[0][0] = liters
    
    # Simulate the filling and overflow process
    for row in range(len(glasses) - 1):
        for col in range(len(glasses[row])):
            if glasses[row][col] > 1:
                # Calculate the overflow
                overflow = glasses[row][col] - 1
                glasses[row][col] = 1  # The glass can hold a maximum of 1 liter
                
                # Distribute the overflow equally to the next row
                glasses[row + 1][col] += overflow / 2
                glasses[row + 1][col + 1] += overflow / 2
    
    # Count how many glasses have water in them (water > 0)
    count = 0
    for row in glasses:
        for glass in row:
            if glass > 0:
                count += 1

    return count

l_1 = 2
l_2 = 8
l_3 = 23
for l in [l_1, l_2, l_3]:
    try:
        print(f"the number of glasses with water from {l} liters poured is {numb_glasses(l)}")
    except Exception as e:
        print(e)