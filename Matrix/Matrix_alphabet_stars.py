'''
https://www.geeksforgeeks.org/find-alphabet-in-a-matrix-which-has-maximum-number-of-stars-around-it/

Given a matrix mat consisting of * and lowercase English alphabets, the task is to find the character which has the maximum number of * around it 
(including diagonal elements too). If two characters have same maximum count, print lexicographically smallest character.

Examples: 

Input: 
mat[][] = {{'b', '*', '*', '*'}, 
           {'*', '*', 'c', '*'}, 
           {'*', 'a', '*', '*'}, 
           {'*', '*', '*', 'd'}}
Output: a
'a', 'b', 'c' and 'd' are surrounded by 
'7', '3', '7' and '3' stars respectively.
'a' and 'c' are surrounded by maximum stars 
but 'a' is lexicographically smaller than 'c'.

Input: 
mat[][] = {{'*', 'r', '*', '*'}, 
           {'m', 'a', 'z', '*'}, 
           {'l', '*', 'f', 'k'}, 
           {'*', '*', '*', 'd'} }
Output: f

Approach: The idea is to traverse the matrix and if a character is found then calculate the count of stars around it. 
Check at all 8 positions around it and count the number of starts.
Use a map to keep track of the character and the number of stars surrounding it. 
Then traverse the map and find the character which is surrounded by maximum stars and is lexicographically smallest.
'''

def matrix_element(matrix: list) -> str:
    '''
    This function takes a matrix of m x n element and returns the lexicographically smallest character surrounded by the biggest amount of stars
    '''

    if isinstance(matrix, list) is False:
        raise TypeError("The matrix should be of type list")
    elif matrix == []:
        raise ValueError("The matrix should have at least one row")
    elif all(isinstance(row, list) for row in matrix) is False:
        raise TypeError("The matrix rows should be of type list")
    
    # Assume character to return is None
    char_to_return = None
    max_stars = -1

    # Define row_index without a function
    row_index = -1

    # Define len and width of the matrix
    len_m = len(matrix)
    width_m = len(matrix[0])

    # Loop through the matrix:
    for row in matrix: # loop through the rows

        row_index += 1 # Add 1 to the row_index to avoid running the index function later
        col_index = -1 # Implement the same logic for the column index

        for element in row: # loop through the elements of the rows

            col_index += 1
            if element != "*": # If the element isn't a star

                count_stars = 0 # Assume zero stars around the letter

                for i in range(max(0, col_index-1), min(width_m, col_index+2), 1): # Loop in the row one by one starting on the left of letter
                    for j in range(max(0, row_index-1), min(len_m, row_index+2), 1):
                        test = matrix[i][j]
                        if matrix[i][j] == "*":
                            count_stars += 1
                
                # If the count of stars is more than current or equal but ord() is below current one then update values to return
                if (count_stars > max_stars) or (count_stars == max_stars and element < char_to_return) is True:
                    char_to_return, max_stars = element, count_stars

    return char_to_return, max_stars if char_to_return else None
    
mat_1 = [['b', '*', '*', '*'], ['*', '*', 'c', '*'], ['*', 'a', '*', '*'], ['*', '*', '*', 'd']]
mat_2 = [['*', 'r', '*', '*'], ['m', 'a', 'z', '*'], ['l', '*', 'f', 'k'], ['*', '*', '*', 'd']]

for mat in [mat_1, mat_2]:
    try:
        let, num = matrix_element(mat)
        print(f"the letter with smallest lexicography and surrounded by highest number of stars in the matrix {mat} is the letter {let} with {num} stars")
    except Exception as e:
        print(e)