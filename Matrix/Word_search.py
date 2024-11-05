'''
Problem: Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Examples:

board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word = "ABCCED"
word_search(board, word)
# Output: True

board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word = "SEE"
word_search(board, word)
# Output: True

board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word = "ABCB"
word_search(board, word)
# Output: False
'''

def word_search(board: list, word: str) -> bool:
    '''This function takes a matrix board and a word and checks if the letters of word are in board'''

    if not isinstance(board, list) or not isinstance(word, str):
        raise TypeError("The inputs must be a list of lists and a word to check")
    
    rows, cols = len(board), len(board[0]) # Create rows and cols
    
    # Define a search function
    def search(r, c, index):
        # If the current index matches the length of the word, word is found
        if index == len(word):
            return True
        
        # Check for out-of-bounds or mismatches
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False
        
        # Mark the current cell as visited by changing its value temporarily
        temp = board[r][c]
        board[r][c] = "#"
        
        # Explore all four possible directions (up, down, left, right)
        found = (search(r + 1, c, index + 1) or   # Move down
                 search(r - 1, c, index + 1) or   # Move up
                 search(r, c + 1, index + 1) or   # Move right
                 search(r, c - 1, index + 1))     # Move left
        
        # Backtrack by restoring the current cell's value
        board[r][c] = temp
        
        return found
    
    # Iterate over each cell in the grid and start a search if the first character matches
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and search(r, c, 0):
                return True
    
    return False

board1, word1 = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "ABCCED"
board2, word2 = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "SEE"
board3, word3 = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], "ABCB"
for board_, word_ in [(board1, word1), (board2, word2), (board3, word3)]:
    try:
        if word_search(board_, word_):
            print(f"the word {word_} can be found in {board_}")
        else:
            print(f"the word {word_} can't be found in {board_}")
    except Exception as e:
        print(e)