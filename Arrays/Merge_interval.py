'''
Problem: Merge Intervals
Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals, 
 and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example:

merge_intervals([[1,3],[2,6],[8,10],[15,18]])  
# Output: [[1, 6], [8, 10], [15, 18]]

merge_intervals([[1,4],[4,5]])  
# Output: [[1, 5]]
'''

def merge_intervals(intervals: list) -> list:
    '''This function takes a list of lists of intervals and returns a list of list of intervals where overlaping intervals are merged'''

    if not isinstance(intervals, list):
        raise TypeError("The entry must be a list of lists of intervals")
    
    output = [] # Start the output as being empty list
    sorted_intervals = sorted(intervals, key=lambda x: x[0]) # Sort intervals by bottom of the interval

    current_int = sorted_intervals[0] # Base first interval as current one

    # Loop through intervals
    for inter in sorted_intervals[1:]:

        if inter[0] > current_int[1]: # if bottom value of new interval is higher than upper value of current interval

            output.append(current_int) # append current interval to the output
            current_int = inter # set new interval as current interval

        else:

            current_int[1] = max(inter[1], current_int[1]) # Extend upper valueof current interval if newest interval upper value is superior
            
    output.append(current_int) # Append last current interval to the output
    return output

int_1 = [[1,3],[2,6],[8,10],[15,18]]
int_2 = [[1,4],[4,5]]
for int_ in [int_1, int_2]:
    try:
        print(f"the output of non overlapping intervals of {int_} is {merge_intervals(int_)}")
    except Exception as e:
        print(e)
