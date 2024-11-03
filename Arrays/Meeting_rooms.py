'''
Problem: Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of conference rooms required.

Examples:

intervals = [[0, 30], [5, 10], [15, 20]]
min_meeting_rooms(intervals)
# Output: 2

intervals = [[7, 10], [2, 4]]
min_meeting_rooms(intervals)
# Output: 1
'''

def min_meeting_rooms(intervals: list) -> int:
    '''This function takes a list of meetings [start, end] and returns the number of rooms needed'''

    if not isinstance(intervals, list):
        raise TypeError("The input should be a list of lists of integers")
    
    # Create rooms needed var, start time and end time lists and sort them
    rooms_needed = 1
    start_time_list, end_time_list = [], [] # Create empty start time and end time lists

    for inter_ in intervals:

        start_time_list.append(inter_[0])
        end_time_list.append(inter_[1])
    
    # Sort start time and end time lists
    start_time_list.sort()
    end_time_list.sort()

    # create 2 pointers logic
    i, j = 0, 0

    while i < len(start_time_list)-1: # Let's move through the lists

        start = start_time_list[i+1] # Next meeting startingtime
        end = end_time_list[j] # Current meeting end time

        if start < end: # If next meeting debuts before the current end, we need an extra room

            rooms_needed += 1
            i+=1 # End we move to the next meeting starting time
        
        # Otherwise, it means the next meeting is already fed and we can move to the next meetings start and end time

        else: 

            i+=1 
            j+=1

    return rooms_needed
        

intervals1 = [[0, 30], [5, 10], [15, 20]]
intervals2 = [[7, 10], [2, 4]]
intervals3 = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]] # Output: 4
intervals4 = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11]] # Output: 4
intervals5 = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18]] # Output: 9
intervals6 = [[1, 5], [2, 6], [3, 7], [4, 8], [4, 9], [6, 10], [7, 11], [4, 12]] # Output: 6

for intervals_ in [intervals1, intervals2, intervals3, intervals4, intervals5, intervals6]:
    try:
        print(f"the number of rooms needed for the intervals {intervals_} is: {min_meeting_rooms(intervals_)}")
    except Exception as e:
        print(e)