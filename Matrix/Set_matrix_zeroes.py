'''
Problem: Set Matrix Zeroes
Given an m x n matrix with positive integers only. If an element is 0, set its entire row and column to 0. You must do it in place => no extra space used

Example:

matrix = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
set_zeroes(matrix)
# Output:
# [
#   [1, 0, 1],
#   [0, 0, 0],
#   [1, 0, 1]
# ]

matrix = [
  [0, 1, 2, 0],
  [3, 4, 5, 2],
  [1, 3, 1, 5]
]
set_zeroes(matrix)
# Output:
# [
#   [0, 0, 0, 0],
#   [0, 4, 5, 0],
#   [0, 3, 1, 0]
# ]
'''

def set_zeroes(matrix: list) -> None:
    '''This function takes a matric of m x n elements and transform all the 0s in rows and cols of 0s'''
    
    if not isinstance(matrix, list):
        raise TypeError("the input must be a list of lists of integers -> m x n")
    
    len_matrix, size_matrix = len(matrix[0]), len(matrix) # Len of the matrix vertically
    
    # Loop through the matrix in classical double loop
    for c in range(len_matrix): # Loop in col
        for r in range(size_matrix): # Loop in row
            
            if matrix[r][c] == 0: # If matrix element equals 0

                matrix[0][c] = -1 * abs(matrix[0][c])
                matrix[r][0] = -1 * abs(matrix[r][0])

    # Transform all rows and columns 
    # First the columns - the first one
    for c in range(1, len_matrix):
        if matrix[0][c] <= 0:
            for row in matrix:
                row[c] = 0 # Transform all the col in zeros

    # Then the rows
    for index, row in enumerate(matrix):
        if row[0] <= 0:
            matrix[index] = [0 for x in matrix[index]] # transform all the row in 0s
    
    # Finish to check the first column
    if matrix[0][0] <= 0:
            for row in matrix:
                row[0] = 0 # Transform all the col in zeros

    return matrix


m1 = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
m2 = [
  [0, 1, 2, 0],
  [3, 4, 5, 2],
  [1, 3, 1, 5]
]
m3 = [
  [0, 1, 2, 0],
  [3, 4, 5, 2],
  [1, 3, 1, 5],
  [1, 3, 0, 5],
  [1, 3, 1, 5]
]
for m_ in [m1, m2, m3]:
    try:
        print(f"the 'zeroed' verison of the matrix {m_} is {set_zeroes(m_)}")
    except Exception as e:
        print(e)