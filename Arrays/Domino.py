'''
https://stackoverflow.com/questions/26189818/longest-domino-chain-sequence

I need to find the longest chain of dominoes possible, given a set of 12 randomly picked dominoes. 
I've already recursively generated all possibilities of dominoes (there are 91 possibilities using face values of 0 to 12). 
A domino consists of one "brick" with two squares on it: [a|b] where 0 =< a, b <= 12. 
Thus, an example of a domino could be [12, 0] or [6, 3] etc. Dominoes may be connect if adjacent halves have the same value.

Dominoes may be flipped to accommodate a match. For example, given [8, 4], [9, 4] could be flipped to make the pair [8, 4][4, 9]

myDomino #0: [1 12 ]
myDomino #1: [0  5 ]
myDomino #2: [7  9 ]
myDomino #3: [2  7 ]
myDomino #4: [7 12 ]
myDomino #5: [4  8 ]
myDomino #6: [8 10 ]
myDomino #7: [3 11 ]
myDomino #8: [11 12 ]
myDomino #9: [10 11 ]
myDomino #10: [2  9 ]
myDomino #11: [2  4 ]
'''

import random

def generate_dominos(max_face: int, nb_of_dominos: int):
    
    # Check that max_face and nb_of_dominos are ready for ingestion by the fuction
    if not all(isinstance(inp, int) for inp in [max_face, nb_of_dominos]):
        raise TypeError("The max number of faces and number of dominos must be integers")
    if max_face < 2:
        raise ValueError("the number of faces of the dominos must be at least 2")
    elif nb_of_dominos < 0:
        raise ValueError("The number of dominos can't be negative")

    # Create a list of tuples representing all the dominos
    all_dominos = [(side_a, side_b) for side_a in range(1, max_face+1, 1) for side_b in range(1, max_face+1, 1)]
    # Randomly select the number of dominos required
    dominos_set = random.sample(all_dominos, nb_of_dominos)
    # Return the dominos that we need to find the longest chain sequence
    return dominos_set

def find_longest_chain(dominos_list: list, chain=None):

    # Create an empty chain at the beginning, or take the existing chain in the recusive function
    if chain is None:
        chain = []

    # Define the max chain as this chain
    max_chain = chain

    # Start iterating through the dominos
    for domino_nb in range(len(dominos_list)):
        next_domino = dominos_list[domino_nb] # Next domino in line
        remaining_dominos = dominos_list[:domino_nb] + dominos_list[domino_nb+1:] # Create a list with the remaining dominos

        if not chain or chain[-1][1] == next_domino[0]:
            # If the element on the very right of the chain equals the left element of the next domino, activate the recursivity
            new_chain = chain + [next_domino]
            valid_chain = find_longest_chain(remaining_dominos, new_chain)
            if len(valid_chain) > len(max_chain):
                max_chain = valid_chain
        
        elif not chain or chain[-1][1] == next_domino[1]:
            # Else, if the element on the very right of the chain equals the right element of the next domino, activate the recursivity
            new_chain = chain + [(next_domino[1], next_domino[0])]
            valid_chain = find_longest_chain(remaining_dominos, new_chain)
            if len(valid_chain) > len(max_chain):
                max_chain = valid_chain

    return max_chain # Return the max chain


# Create the set of dominos
dominos = generate_dominos(max_face=6, nb_of_dominos=12)
# Find the longest chain
longest_chain = find_longest_chain(dominos)

print("Length of longest chain: ", len(longest_chain), "\n")
print("Longest chain of dominoes: ", longest_chain)

