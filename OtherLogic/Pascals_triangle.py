'''
Pascal’s triangle is a triangular array of binomial coefficients. 
Write a function that takes an integer value N as input and prints the first N lines of Pascal’s triangle.
Ex:
      1
    1   1
   1  2  1
  1  3 3  1
 1 4  6  4 1
1 5 10 10 5 1
'''

def create_pascal_triangle(row_number: int) -> list:

    # Raise an error if the number of rows submitted isn't an integer
    if isinstance(row_number, int) is False:
        raise TypeError("The number of rows submitted should be an integer value!")
    
    # Raise an error if the number of rows submitted is less than 2
    if row_number < 2:
        raise ValueError("A triangle can't be less than 2 rows")
    
    else:
        triangle = [[1], [1,1]]
        print('1', '1 1', sep="\n") # Print the first 2 rows
         # Create the triangle for the first 2 rows
        for row in range(2, row_number):
            # Start after the 2nd row and create the line by adding the elements of the previous row
            triangle.insert(row, [triangle[row-1][num] + triangle[row-1][num+1] for num in range(len(triangle[row-1])-1)])
            triangle[row].insert(0, 1)
            triangle[row].append(1)
            print(' '.join(map(str, triangle[row]))) # Print each row
        
    return triangle

create_pascal_triangle(10)
    