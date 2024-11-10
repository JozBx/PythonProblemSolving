'''
https://www.geeksforgeeks.org/queries-to-check-if-a-number-lies-in-n-ranges-of-l-r/
Given N ranges and Q queries consisting of numbers. Every range consists of L and R. 
The task is to check if the given number lies in any of the given ranges or not for every query.
Note: There is no overlapping range.
'''


def number_in_range(ranges: list, queries: list) -> str:
    '''Takes an array of X ranges(tuples), find if number lies in ranges
    '''

    # Set few securities
    if isinstance(ranges, list) is False or isinstance(queries, list) is False:
        raise TypeError("The ranges and queries submitted must be of type list")
    if all(isinstance(x, (tuple, list)) for x in ranges) is False:
        raise TypeError("The ranges within the list of edges must be of type tuple or list")
    if all(isinstance(x, int) for x in queries) is False:
        raise TypeError("The number to search in the queries must be of type integer")
    
    points = []
    for L, R in ranges:
        points.append((L, 1))  # Mark L with 1
        points.append((R, 2))  # Mark R with 2
    
    # Sort by point value, and in case of tie, by marker value (L before R)
    points.sort()

    for query in queries:
        left, right = 0, len(points)
        while left < right:
            mid = (left + right) // 2
            if points[mid][0] < query:
                left = mid + 1
            else:
                right = mid
        if left < len(points):
            # Check if we found an exact match
            if points[left][0] == query:
                # If we hit an L, it overlaps
                print(f"{query} is contained in at least one of the ranges")
            else:
                # Otherwise, check the marker
                if points[left][1] == 1:
                    # If it's an L and we did not hit it exactly, it means the query is before a new range starts
                    print(f"{query} is not contained in any of the ranges")
                else:
                    # If it's an R, the query is within a range
                    print(f"{query} is contained in at least one of the ranges")
        
        else:
            print(f"{query} is not contained in any of the ranges")


a = [[5, 6], [1, 3], [8, 10]]
queries_ = [2, 3, 4, 7]
number_in_range(ranges=a, queries=queries_)