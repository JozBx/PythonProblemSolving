'''
Problem: Alien Dictionary
There is a new alien language that uses the English alphabet. However, the order among letters is unknown to you. 
You are given a list of words from the alien dictionary, where words are sorted lexicographically by the rules of this new language.

Return a string representing the lexicographical order of the alien language. 
If there is no valid order, return an empty string. If multiple valid orders exist, return any of them.

Examples:

words = ["wrt", "wrf", "er", "ett", "rftt"]
alien_order(words)
# Output: "wertf"

words = ["z", "x"]
alien_order(words)
# Output: "zx"

words = ["z", "x", "z"]
alien_order(words)
# Output: "" (since there's a cycle and no valid order)
'''

from collections import defaultdict, deque

def alien_order(words: list) -> str:
    '''This function takes a sequence of words and returns the alien dictionary associated'''

    if not isinstance(words, list):
        raise TypeError("The input must be a list of words")

    graph = defaultdict(set)  # Initialize the graph 
    in_degree = {char: 0 for word in words for char in word} # Initialize in_degree count
    
    # Loop through words
    for i in range(len(words) - 1):
        first, second = words[i], words[i + 1]
        
        # Check for invalid case where word1 is a prefix of word2 but is longer
        if len(first) > len(second) and first.startswith(second):
            return ""
        
        # Find the first differing character and create an edge
        for c1, c2 in zip(first, second):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    in_degree[c2] += 1
                break
    
    # Queue for nodes with no incoming edges
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    order = []
    
    while queue:
        char = queue.popleft()
        order.append(char)
        
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If order includes all characters, return as a single string
    if len(order) == len(in_degree):
        return "".join(order)
    else:
        return ""  # There was a cycle, so no valid order


words1 = ["wrt", "wrf", "er", "ett", "rftt"]
words2 = ["z", "x"]
words3 = ["z", "x", "z"]
for words_ in [words1, words2, words3]:
    try:
        print(f"the alien dictionary for the sequence {words_} is: {alien_order(words_)}")
    except Exception as e:
        print(e)

