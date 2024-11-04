'''
Problem: Find the Celebrity
Suppose you are at a party with n people (labeled from 0 to n - 1), and you are trying to find a celebrity. 
A celebrity is defined as someone who:

Everyone else knows, but
They know no one.
You are given access to a function knows(a, b) which tells you whether person a knows person b. 
You need to find out who the celebrity is (if there is one) by querying the knows function as few times as possible.

Return the label of the celebrity if there is a celebrity at the party. If there is no celebrity, return -1.

Example:

# Suppose the knows function is defined as follows:
def knows(a: int, b: int) -> bool:
    # returns True if person a knows person b, otherwise False
    pass

n = 3
# Example: Matrix of knows function
# [ [1, 1, 0],
#   [0, 1, 0],
#   [1, 1, 1] ]
find_celebrity(n)
# Output: 1
# Explanation: Person 1 is the celebrity because everyone knows them, and they know no one.
'''

def find_celebrity(n: int, know: list) -> int:
    '''This function takes a number of people n and a matrix of knowledge know and finds the number of celebrities if any'''

    if not isinstance(n, int) or not isinstance(know, list):
        raise TypeError("The entries must be a number of people n and a matrix n * n of 0 and 1")
    
    celebs = [] # Assume there are no celebrities
    known = {}
    knows = {}

    # Loop through the list
    for i in range(n):
        for j in range(n):
            if know[i][j] == 1:
                known[j] = known.get(j, 0) + 1
                knows[i] = knows.get(i, 0) + 1

    for person in range(n):
        if known[person] == n and knows[person] == 1:
            celebs.append(str(person))

    return ", ".join(celebs) if len(celebs) > 0 else None


tup1 = 4, [
    [1, 1, 0, 1],  # Person 0 knows 1, 3
    [0, 1, 0, 1],  # Person 1 knows 3
    [1, 1, 1, 1],  # Person 2 knows everyone
    [0, 0, 0, 1]   # Person 3 knows no one (could be celebrity)
]
tup2 = 3, [[1, 1, 0], [0, 1, 0], [1, 1, 1]]
for tup_ in [tup1, tup2]:
    try:
        print(f"The celebrity(ies) in the pop {tup_[1]} is/are {find_celebrity(tup_[0], tup_[1])}")
    except Exception as e:
        print(e)
